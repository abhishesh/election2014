import duckdb
import pandas as pd


def main():
    # Path to the JSON file
    json_file_path = "election_data.json"

    # Path to save the output CSV
    output_csv_path = "election_data_analysed.csv"

    # Create a DuckDB connection
    con = duckdb.connect(database=":memory:")  # Using in-memory database

    # Read JSON data into a DuckDB table
    # Assuming the JSON structure is a list of objects (common case)
    con.execute(
        f"CREATE TABLE election_data AS SELECT * FROM read_json('{json_file_path}')"
    )

    # Execute SQL query
    result = con.execute(
        """SELECT
                   state,
                   constituency,
                   candidate,
                   party,
                   evm_votes,
                   postal_votes,
                   total_votes,
                   perc_votes,
                   Rnk
                   FROM (
                       SELECT
                         state,
                         constituency,
                         candidate,
                         party,
                         evm_votes,
                         postal_votes,
                         total_votes,
                         perc_votes,
                         RANK() OVER (PARTITION BY state, constituency ORDER BY CAST(total_votes AS INT) DESC) AS Rnk
                       FROM election_data
                   ) ranked
                   WHERE Rnk <= 2"""
    ).fetchdf()

    # Save results to CSV
    result.to_csv(output_csv_path, index=False)

    # Close the DuckDB connection
    con.close()


if __name__ == "__main__":
    main()

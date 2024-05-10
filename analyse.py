import json
import duckdb
import pandas as pd


def main():
    # Load JSON data from file
    with open("./data.json") as file:
        data = json.load(file)

    # Initialize an empty DataFrame to collect all normalized data
    all_normalized_data = pd.DataFrame()

    # Assuming 'data' is a list of records
    for record in data:
        # Normalize the current record
        normalized_df = pd.json_normalize(
            record, record_path="Candidates", meta=["State", "Constituency"]
        )

        # Append to the full DataFrame
        all_normalized_data = pd.concat(
            [all_normalized_data, normalized_df], ignore_index=True
        )

    # Connect to DuckDB
    con = duckdb.connect(database=":memory:", read_only=False)

    # Create a table and insert data into DuckDB
    con.register("election_data", all_normalized_data)
    con.execute("CREATE TABLE election_data AS SELECT * FROM election_data")

    # Save the entire table as csv
    con.execute(
        f"COPY election_data TO election_data_raw.csv WITH (HEADER TRUE, DELIMITER ',')"
    )

    # Close the connection when done
    con.close()


if __name__ == "__main__":
    main()

import pandas as pd
import duckdb

# Load the CSV file
file_path = "election_results.csv"
election_results = pd.read_csv(file_path)

# Clean the data by replacing '-' with 0 and converting to appropriate data types
election_results_cleaned = election_results.replace("-", 0)
election_results_cleaned["Total Votes"] = election_results_cleaned[
    "Total Votes"
].astype(int)
election_results_cleaned["% of Votes"] = (
    election_results_cleaned["% of Votes"].str.replace("%", "").astype(float)
)

# Create a DuckDB in-memory database and load the data
con = duckdb.connect(database=":memory:")
con.execute("CREATE TABLE election_results AS SELECT * FROM election_results_cleaned")

# Define the query to aggregate the winners from each constituency
query = """
SELECT
    Constituency,
    State,
    Candidate AS Winner,
    Party,
    "Total Votes"::INTEGER,
    "% of Votes"::FLOAT
FROM
    election_results
QUALIFY ROW_NUMBER() OVER (PARTITION BY Constituency ORDER BY "Total Votes"::INTEGER DESC) = 1
"""

# Execute the query and fetch results
winners = con.execute(query).fetchdf()

# Display the results
print(winners)

# Optionally, save the results to a new CSV file
winners.to_csv("election_winners_by_constituency.csv", index=False)

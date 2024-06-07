# Winners by lowest margin


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

# Define the query to find candidates who won by the lowest margin in each constituency
query = """
WITH ConstituencyResults AS (
    SELECT
        Constituency,
        State,
        Candidate,
        Party,
        CAST("Total Votes" AS INTEGER) AS TotalVotes,
        CAST("% of Votes" AS FLOAT) AS PercentVotes,
        ROW_NUMBER() OVER (PARTITION BY Constituency ORDER BY CAST("Total Votes" AS INTEGER) DESC) AS rank
    FROM
        election_results
),
WinnerRunnerUp AS (
    SELECT
        Constituency,
        State,
        MAX(CASE WHEN rank = 1 THEN Candidate END) AS Winner,
        MAX(CASE WHEN rank = 1 THEN Party END) AS WinnerParty,
        MAX(CASE WHEN rank = 1 THEN TotalVotes END) AS WinnerVotes,
        MAX(CASE WHEN rank = 2 THEN Candidate END) AS RunnerUp,
        MAX(CASE WHEN rank = 2 THEN Party END) AS RunnerUpParty,
        MAX(CASE WHEN rank = 2 THEN TotalVotes END) AS RunnerUpVotes
    FROM
        ConstituencyResults
    GROUP BY
        Constituency, State
)
SELECT
    Constituency,
    State,
    Winner,
    WinnerParty,
    WinnerVotes,
    RunnerUp,
    RunnerUpParty,
    RunnerUpVotes,
    WinnerVotes - RunnerUpVotes AS Margin
FROM
    WinnerRunnerUp
ORDER BY
    Margin ASC
"""

# Execute the query and fetch results
winners_by_lowest_margin = con.execute(query).fetchdf()

# Display the results
print(winners_by_lowest_margin)

# Optionally, save the results to a new CSV file
winners_by_lowest_margin.to_csv("winners_by_lowest_margin.csv", index=False)

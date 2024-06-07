import glob
import json
from bs4 import BeautifulSoup


def get_text_safe(column):
    """Helper function to safely extract text from BeautifulSoup Tag, avoiding NoneType errors."""
    return column.text.strip() if column else ""


# List to hold all candidate data across all files
all_candidates_data = []

# Loop through all .htm files in the 'data' directory
for filename in glob.glob("data/*.htm"):
    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

        # Find the table with class 'table-party'
        table = soup.find("table", class_="table-party")
        if table:
            # Attempt to extract state and constituency from the table header or a designated element
            header = soup.find(
                "th", colspan="9"
            )  # Adjust if the header structure is different
            if header:
                header_text = header.text.strip()
                state_constituency = header_text.split(
                    "-"
                )  # Adjust based on actual text format
                state = state_constituency[0].strip()
                constituency = (
                    state_constituency[1].strip() if len(state_constituency) > 1 else ""
                )

            rows = table.find_all("tr")[3:]  # Adjust the index to skip header rows
            for row in rows:
                cols = row.find_all("td")
                if (
                    len(cols) >= 7
                ):  # Ensure there are enough columns to match your data structure
                    candidate_info = {
                        "state": state,
                        "constituency": constituency,
                        "OSN": get_text_safe(cols[0]),
                        "candidate": get_text_safe(cols[1]),
                        "party": get_text_safe(cols[2]),
                        "evm_votes": get_text_safe(cols[3]),
                        "postal_votes": get_text_safe(cols[4]),
                        "total_votes": get_text_safe(cols[5]),
                        "perc_votes": get_text_safe(cols[6]),
                    }
                    if candidate_info["candidate"] != "Total":
                        all_candidates_data.append(candidate_info)
        else:
            print(f"No 'table-party' found in {filename}")

# Save the collected data to a JSON file
with open("election_data.json", "w", encoding="utf-8") as json_file:
    json.dump(all_candidates_data, json_file, ensure_ascii=False, indent=4)

print("Data successfully saved to 'election_data.json'.")

from bs4 import BeautifulSoup
import pandas as pd
import glob
import os


def parse_page(filepath):
    # Load the HTML content
    with open(filepath, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract constituency and state name
    page_title = soup.find("div", class_="page-title")
    constituency = page_title.find("h2").find("span").text.strip()
    state = page_title.find("h2").find("strong").text.strip()
    constituency_clean = constituency.split("-")[1].split("(")[0].strip()
    state_clean = state.replace("(", "").replace(")", "")

    # Find the table
    table = soup.find("table", class_="table table-striped table-bordered")

    # Extract table headers
    headers = [header.text.strip() for header in table.find_all("th")]

    # Extract table rows
    rows = []
    for row in table.find("tbody").find_all("tr"):
        cells = row.find_all("td")
        row_data = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
        # Remove 'S.N.' key from row_data
        if "S.N." in row_data:
            del row_data["S.N."]
        # Add constituency and state to each row
        row_data["Constituency"] = constituency_clean
        row_data["State"] = state_clean
        rows.append(row_data)

    # Extract footer totals if needed
    footer = table.find("tfoot").find("tr")
    footer_cells = footer.find_all("th")

    footer_data = {
        headers[i]: footer_cells[i].text.strip() if i < len(footer_cells) else ""
        for i in range(len(headers))
    }

    return rows


# Use glob to find all HTML files in the data directory
result = []
for filename in glob.glob("data/*.htm"):
    data = parse_page(filename)
    result.extend(data)

# Convert to DataFrame
df = pd.DataFrame(result)

# Save DataFrame to CSV
df.to_csv("election_data_raw.csv", index=False)
print("Data has been saved to election_data_raw.csv")

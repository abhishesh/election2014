import requests
import os

name_lookup = {
    "U01": "Andaman & Nicobar Islands",
    "U02": "Chandigarh",
    "U03": "Dadra & Nagar Haveli and Daman & Diu",
    "U06": "Lakshadweep",
    "U05": "NCT OF Delhi",
    "U07": "Puducherry",
    "U08": "Jammu and Kashmir",
    "U09": "Ladakh",
    "S01": "Andhra Pradesh",
    "S02": "Arunachal Pradesh",
    "S03": "Assam",
    "S04": "Bihar",
    "S05": "Goa",
    "S06": "Gujarat",
    "S07": "Haryana",
    "S08": "Himachal Pradesh",
    "S10": "Karnataka",
    "S11": "Kerala",
    "S12": "Madhya Pradesh",
    "S13": "Maharashtra",
    "S14": "Manipur",
    "S15": "Meghalaya",
    "S16": "Mizoram",
    "S17": "Nagaland",
    "S18": "Odisha",
    "S19": "Punjab",
    "S20": "Rajasthan",
    "S21": "Sikkim",
    "S22": "Tamil Nadu",
    "S23": "Tripura",
    "S24": "Uttar Pradesh",
    "S25": "West Bengal",
    "S26": "Chhattisgarh",
    "S27": "Jharkhand",
    "S28": "Uttarakhand",
    "S29": "Telangana",
}

entities_dict = {
    "U01": 1,
    "U02": 1,
    "U03": 2,
    "U05": 7,
    "U06": 1,
    "U07": 1,
    "U08": 5,
    "U09": 1,
    "S01": 25,
    "S02": 2,
    "S03": 14,
    "S04": 40,
    "S05": 2,
    "S06": 26,
    "S07": 10,
    "S08": 4,
    "S10": 28,
    "S11": 20,
    "S12": 29,
    "S13": 48,
    "S14": 2,
    "S15": 2,
    "S16": 1,
    "S17": 1,
    "S18": 21,
    "S19": 13,
    "S20": 25,
    "S21": 1,
    "S22": 39,
    "S23": 2,
    "S24": 80,
    "S25": 42,
    "S26": 11,
    "S27": 14,
    "S28": 5,
    "S29": 17,
}

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

for item, ctr in entities_dict.items():
    for i in range(1, ctr + 1):
        filename = f"Constituencywise{item}{i}.htm"
        try:
            url_to_open = f"https://results.eci.gov.in/PcResultGenJune2024/{filename}"
            print("Saving -----", url_to_open)
            response = requests.get(url_to_open)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            with open(f"data/{filename}", "wb") as f:
                f.write(response.content)
        except Exception as e:
            print("Exception occurred:", e)
            print("Filename:", filename)

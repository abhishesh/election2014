Election Data Crawler
=====================
A python web crawler that gets constituency wise election results for 543 seats in Lok Sabha from election commission website. Its a great tool for psephology enthusiasts who want to analyse the results from difrent angles. It Converts the data in HTML tables to JSON format, that makes analysis way easier. 

Usage
=====

    python webscrapy.py
    python parse.py

Sample Output
==============
We get a JSON file of constituency wise data. This can be used to aggregate various reports for analysis

```json
[
    {
        "state": "Telangana",
        "constituency": "Mahabubabad",
        "OSN": "1",
        "candidate": "Kalluri. Venkateswara Rao.",
        "party": "Communist Party of India",
        "evm_votes": "45694",
        "postal_votes": "25",
        "total_votes": "45719",
        "perc_votes": "4.65"
    },
    {
        "state": "Telangana",
        "constituency": "Mahabubabad",
        "OSN": "2",
        "candidate": "Kavitha Malothu",
        "party": "Telangana Rashtra Samithi",
        "evm_votes": "461824",
        "postal_votes": "285",
        "total_votes": "462109",
        "perc_votes": "46.98"
    },
    {
        "state": "Telangana",
        "constituency": "Mahabubabad",
        "OSN": "3",
        "candidate": "Jatothu Hussain",
        "party": "Bharatiya Janata Party",
        "evm_votes": "25333",
        "postal_votes": "154",
        "total_votes": "25487",
        "perc_votes": "2.59"
    }
]
```

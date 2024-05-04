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
        "State": "Telangana",
        "Constituency": "Mahabubabad",
        "OSN": "1",
        "Candidate": "Kalluri. Venkateswara Rao.",
        "Party": "Communist Party of India",
        "EVM Votes": "45694",
        "Postal Votes": "25",
        "Total Votes": "45719",
        "% of Votes": "4.65"
    },
    {
        "State": "Telangana",
        "Constituency": "Mahabubabad",
        "OSN": "2",
        "Candidate": "Kavitha Malothu",
        "Party": "Telangana Rashtra Samithi",
        "EVM Votes": "461824",
        "Postal Votes": "285",
        "Total Votes": "462109",
        "% of Votes": "46.98"
    },
    
]
```

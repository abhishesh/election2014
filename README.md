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

    {    
        "Constituency": "Allahabad", 
        "State": "Uttar Pradesh",
        "Candidates": [
            {
                "Candidate": "SHYAMA CHARAN GUPTA", 
                "Party": "Bharatiya Janata Party", 
                "Votes": "313772"
            }, 
            {
                "Candidate": "KUNWAR REWATI RAMAN SINGH ALIAS MANI", 
                "Party": "Samajwadi Party", 
                "Votes": "251763"
            }
            .
            .
            .
        ]
    }

# Indian Election Results Crawler

This repository contains a Python-based web crawler designed to extract and store Indian election results. 
The collected data is stored in a format optimized for querying with [DuckDB](https://duckdb.org/) for analysis


## Features

- Crawls official and public sources for Indian election results - **webscrapy.py**
- Extracts results and stores them in a structured format (JSON) - **parse.py**
- Compatible with DuckDB for efficient querying and analysis - **analyse.py**

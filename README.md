# Global Interest in the 2020 U.S. Election

<div align="center">
    <img alt="Screenshot" src="files/interest.png">
</div>

<p align="center">
  <a>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.8.10-green">
  </a> 
  <a>
    <img alt="Pandas" src="https://img.shields.io/badge/Pandas-1.4.0-orange">
  </a> 
  <a>
    <img alt="Numpy" src="https://img.shields.io/badge/Numpy-1.22.1-lightblue">
  </a>
  <a>
    <img alt="Pytrends" src="https://img.shields.io/badge/Pytrends-4.8.0-blue">
  </a> 
</p>


## Table of Contents
- [Description](#Description)
- [Installation](#Installation)
- [Usage](#Usage)

## Description

This is a data science project tracking global interest in US-related topics through Google Trends. The scripts collect and analyze data from various sources, including online webpages and an unofficial Google Trends API. The data is stored in .csv tables. I visualized the data in a Jupyter Notebook and produced a 25-page research paper for a university course (the course did not involve coding - the scripts I wrote helped me gather the data necessary to write the paper).

## Installation

The project requires no specific installation, though it does require that certain python dependencies be installed. 

The project was written on a 64-bit [MacOS 11 Big Sur](https://apps.apple.com/us/app/macos-big-sur/id1526878132?mt=12) using [Python 3.8.10](https://www.python.org/downloads/release/python-3810/). It uses a few external dependencies, including pandas, numpy, and third-party apis.

To download all python dependencies with pip, type in the command line:
```bash
$ pip install -r requirements.txt
```

## Usage

I do not recommend running the scripts now. The scraped websites and APIS used might be outdated or deprecated. Moreover, the data collected would be different, since it collects data up to the present day. It is better to view the research by reading the paper. 

Nevertheless, to run the scripts, just run them through a python interpreter. 
```bash
python3 scripts/country_table_creator.py
python3 scripts/hourly_df_creator.py
python3 scripts/minthly_df_creator.py
python3 scripts/sattistical_additions.py
```
The scripts will then save the found data in the .csv files in tables. 

To visualize the data, open visualizations/grapher.ipynb in a Jupyter Notebook reader. 
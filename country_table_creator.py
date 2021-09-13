"""
Includes a function returning a table, and executes the function, generating file country_table.csv.
"""
# %%
import wbgapi as wbank
import requests
import global
import pandas as pd
from bs4 import BeautifulSoup

def country_table_creator():
    """
    Returns table with un country name, alpha2 code, alpha3 code, UN membership, G-20 membership.
    """
    # Retrieve html page
    req_iban = requests.get(global.IBANLINK).text
    soup_iban = BeautifulSoup(req_iban, 'lxml')
    # Get the iban table with all the necesary rows
    table_iban = soup_iban.find("table", id="myTable").find("tbody")
    rows_iban = table_iban.find_all("tr")
    # Initiate column lists
    country_names = []
    alpha_2s = []
    alpha_3s = []
    g_20_memberships = []

    for row in rows_iban:
        cells = row.find_all("td")
        # Eliminate whitespace
        country_name = cells[0].text.strip()
        alpha_2 = cells[1].text.strip()
        alpha_3 = cells[2].text.strip()
        # Set membership 
        g_20_membership = alpha_2 in global.G20
        # Append to column lists
        country_names.append(country_name)
        alpha_2s.append(alpha_2)
        alpha_3s.append(alpha_3)
        g_20_memberships.append(g_20_membership)
    
    # Include "Worldwide"
    country_names.append("Worldwide")
    alpha_2s.append("")
    alpha_3s.append("")
    g_20_memberships.append(True) # Included for comparisons
    # Create resulting df
    dictionary = {"Country": country_names,
                  "Alpha_2": alpha_2s,
                  "Alpha_3": alpha_3s,
                  "G20": g_20_memberships}
    
    # UN column is false by default
    df = pd.DataFrame(dictionary)
    df["UN"] = False
    
    # Retrieve html page
    req_un = requests.get(global.UNLINK).text
    soup_un = BeautifulSoup(req_un, 'lxml')
    # Extract list of UN members, exclude first row
    un_countries = soup_un.find_all("h2")[1:] # Avoid superfluous
    for un_country in un_countries:
        # un_country = pattern_country_name.sub("\1", un_country.text)
        un_country = un_country.text
        print(un_country)
        if un_country in list(df["Country"]):
            df.loc[df["Country"] == un_country, "UN"] = True
        # If it can't find the country by name, manually insert the Alpha 3 code
        else:
            code = input(f"Country: {un_country} - Alpha 3:")
            df.loc[df["Alpha_3"] == code, "UN"] = True
            
    # Include "Worldwide", again for comparison
    df.loc[df["Country"] == "Worldwide", "UN"] = True
    # Exclude non-un countries
    df = df[df["UN"] == True]
    df.drop(columns=["UN"], inplace=True)
    
    return df
        

# %%
country_table = country_table_creator()
# %%
# Add 2004 population as 2004_POP column
for row in wbank.data.fetch("SP.POP.TOTL", economy=country_table["Alpha 3"], time=2004):
    country_table.loc[country_table["Alpha_3"] == row["economy"], "2004_POP"] = row["value"]
    
# Add 2019 GDP per capita as GDPPCAP column
for row in wbank.data.fetch("NY.GDP.PCAP.CD", economy=country_table["Alpha 3"], time=2019):
    country_table.loc[country_table["Alpha_3"] == row["economy"], "GDPPCAP"] = row["value"]
    
# %%
# Save countrytable
country_table.to_csv("country_table.csv")
# %%

"""
Includes a function returning the table with interest in "United States" by UN country,
and executes the function, generating file monthly_df.csv.
"""
# %%
import pandas as pd
from pytrends.request import TrendReq

from .global_vars import UNITEDSTATES

def monthly_df_creator():
    
    temp_df_list = []
    country_table = pd.read_csv("../tables/country_table.csv")
    master_us_pytrends = TrendReq(hl='en-US', tz=360)

    for country_name, code in zip(country_table["Country"], country_table["Alpha_2"]):
        # Print to track country in command line
        print(country_name)
        # Get data, handle exception if country is not found
        try:
            master_us_pytrends.build_payload(UNITEDSTATES,
                                             timeframe = "all",
                                             geo=code)
        except Exception as e:
            if "Google returned a response with code 400" in str(e):
                print("Caught error 400")
                continue
            else:
                raise(e)
        
        temp_df = master_us_pytrends.interest_over_time()
        # Drop irrelevant column
        temp_df.drop(columns="isPartial", inplace=True)
        # Rename the values column as the country column
        temp_df.columns = [country_name]
        # Add the results to the list of dfs
        temp_df_list.append(temp_df)

    # Concatenate all the columns
    monthly_df = pd.concat(temp_df_list, axis=1)
    print("Finished")
    
    return monthly_df

df = monthly_df_creator()
df.to_csv("tables/monthly.csv")
"""
This file makes valuable additions to the country_table.csv table, including 5 new columns.
The file includes three functions that perform statistical calculations. 
"""
# %%
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

def residual(x_values, y_values, ind=17):
    """
    Runs regression between x_values and y_values, but without the observation corresponding to the ind, then calculates the difference between the predicted value for the observation and the observation.
    """
    # In these "try" arrays, Take out the indexth element
    x_values_try = x_values[:ind] + x_values[(ind+1):]
    y_values_try = y_values[:ind] + y_values[(ind+1):]
    # Format the arrays in numpy to be able to run the regression
    x_values_rgr = np.array(x_values).reshape((-1, 1))
    x_values_rgr_try = np.array(x_values_try).reshape((-1, 1))
    y_values_rgr_try = np.array(y_values_try)
    # Fit the "try" arrays
    model = LinearRegression().fit(x_values_rgr_try, 
                                   y_values_rgr_try)
    # Get the predicted values for the complete array of the independent variable
    pred_values = model.predict(x_values_rgr)
    # Return the residual
    return y_values[ind] - pred_values[ind]

def residual_list_generator(master_df, months=24, ind=17):
    """
    This function loops through the columns of a df, which has country columns,
    and retrieves the last *months* values, and provides residuals according to
    the indexth element.
    """
    residuals = []
    #Loop through columns (countries)
    for col in master_df.columns:
        # Skip the index "date" column
        if col == "date":
            continue
        #Extract values
        x_values = list(range(months))
        y_values = list(df[col])[-24:]
        #Append country residual
        residuals.append(residual(x_values=x_values,
                                  y_values=y_values,
                                  ind=ind))
    # Return list of residuals, in the same order as columns
    return residuals

def means_and_errors(df, ind=12):
    """
    Returns a list of the mean and standard deviation for interest in 
    "United States" in the last 12 months.
    """
    means_list = []
    errors_list = []
    #Loop through columns (countries)
    for col in df.columns:
        # Get all numbers up to the indexth element
        data = np.array(list(df[col])[:ind])
        # get mean and standard deviation of sample
        avg = np.mean(data)
        std = np.std(data, ddof=1) / np.sqrt(np.size(data))
        # Append results
        means_list.append(avg)
        errors_list.append(std)
    
    return means_list, errors_list
    
# %%
# Import monthly df, eliminate spurious column, and set "date" as index
df = pd.read_csv("monthly_df.csv", header=0)
df.drop(columns=["Unnamed: 0"], inplace=True)
df.set_index("date", inplace=True)
df.fillna(0, inplace=True)
# Import country_table, set "country" as index
country_table = pd.read_csv("country_tableComplete(for_now).csv")
country_table.set_index("Country", inplace=True)
# Gather means, 
means, errors = means_and_errors(df=df)
november_interest = list(df.loc["2020-11-01"])
residuals = residual_list_generator(df)
# Create "addition" df with means and errors
addition = pd.DataFrame({"2004_MEAN": means,
                         "2004_SIGMA": errors,
                         "2020_NOV": november_interest,
                         "RESIDUAL": residuals},
                        index=df.columns)
# Include the "multiple" column
addition["MULTIPLE"] = addition["2020_NOV"] / (addition["2020_NOV"] - addition["RESIDUAL"])
# Concatenate the two dfs, and save to file.
new_df = pd.concat([country_table, addition], axis=1)
new_df.to_csv("country_table.csv")
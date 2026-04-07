"""
===============================================================================
Script Name:       Parcel Acres Validation and Conversion
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-04-07

Description:
-------------
This script demonstrates how to use Python and Pandas to perform practical
tabular data operations on GIS parcel datasets. Specifically, it:
    - Loads Excel or CSV parcel datasets
    - Ensures numeric consistency for the ACRES field
    - Detects negative or invalid ACRES values
    - Interactively converts negative values to positive, if requested
    - Calculates a new SQ_FT field based on ACRES
    - Provides a clean preview of updated data

Usage:
------
1. Update the 'source' path to point to your Excel or CSV file.
2. Run the script. If negative ACRES values exist, you will be prompted
   to convert them to positive values.
3. The script will create a new 'SQ_FT' column and print the first
   few rows of the updated data.
4. For CSV files, use `pd.read_csv()` instead of `pd.read_excel()`.


Notes:
------
- Designed for small to medium-sized parcel datasets; very large datasets 
  may require memory optimization.
- Demonstrates a workflow similar to ArcGIS Calculate Field or QA checks,
  using Pandas for interactive and reproducible processing.
- Can be extended to include additional validation, reporting, or export
  to Excel/CSV.
===============================================================================
"""
import pandas as pd

source=r"[EXCEL FILE PATH]"

df=pd.read_excel(source) #load xlsx file, to load csv, run read_csv(file)

##print(df.head())   # first 5 rows
##print(df.columns)  # column names
##print(df.info())   # data types + nulls
#Create a new field and calculate over the values
##df["SQ_FT"]=df["ACRES"].fillna(0) * 43560 #will treat blank cells with zero for new calculation
##print(df.head())

df["ACRES"]=pd.to_numeric(df["ACRES"],errors="coerce") #Ensure field is numeric
negatives=df[df["ACRES"]<0]
if (df["ACRES"]<0).any():
##if not negatives.empty:
    print("Negative values found in ACRES:")
    print(negatives[['ACRES']])
    while True:
        user_input=input("Automatically convert negative numbers to positives? (y/n): ").strip().lower()
        if user_input in ["y", "yes"]:
            df["ACRES"]=df["ACRES"].abs()
            print("Negative values converted")
            break
        elif user_input in ["n", "no"]:
            print("Process stopped")
            exit()
        else:
            print("Invalid input. Please enter a 'y' or 'n'.")
df["SQ_FT"]=df["ACRES"].fillna(0)*43560
print("\nUpdated Data:")
print(df[["ACRES", "SQ_FT"]].head())

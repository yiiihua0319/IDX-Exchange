import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

folder = "Data"

months = [
    "202401", "202402", "202403", "202404", "202405", "202406",
    "202407", "202408", "202409", "202410", "202411", "202412",
    "202501", "202502", "202503", "202504", "202505", "202506",
    "202507", "202508", "202509", "202510", "202511", "202512",
    "202601", "202602", "202603"
]

sold_files = []
listing_files = []

for ym in months:
    sold_df = pd.read_csv(f"{folder}/CRMLSSold{ym}.csv")
    listing_df = pd.read_csv(f"{folder}/CRMLSListing{ym}.csv")

    # print(f"Sold {ym} rows before concat:", len(sold_df))
    # print(f"Listing {ym} rows before concat:", len(listing_df))

    sold_files.append(sold_df)
    listing_files.append(listing_df)

sold_all = pd.concat(sold_files, ignore_index=True)
listings_all = pd.concat(listing_files, ignore_index=True)

print("Sold total rows after concat:", len(sold_all))
print("Listings total rows after concat:", len(listings_all))

print("Sold rows before Residential filter:", len(sold_all))
sold = sold_all[sold_all["PropertyType"] == "Residential"]
print("Sold rows after Residential filter:", len(sold))

print("Listings rows before Residential filter:", len(listings_all))
listings = listings_all[listings_all["PropertyType"] == "Residential"]
print("Listings rows after Residential filter:", len(listings))

sold.to_csv("Sold_Residential.csv", index=False)
listings.to_csv("Listings_Residential.csv", index=False)
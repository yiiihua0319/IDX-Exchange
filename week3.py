# Step 1 – Fetch the mortgage rate data from FRED
import pandas as pd
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']


# Step 2 – Resample weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (
mortgage.groupby('year_month')['rate_30yr_fixed']
.mean()
.reset_index()
)


# Step 3 – Create a matching year_month key on the MLS datasets
# read the sold and listing datasets
res_sold = pd.read_csv('res_sold.csv')
res_listing = pd.read_csv('res_listing.csv')

# Sold dataset — key off CloseDate
res_sold['year_month'] = pd.to_datetime(res_sold['CloseDate']).dt.to_period('M')
# Listings dataset — key off ListingContractDate
res_listing['year_month'] = pd.to_datetime(
res_listing['ListingContractDate']
).dt.to_period('M')


# Step 4 – Merge
res_sold_with_rates = res_sold.merge(mortgage_monthly, on='year_month', how='left')
res_listing_with_rates = res_listing.merge(mortgage_monthly, on='year_month', how='left')


# Step 5 – Validate the merge
# Check for any unmatched rows (rate should not be null)
print(res_sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(res_listing_with_rates['rate_30yr_fixed'].isnull().sum())
# Preview
print(
res_sold_with_rates[
['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']
].head()
)


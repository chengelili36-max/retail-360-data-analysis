import pandas as pd
import numpy as np
import kagglehub
import datetime as dt


path = kagglehub.dataset_download("mohammadtalib786/retail-sales-dataset")
df = pd.read_csv(f"{path}/retail_sales_dataset.csv")

df['Date'] = pd.to_datetime(df['Date'])
# 确保 Total Amount 准确性
df.columns = df.columns.str.strip().str.replace(' ', '_')
df['Total_Amount'] = df['Quantity'] * df['Price_per_Unit']


study_date = df['Date'].max() + dt.timedelta(days=1)
rfm = df.groupby('Customer_ID').agg({
    'Date': lambda x: (study_date - x.max()).days,
    'Transaction_ID': 'count',
    'Total_Amount': 'sum'
}).rename(columns={'Date': 'Recency', 'Transaction_ID': 'Frequency', 'Total_Amount': 'Monetary'})

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm['RFM_Total'] = rfm['R_Score'] + rfm['F_Score'] + rfm['M_Score']

def segment_customer(df):
    if df['RFM_Total'] >= 12: return 'Core Customers'
    elif df['RFM_Total'] >= 8: return 'Potential Customers'
    else: return 'Churn Risk Customers'

rfm['Customer_Segment'] = rfm.apply(segment_customer, axis=1)

df.to_csv('retail_clean_main.csv', index=False) 
rfm.to_csv('rfm_segmentation.csv') 
# -*- coding: utf-8 -*-
"""DataAnalysis1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FZVEHRIPpnWnYrr3qysiv9Za-70C5wxs
"""

import pandas as pd

df_store = pd.read_csv("/content/stores_data_set.csv")
df_sales = pd.read_csv("/content/sales_data_set.csv")
df_features = pd.read_csv("/content/Features_data_set.csv")

df_store.head()

df_sales.head()

df_features.head()

df_features.drop(columns="IsHoliday",axis=1,inplace=True) # axis = 0 is row, axis =1 is column

df_features.head()

df_store_sales= pd.merge(df_store,df_sales,on="Store")

df_store_sales.shape

df_store_sales.head(10)

df_final = pd.merge(df_features,df_store_sales,on=["Store","Date"])

df_final.head()

df_final.shape

df_store_sales.shape

df_final.info()

df_final["Date"]=pd.to_datetime(df_final["Date"],format="%d/%m/%Y")

df_final.info()

df_final["Year"] = df_final["Date"].dt.year

df_final.head()

df_final["Month"] = df_final["Date"].dt.month
df_final["Day"] = df_final["Date"].dt.day
df_final["Day_of_week"] = df_final["Date"].dt.day_of_week
df_final["Week"] = df_final["Date"].dt.isocalendar().week

df_final.tail(100)


#This script convert all the the numerical columns to their required form

import pandas as pd

df= pd.read_csv(r'C:\Users\hp\Desktop\STOCKX PRICES\RED TABLE.csv')

df

#to convert this column into float data type
df['Percentage Positive Feedback'] = df['Percentage Positive Feedback'].astype('float32')

#to remove US $ from from the values this column and convert it into int64
df['Price'] = df['Price'].str.replace('US', '').str.replace('$', '').astype('int64')

#to convert this column into float data type
df['Feedback Score'] = df['Feedback Score'].astype('float32')

df.to_csv('RED TABLE.csv')

import pandas as pd
import matplotlib.pyplot as plt

# Load collected data
stock_data = pd.read_csv('stock_data.csv', index_col=0, parse_dates=True)

stock_data.index = pd.to_datetime(stock_data.index, errors='coerce')
print(stock_data.index)
if stock_data.index.isnull().any():
    print("WARNING: Some index entries could not be converted to dates and are NaT (Not-a-Time).")

stock_data = stock_data[~stock_data.index.isnull()] 


# Plot closing prices over time
plt.figure(figsize=(12,6))
plt.plot(stock_data['Close'])
plt.title('Stock Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.grid(True)
plt.show()

# Check for missing values in each column
print("Missing values in each column:")
print(stock_data.isnull().sum())

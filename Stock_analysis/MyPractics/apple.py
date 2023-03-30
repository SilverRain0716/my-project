import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

# Define the stock ticker and time period
ticker = "AAPL"
start_date = "2015-01-01"
end_date = datetime.now().strftime('%Y-%m-%d')

# Fetch the stock data from Yahoo Finance API
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Visualize the stock data
plt.plot(stock_data['Close'])
plt.title('Stock Price Data')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Split the data into training and testing sets
train_data = stock_data[:'2021-01-01']
test_data = stock_data['2021-01-01':]

# ARIMA model
arima_model = ARIMA(train_data['Close'], order=(1, 1, 1))
arima_fit = arima_model.fit()
arima_predictions = arima_fit.forecast(steps=len(test_data))[0]

# Linear regression model
lr_model = LinearRegression()
lr_model.fit(train_data.index.values.reshape(-1, 1), train_data['Close'])
lr_predictions = lr_model.predict(test_data.index.values.reshape(-1, 1))

# Random forest model
rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(train_data.index.values.reshape(-1, 1), train_data['Close'])
rf_predictions = rf_model.predict(test_data.index.values.reshape(-1, 1))

# Visualize the predicted values against the actual values
plt.plot(test_data.index, arima_predictions, label='ARIMA')
plt.plot(test_data.index, lr_predictions, label='Linear Regression')
plt.plot(test_data.index, rf_predictions, label='Random Forest')
plt.plot(test_data.index, test_data['Close'], label='Actual')
plt.title('Stock Price Predictions')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Evaluate the models using mean absolute error (MAE)
arima_mae = abs(arima_predictions - test_data['Close']).mean()
lr_mae = abs(lr_predictions - test_data['Close']).mean()
rf_mae = abs(rf_predictions - test_data['Close']).mean()
print('ARIMA MAE:', arima_mae)
print('Linear Regression MAE:', lr_mae)
print('Random Forest MAE:', rf_mae)

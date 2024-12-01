import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/fuel_prices_metro_cities.csv'
df = pd.read_csv(file_path)

# Convert the date column to datetime
df['date_of_revision'] = pd.to_datetime(df['date_of_revision'], format="%d-%b-%y")


def forecast_fuel_prices(df, fuel_type):
    """
    Forecast prices for given fuel type (Petrol or Diesel)
    """
    df['days_from_start'] = (df['date_of_revision'] - df['date_of_revision'].min()).dt.days

    # Prepare data
    X = df['days_from_start'].values.reshape(-1, 1)
    y = df[f'{fuel_type}_Price_in_Mumbai'].values

    # Fit the model
    model = LinearRegression()
    model.fit(X, y)

    # Create future dates
    last_date = df['date_of_revision'].max()
    future_dates = pd.date_range(start=last_date, periods=730, freq='D')  # 2 years
    future_days = (future_dates - df['date_of_revision'].min()).days

    # Make predictions
    predictions = model.predict(future_days.values.reshape(-1, 1))

    return future_dates, predictions


def plot_fuel_predictions(df, petrol_forecast, diesel_forecast):
    plt.figure(figsize=(15, 8))

    # Plot historical data
    plt.plot(df['date_of_revision'], df['Petrol_Price_in_Mumbai'],
             label='Historical Petrol Price', color='blue', alpha=0.6)
    plt.plot(df['date_of_revision'], df['Diesel_Price_in_Mumbai'],
             label='Historical Diesel Price', color='green', alpha=0.6)

    # Plot predictions
    plt.plot(petrol_forecast[0], petrol_forecast[1],
             label='Predicted Petrol Price', color='red', linestyle='--')
    plt.plot(diesel_forecast[0], diesel_forecast[1],
             label='Predicted Diesel Price', color='orange', linestyle='--')

    plt.title('Fuel Price Predictions (2-Year Forecast)')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    plt.show()


# Run predictions for both fuel types
petrol_forecast = forecast_fuel_prices(df, 'Petrol')
diesel_forecast = forecast_fuel_prices(df, 'Diesel')

# Plot both predictions
plot_fuel_predictions(df, petrol_forecast, diesel_forecast)

import pandas as pd
import os

def calculate_ice_vehicle_costs(vehicle_name, initial_vehicle_cost, annual_maintenance_cost, annual_insurance_cost,
                                other_annual_costs, fuel_efficiency, annual_distance, fuel_price_column, df, start_date, end_date):
    # Calculate annual fuel consumption
    annual_fuel_consumption = annual_distance / fuel_efficiency

    # Filter the dataset for the desired date range
    filtered_df = df[(df['date_of_revision'] >= start_date) & (df['date_of_revision'] <= end_date)]

    # Calculate the total fuel cost over the period
    total_fuel_cost = filtered_df[fuel_price_column].mean() * annual_fuel_consumption * (end_date.year - start_date.year + 1)

    # Calculate total costs over the period
    total_maintenance_cost = annual_maintenance_cost * (end_date.year - start_date.year + 1)
    total_insurance_cost = annual_insurance_cost * (end_date.year - start_date.year + 1)
    total_other_costs = other_annual_costs * (end_date.year - start_date.year + 1)

    total_cost = (initial_vehicle_cost + total_fuel_cost +
                  total_maintenance_cost + total_insurance_cost +
                  total_other_costs)

    # Round the total cost to 2 decimal places
    total_cost_rounded = round(total_cost, 2)

    print(f"Total cost for {vehicle_name} from {start_date.date()} to {end_date.date()}: {total_cost_rounded} INR")

def load_ice_data():
    # Construct the path using os.path
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'fuel_prices_metro_cities.csv')
    df = pd.read_csv(file_path)

    # Convert the date column to datetime format
    df['date_of_revision'] = pd.to_datetime(df['date_of_revision'], format='%d-%b-%y')
    return df

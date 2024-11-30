import pandas as pd
import os

def calculate_electric_vehicle_costs(vehicle_name, initial_vehicle_cost, annual_maintenance_cost, annual_insurance_cost,
                                     other_annual_costs, electricity_consumption_per_km, annual_distance, df, start_date, end_date
                                     ):

    # Calculate annual electricity consumption
    annual_electricity_consumption = annual_distance * electricity_consumption_per_km

    # Adjust the start and end years for fiscal year calculation
    fiscal_start_year = start_date.year if start_date.month >= 4 else start_date.year - 1
    fiscal_end_year = end_date.year if end_date.month >= 4 else end_date.year - 1

    # Filter the dataset for the desired fiscal year range
    filtered_df = df[(df['Year'] >= fiscal_start_year) & (df['Year'] <= fiscal_end_year)]

    # Calculate the average electricity price over the period
    average_electricity_price = filtered_df['Domestic'].mean()

    # Calculate the total electricity cost over the period
    total_years = fiscal_end_year - fiscal_start_year + 1
    total_electricity_cost = average_electricity_price * annual_electricity_consumption * total_years

    # Calculate total costs over the period
    total_maintenance_cost = annual_maintenance_cost * total_years
    total_insurance_cost = annual_insurance_cost * total_years
    total_other_costs = other_annual_costs * total_years

    total_cost = (initial_vehicle_cost + total_electricity_cost +
                  total_maintenance_cost + total_insurance_cost +
                  total_other_costs)

    # Round the total cost to 2 decimal places
    total_cost_rounded = round(total_cost, 2)

    print(f"Total cost for {vehicle_name} from {start_date.date()} to {end_date.date()}: {total_cost_rounded} INR")

def load_ev_data():
    # Construct the path using os.path
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'electricity_prices_2015-2024.csv')
    df = pd.read_csv(file_path)

    # Convert the 'Year' column to integer for filtering
    df['Year'] = df['Year'].apply(lambda x: int(x.split('-')[0]))
    return df

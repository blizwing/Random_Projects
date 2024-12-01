import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def calculate_ice_vehicle_future_costs(vehicle_params, start_date, prediction_years=3):
    """
    Calculate future costs for ICE vehicle using predicted fuel prices

    Parameters:
    vehicle_params: dict with keys:
        - vehicle_name: str
        - initial_vehicle_cost: float
        - annual_distance: float
        - fuel_efficiency: float (km/L)
        - annual_maintenance_cost: float
        - annual_insurance_cost: float
        - other_annual_costs: float
    start_date: datetime
    prediction_years: int
    """
    # Load and prepare fuel price data
    file_path = 'data/fuel_prices_metro_cities.csv'
    df = pd.read_csv(file_path)
    df['date_of_revision'] = pd.to_datetime(df['date_of_revision'], format="%d-%b-%y")

    # Create fuel price prediction model
    df['days_from_start'] = (df['date_of_revision'] - df['date_of_revision'].min()).dt.days
    X = df['days_from_start'].values.reshape(-1, 1)
    y = df['Petrol_Price_in_Mumbai'].values

    model = LinearRegression()
    model.fit(X, y)

    # Generate future dates and predictions
    future_dates = pd.date_range(start=start_date, periods=prediction_years * 365, freq='D')
    future_days = (future_dates - df['date_of_revision'].min()).days
    predicted_prices = model.predict(future_days.values.reshape(-1, 1))

    # Calculate yearly fuel costs using predicted prices
    annual_fuel_consumption = vehicle_params['annual_distance'] / vehicle_params['fuel_efficiency']
    yearly_fuel_costs = []

    for year in range(prediction_years):
        year_start_idx = year * 365
        year_end_idx = (year + 1) * 365
        avg_fuel_price = np.mean(predicted_prices[year_start_idx:year_end_idx])
        yearly_fuel_cost = annual_fuel_consumption * avg_fuel_price
        yearly_fuel_costs.append(yearly_fuel_cost)

    # Calculate total costs
    total_fuel_cost = sum(yearly_fuel_costs)
    total_maintenance_cost = vehicle_params['annual_maintenance_cost'] * prediction_years
    total_insurance_cost = vehicle_params['annual_insurance_cost'] * prediction_years
    total_other_costs = vehicle_params['other_annual_costs'] * prediction_years

    total_cost = (vehicle_params['initial_vehicle_cost'] +
                  total_fuel_cost +
                  total_maintenance_cost +
                  total_insurance_cost +
                  total_other_costs)

    # Print detailed breakdown
    print(f"\nCost Breakdown for {vehicle_params['vehicle_name']} ({prediction_years} Years):")
    print("-" * 60)
    print(f"Initial Vehicle Cost: ₹{vehicle_params['initial_vehicle_cost']:,.2f}")
    print(f"Total Fuel Cost: ₹{total_fuel_cost:,.2f}")
    print(f"Total Maintenance Cost: ₹{total_maintenance_cost:,.2f}")
    print(f"Total Insurance Cost: ₹{total_insurance_cost:,.2f}")
    print(f"Other Costs: ₹{total_other_costs:,.2f}")
    print("-" * 60)
    print(f"Total Cost of Ownership: ₹{total_cost:,.2f}")

    return total_cost


# Example usage with your vehicle parameters
vehicle_params = {
    "vehicle_name": "TVS Raider 125",
    "initial_vehicle_cost": 155000,
    "annual_distance": 15000,  # km per year
    "fuel_efficiency": 50,  # km/L
    "annual_maintenance_cost": 8000,
    "annual_insurance_cost": 1200,
    "other_annual_costs": 400  # PUC and other costs
}

start_date = pd.to_datetime('2024-12-01')
total_cost = calculate_ice_vehicle_future_costs(vehicle_params, start_date)

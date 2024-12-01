import pandas as pd

from Electric_Vehicles.ElectricCostCalculation import calculate_electric_vehicle_costs, load_ev_data
from ICE_Vehicles.ICECostCalculation import calculate_ice_vehicle_costs, load_ice_data
from Visualize.visualize import visualize_cost_comparison

# Define the date range
start_date = pd.to_datetime('2019-06-16', format='%Y-%m-%d')
end_date = pd.to_datetime('2024-11-29', format='%Y-%m-%d')

# Load datasets
ice_df = load_ice_data()
ev_df = load_ev_data()

# Calculate costs for an ICE vehicle
ice_costs = calculate_ice_vehicle_costs(
    vehicle_name="TVS Raider 125",
    initial_vehicle_cost=155000,
    annual_insurance_cost=2500,
    other_annual_costs=200,         #PUC
    fuel_efficiency=50,  # km/l for petrol
    annual_distance=15000,
    fuel_price_column='Petrol_Price_in_Mumbai',     #Change to Petrol or Diesel
    df=ice_df,
    start_date=start_date,
    end_date=end_date
)

# Calculate costs for an electric vehicle
ev_costs = calculate_electric_vehicle_costs(
    vehicle_name="Aether Ritza Z",
    initial_vehicle_cost=155000,
    annual_maintenance_cost=8000,
    annual_insurance_cost=1200,     #Annual Insurance Cost
    other_annual_costs=1249,        #Subscriptions
    electricity_consumption_per_km=0.21,
    annual_distance=15000,
    df=ev_df,
    start_date=start_date,
    end_date=end_date,
)

visualize_cost_comparison(ice_costs, ev_costs)
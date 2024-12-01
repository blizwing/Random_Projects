import pandas as pd
import os
from tabulate import tabulate  # Add this import for better table formatting

def calculate_maintenance_cost(start_date, end_date):
    """Calculate maintenance cost based on the year of ownership"""
    total_maintenance_cost = 0
    years = end_date.year - start_date.year + 1

    for year in range(years):
        if year < 3:  # First three years
            total_maintenance_cost += 5000
        else:  # Years 4 and 5
            total_maintenance_cost += 8000

    return total_maintenance_cost

def calculate_ice_vehicle_costs(vehicle_name, initial_vehicle_cost, annual_insurance_cost,
                              other_annual_costs, fuel_efficiency, annual_distance,
                              fuel_price_column, df, start_date, end_date):
    # Calculate annual fuel consumption
    annual_fuel_consumption = annual_distance / fuel_efficiency

    # Filter the dataset for the desired date range
    filtered_df = df[(df['date_of_revision'] >= start_date) & (df['date_of_revision'] <= end_date)]

    # Calculate costs
    total_years = end_date.year - start_date.year + 1
    avg_fuel_price = filtered_df[fuel_price_column].mean()
    total_fuel_cost = avg_fuel_price * annual_fuel_consumption * total_years
    total_maintenance_cost = calculate_maintenance_cost(start_date, end_date)
    total_insurance_cost = annual_insurance_cost * total_years
    total_other_costs = other_annual_costs * total_years
    total_cost = (initial_vehicle_cost + total_fuel_cost +
                  total_maintenance_cost + total_insurance_cost +
                  total_other_costs)

    # Prepare detailed breakdown
    print("\n" + "="*50)
    print(f"🚗 Cost Analysis for {vehicle_name}")
    print(f"📅 Period: {start_date.date()} to {end_date.date()}")
    print("="*50)

    # Create a detailed breakdown table
    cost_breakdown = [
        ["Initial Vehicle Cost", f"{initial_vehicle_cost:,.2f}"],
        ["Fuel Costs", f"{total_fuel_cost:,.2f}"],
        ["Maintenance Costs", f"{total_maintenance_cost:,.2f}"],
        ["Insurance Costs", f"{total_insurance_cost:,.2f}"],
        ["Other Costs", f"{total_other_costs:,.2f}"],
        ["━"*20, "━"*15],
        ["Total Cost", f"{total_cost:,.2f}"]
    ]

    # Print the table
    print(tabulate(cost_breakdown, headers=["Cost Component", "Amount (INR)"],
                  tablefmt="pretty", colalign=("left", "right")))

    # Print additional details
    print("\n📊 Additional Information:")
    print(f"• Annual Distance: {annual_distance:,} km")
    print(f"• Fuel Efficiency: {fuel_efficiency:.1f} km/L")
    print(f"• Average Fuel Price: ₹{avg_fuel_price:.2f}/L")
    print(f"• Ownership Period: {total_years} years")
    print("="*50)

    return {
        'initial_cost': initial_vehicle_cost,
        'fuel_cost': total_fuel_cost,
        'maintenance_cost': total_maintenance_cost,
        'insurance_cost': total_insurance_cost,
        'other_costs': total_other_costs,
        'total_cost': total_cost
    }

def load_ice_data():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                            'data', 'fuel_prices_metro_cities.csv')
    df = pd.read_csv(file_path)
    df['date_of_revision'] = pd.to_datetime(df['date_of_revision'], format='%d-%b-%y')
    return df

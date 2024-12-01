import pandas as pd
import os
from tabulate import tabulate

def calculate_electric_vehicle_costs(vehicle_name, initial_vehicle_cost, annual_maintenance_cost, annual_insurance_cost,
                                   other_annual_costs, electricity_consumption_per_km, annual_distance, df,
                                   start_date, end_date):
    # Calculate annual electricity consumption
    annual_electricity_consumption = annual_distance * electricity_consumption_per_km

    # Adjust the start and end years for fiscal year calculation
    fiscal_start_year = start_date.year if start_date.month >= 4 else start_date.year - 1
    fiscal_end_year = end_date.year if end_date.month >= 4 else end_date.year - 1

    # Filter the dataset for the desired fiscal year range
    filtered_df = df[(df['Year'] >= fiscal_start_year) & (df['Year'] <= fiscal_end_year)]

    # Calculate the average electricity price over the period
    average_electricity_price = filtered_df['Domestic'].mean()

    # Calculate costs
    total_years = fiscal_end_year - fiscal_start_year + 1
    total_electricity_cost = average_electricity_price * annual_electricity_consumption * total_years
    total_maintenance_cost = annual_maintenance_cost * total_years
    total_insurance_cost = annual_insurance_cost * total_years
    total_other_costs = other_annual_costs * total_years
    total_cost = (initial_vehicle_cost + total_electricity_cost +
                  total_maintenance_cost + total_insurance_cost +
                  total_other_costs)

    # Print formatted output
    print("\n" + "="*50)
    print(f"🚗 Cost Analysis for {vehicle_name}")
    print(f"📅 Period: {start_date.date()} to {end_date.date()}")
    print("="*50)

    # Create cost breakdown table
    cost_breakdown = [
        ["Initial Vehicle Cost", f"{initial_vehicle_cost:,.2f}"],
        ["Electricity Costs", f"{total_electricity_cost:,.2f}"],
        ["Maintenance Costs", f"{total_maintenance_cost:,.2f}"],
        ["Insurance Costs", f"{total_insurance_cost:,.2f}"],
        ["Other Costs", f"{total_other_costs:,.2f}"],
        ["━"*20, "━"*15],
        ["Total Cost", f"{total_cost:,.2f}"]
    ]

    # Print the table
    print(tabulate(cost_breakdown, headers=["Cost Component", "Amount (INR)"],
                  tablefmt="pretty", colalign=("left", "right")))

    # Print additional information
    print("\n📊 Additional Information:")
    print(f"• Annual Distance: {annual_distance:,} km")
    print(f"• Energy Consumption: {electricity_consumption_per_km:.3f} kWh/km")
    print(f"• Average Electricity Price: ₹{average_electricity_price:.2f}/kWh")
    print(f"• Ownership Period: {total_years} years")
    print("="*50)

    return {
        'initial_cost': initial_vehicle_cost,
        'electricity_cost': total_electricity_cost,
        'maintenance_cost': total_maintenance_cost,
        'insurance_cost': total_insurance_cost,
        'other_costs': total_other_costs,
        'total_cost': total_cost
    }

def load_ev_data():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data',
                            'electricity_prices_2015-2024.csv')
    df = pd.read_csv(file_path)
    df['Year'] = df['Year'].apply(lambda x: int(x.split('-')[0]))
    return df

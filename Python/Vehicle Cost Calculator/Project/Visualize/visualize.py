import matplotlib.pyplot as plt
import numpy as np


def visualize_cost_comparison(ice_costs, ev_costs):
    # Set style
    plt.style.use('seaborn-v0_8')

    # Create figure with multiple subplots
    fig = plt.figure(figsize=(15, 10))

    # 1. Bar Chart Comparison
    ax1 = fig.add_subplot(221)
    categories = ['Initial Cost', 'Fuel/Electricity', 'Maintenance', 'Insurance', 'Other', 'Total']
    ice_values = [ice_costs['initial_cost'], ice_costs['fuel_cost'], ice_costs['maintenance_cost'],
                  ice_costs['insurance_cost'], ice_costs['other_costs'], ice_costs['total_cost']]
    ev_values = [ev_costs['initial_cost'], ev_costs['electricity_cost'], ev_costs['maintenance_cost'],
                 ev_costs['insurance_cost'], ev_costs['other_costs'], ev_costs['total_cost']]

    x = np.arange(len(categories))
    width = 0.35

    ax1.bar(x - width / 2, ice_values, width, label='ICE Vehicle', color='lightcoral')
    ax1.bar(x + width / 2, ev_values, width, label='Electric Vehicle', color='lightgreen')

    ax1.set_title('Cost Comparison: ICE vs Electric')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, rotation=45)
    ax1.legend()

    # 2. Pie Chart - ICE Cost Breakdown
    ax2 = fig.add_subplot(223)
    ice_labels = ['Initial', 'Fuel', 'Maintenance', 'Insurance', 'Other']
    ice_sizes = ice_values[:-1]  # Exclude total
    ax2.pie(ice_sizes, labels=ice_labels, autopct='%1.1f%%', startangle=90)
    ax2.set_title('ICE Vehicle Cost Breakdown')

    # 3. Pie Chart - EV Cost Breakdown
    ax3 = fig.add_subplot(224)
    ev_labels = ['Initial', 'Electricity', 'Maintenance', 'Insurance', 'Other']
    ev_sizes = ev_values[:-1]  # Exclude total
    ax3.pie(ev_sizes, labels=ev_labels, autopct='%1.1f%%', startangle=90)
    ax3.set_title('Electric Vehicle Cost Breakdown')

    # 4. Line Plot - Cumulative Costs
    ax4 = fig.add_subplot(222)
    years = range(6)  # 5-year period
    ice_cumulative = [ice_costs['initial_cost']]
    ev_cumulative = [ev_costs['initial_cost']]

    for year in years[1:]:
        ice_yearly = (ice_costs['fuel_cost'] + ice_costs['maintenance_cost'] +
                      ice_costs['insurance_cost'] + ice_costs['other_costs']) / 5
        ev_yearly = (ev_costs['electricity_cost'] + ev_costs['maintenance_cost'] +
                     ev_costs['insurance_cost'] + ev_costs['other_costs']) / 5
        ice_cumulative.append(ice_cumulative[-1] + ice_yearly)
        ev_cumulative.append(ev_cumulative[-1] + ev_yearly)

    ax4.plot(years, ice_cumulative, marker='o', label='ICE Vehicle', color='lightcoral')
    ax4.plot(years, ev_cumulative, marker='o', label='Electric Vehicle', color='lightgreen')
    ax4.set_title('Cumulative Costs Over Time')
    ax4.set_xlabel('Years')
    ax4.set_ylabel('Cost (INR)')
    ax4.legend()

    plt.tight_layout()
    plt.show()

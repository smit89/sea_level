import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', alpha=0.5)


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    line_of_best_fit = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, line_of_best_fit, 'r', label='Line of Best Fit (All Data)')


    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_data['Year'], 
        recent_data['CSIRO Adjusted Sea Level']
    )
    years_recent_extended = range(2000, 2051)
    line_of_best_fit_recent = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, line_of_best_fit_recent, 'g', label='Line of Best Fit (Since 2000)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
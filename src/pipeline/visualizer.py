from src.pipeline.data_loader import load_data, get_dataset_info
from src.logger.logger import logger

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

from src.utils.constants import OUTPUTS_DIR

def save_top_countries_confirmed_cases_plot(confirmed_cases_df):
    """
    Takes in the raw dataframe of confirmed cases and cleans it as needed 
    and saves the plot of top 5 countries in output directory

    Parameters:
        confirmed_cases_df: df (Pandas DataFrame) of confirmed cases
    
    Returns:
        None
    """
    try:
        # Group the countries based on Country/Region and sum their cases and drop unnecessary data
        grouped_countries = confirmed_cases_df.groupby('Country/Region').sum()
        grouped_countries.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)

        # Sum all of the confirmed cases and pick 5 countries with most cases of all time
        series_of_sums = grouped_countries.select_dtypes(include='number').sum(axis=1)
        top_5_countries_index = series_of_sums.nlargest(5).index
        top_5_countries = grouped_countries.loc[top_5_countries_index]

        # Convert the columns to proper datetime format
        columns_datetime = pd.to_datetime(top_5_countries.columns, format='%m/%d/%y')
        
        # Customize and plot overtime, and save the figure
        plt.figure(figsize=(14, 6))

        for index, row in top_5_countries.iterrows():
            plt.plot(columns_datetime, row.values, label=f"{index}")
        
        plt.title('Confirmed Cases in Top 5 Countries')
        plt.xlabel('Date')
        plt.ylabel('Confirmed Cases')
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        plt.legend()
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.14)
        plt.xticks(rotation=15)
        plt.grid(True)
        plt.savefig(OUTPUTS_DIR / 'top_five_countries_cases_overtime.svg')
    except Exception as err:
        logger.error(f"An unexpected error occured: {err}")

def save_china_countries_confirmed_cases_plot(confirmed_cases_df):
    """
    Takes in the raw dataframe of confirmed cases and cleans it as needed 
    and saves the plot of china's confirmed cases overtime

    Parameters:
        confirmed_cases_df: df (Pandas DataFrame) of confirmed cases
    
    Returns:
        None
    """
    try:
        # Filter out all of the china regions and group them up and sum their cases
        china_confirmed_cases = confirmed_cases_df[confirmed_cases_df['Country/Region'] == 'China']
        grouped_china_confirmed_cases = china_confirmed_cases.groupby('Country/Region').sum()

        # Remove unnecessary columns
        grouped_china_confirmed_cases.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)

        # Convert the columns to proper datetime format
        columns_datetime = pd.to_datetime(grouped_china_confirmed_cases.columns, format='%m/%d/%y')
        
        # Customize and plot overtime, and save the figure
        plt.figure(figsize=(14, 6))
        plt.plot(columns_datetime, grouped_china_confirmed_cases.iloc[0], label=f"China")
        plt.title('Confirmed Cases in China Overtime')
        plt.xlabel('Date')
        plt.ylabel('Confirmed Cases')
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        plt.legend()
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.14)
        plt.xticks(rotation=15)
        plt.grid(True)
        plt.savefig(OUTPUTS_DIR / 'china_confirmed_cases_overtime.svg')
    except Exception as err:
        logger.error(f"An unexpected error occured: {err}")
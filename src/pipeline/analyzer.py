import pandas as pd

from src.logger.logger import logger

def peak_daily_cases_by_country(confirmed_cases_cleaned, countries):
    """
    Takes in cleaned confirmed cases dataframe and a list of countries and returns
    a dataframe of their highest single day surge and the date

    Parameters:
        confirmed_cases_cleaned: Cleaned DataFrame of confirmed cases
        countries: A list of country names
    
        Returns:
            peak_daily_cases: A DataFrame containing peak daily cases of the countries
    """
    try:
        filtered_countries = confirmed_cases_cleaned[confirmed_cases_cleaned['Country/Region'].isin(countries)]
        filtered_countries = filtered_countries.groupby('Country/Region').sum()
        filtered_countries = filtered_countries.drop(columns=['Province/State', 'Lat', 'Long'])
        max_values = filtered_countries.max(axis=1)
        max_value_columns = filtered_countries.idxmax(axis=1)
        
        peak_daily_cases = pd.DataFrame({'Max Confirmed Cases Per Day': max_values, 'Date': max_value_columns})
        peak_daily_cases.sort_values(by='Max Confirmed Cases Per Day', ascending=False, inplace=True)

        return peak_daily_cases
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

def compare_recovery_rate(recovered_cleaned, confirmed_cases_cleaned, country_one, country_two, date):
    """
    Takes in cleaned recovered and confirmed cases dataframe, names of two countries
    and a date uptil which we want the recovery date comaprison, and returns a 
    dataframe of with compared recovery rate

    Parameters:
        recovered_cleaned: Cleaned DataFrame of recovered cases
        confirmed_cases_cleaned: Cleaned DataFrame of confirmed cases
        country_one: Name of first country
        country_two: Name of the second country
    
        Returns:
            recovery_rates: A DataFrame containing comparison of recovery rates
    """
    try:
        filtered_recovered = recovered_cleaned[recovered_cleaned['Country/Region'].isin([country_one, country_two])]
        filtered_recovered = filtered_recovered.drop(columns=['Province/State', 'Lat', 'Long'])
        filtered_recovered = filtered_recovered.groupby('Country/Region').sum()

        filtered_confirmed = confirmed_cases_cleaned[confirmed_cases_cleaned['Country/Region'].isin([country_one, country_two])]
        filtered_confirmed = filtered_confirmed.drop(columns=['Province/State', 'Lat', 'Long'])
        filtered_confirmed = filtered_confirmed.groupby('Country/Region').sum()

        recovery_rates = ((filtered_recovered / filtered_confirmed) * 100).fillna(0.0).round(2)
        recovery_rates = recovery_rates.loc[:, :date]
        
        return recovery_rates
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

def distribution_of_death_rates(deaths_cleaned, confirmed_cases_cleaned, country, date):
    """
    Takes in cleaned deaths and confirmed cases dataframe, and name of a country
    of which we want distribution of deaths, and returns a dataframe of with 
    death rate distribution accross its provinces

    Parameters:
        deaths_cleaned: Cleaned DataFrame of death cases
        confirmed_cases_cleaned: Cleaned DataFrame of confirmed cases
        country: Name of a country
        date: Date as of which you want the distribution
    
        Returns:
            death_rates: A DataFrame containing comparison of death rates at specific date
    """
    try:
        filtered_deaths = deaths_cleaned[deaths_cleaned['Country/Region'] == country]
        filtered_deaths = filtered_deaths.drop(columns=['Lat', 'Long', 'Country/Region'])
        filtered_deaths = filtered_deaths.groupby('Province/State').sum()

        filtered_confirmed = confirmed_cases_cleaned[deaths_cleaned['Country/Region'] == country]
        filtered_confirmed = filtered_confirmed.drop(columns=['Lat', 'Long', 'Country/Region'])
        filtered_confirmed = filtered_confirmed.groupby('Province/State').sum()

        death_rates = ((filtered_deaths / filtered_confirmed) * 100).fillna(0.0).round(2)
        death_rates = death_rates[[date]]
        
        return death_rates
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

def get_total_deaths_per_country(deaths_cleaned):
    """
    Takes in cleaned deaths dataframe, and returns a dataframe with 
    total deaths per country

    Parameters:
        deaths_cleaned: Cleaned DataFrame of death cases
    
    Returns:
        total_deaths_df: A DataFrame containing total deaths per country
    """
    try:
        # Drop unnecessary columns
        deaths_cleaned = deaths_cleaned.drop(columns=['Lat', 'Long', 'Province/State'])
        
        # Add total deaths column
        total_deaths = deaths_cleaned.sum(axis=1, numeric_only=True)
        total_deaths_df = deaths_cleaned.assign(**{"Total Deaths": total_deaths}).copy()
        
        return total_deaths_df
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

def get_highest_avg_daily_deaths(deaths_cleaned, number_of_countries):
    """
    Takes in cleaned deaths dataframe, and returns a dataframe of top 5 countries with 
    highest average daily deaths

    Parameters:
        deaths_cleaned: Cleaned DataFrame of death cases
        number_of_countries: Integer number of countries you want
    
    Returns:
        highest_deaths: A DataFrame with highest average daily deaths countries
    """
    try:
        # Drop unnecessary columns
        deaths_cleaned = deaths_cleaned.drop(columns=['Lat', 'Long', 'Province/State'])

        deaths_cleaned = deaths_cleaned.groupby('Country/Region').sum().reset_index()
        
        # Add total deaths column
        average_daily_deaths = deaths_cleaned.mean(axis=1, numeric_only=True).round(2)
        highest_deaths = deaths_cleaned.assign(**{"Average Daily Deaths": average_daily_deaths}).copy()

        highest_deaths = highest_deaths.sort_values("Average Daily Deaths", ascending=False).head(number_of_countries)
        
        return highest_deaths
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

def total_deaths_overtime(deaths_cleaned, country_name):
    """
    Takes in cleaned deaths dataframe, and returns a dataframe of deaths
    overtime.

    Parameters:
        deaths_cleaned: Cleaned DataFrame of death cases
        country_name: Name of the country you want the overtime deaths for
    
    Returns:
        overtime_deaths: A DataFrame with overtime deaths of the specified country
    """
    try:
        overtime_deaths = deaths_cleaned[deaths_cleaned['Country/Region'] == country_name]

        # Drop unnecessary columns
        overtime_deaths = overtime_deaths.groupby('Country/Region').sum()
        overtime_deaths = overtime_deaths.drop(columns=['Lat', 'Long', 'Province/State'])

        overtime_deaths = overtime_deaths.T
        overtime_deaths.index = pd.to_datetime(overtime_deaths.index, format='%m/%d/%y')
        overtime_deaths.columns = ['Total_Deaths']
        
        return overtime_deaths
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

def merged_monthly_sum(merged_df):
    """
    Takes in merged dataframe of confirmed, deaths, and recovered cases, and returns
    a dataframe containing monthly sum of each dataset type.

    Parameters:
        merged_df: Merged DataFrame of confirmed, deaths, recovered cases in long format
    
    Returns:
        monthly_sum: A DataFrame with merged monthly sums
    """
    try:
        merged_df.sort_values(by=['Country/Region', 'Date'], inplace=True)

        merged_df['New Confirmed'] = merged_df.groupby('Country/Region')['Confirmed Cases'].diff()
        merged_df['New Deaths'] = merged_df.groupby('Country/Region')['Deaths'].diff()
        merged_df['New Recovered'] = merged_df.groupby('Country/Region')['Recovered'].diff()

        merged_df['Month'] = merged_df['Date'].dt.to_period('M')
        
        monthly_sum = merged_df.groupby(['Country/Region', 'Month'])[
            ['New Confirmed', 'New Deaths', 'New Recovered']
        ].sum().reset_index()

        return monthly_sum
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)
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
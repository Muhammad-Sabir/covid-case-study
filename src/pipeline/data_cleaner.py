import pandas as pd

from src.logger.logger import logger

def rename_column_first_row(raw_df):
    """
    Takes in raw dataframe and renames its column to its first row

    Parameters:
        raw_df: Raw DataFrame
    
    Returns:
        renamed_df: Renamed column DataFrame
    """
    # Rename the column to the first row and remove first row
    renamed_df = raw_df.rename(columns=raw_df.iloc[0])
    renamed_df = renamed_df.drop(renamed_df.index[0]).reset_index(drop=True)

    return renamed_df

def replace_empty_province(raw_df):
    """
    Takes in raw dataframe and replace every empty province entry 
    with 'All Provinces'

    Parameters:
        raw_df: Raw DataFrame
    
    Returns:
        renamed_df: DataFrame with empty provinces replaced with 'All Provinces'
    """
    return raw_df.fillna({'Province/State': 'All Provinces'})

def handle_deaths_missing_data(deaths_raw):
    """
    Takes in raw dataframe of the deaths and handle the missing values
    in the columns, deletes lat/long non-significant rows and ffill 
    the deaths from left to right, and whereever province is empty,
    write 'All Provinces'

    Parameters:
        deaths_raw: Raw DataFrame of the deaths csv
    
    Returns:
        deaths_cleaned: Cleaned DataFrame of the deaths csv
    """
    try:
        deaths_renamed = rename_column_first_row(deaths_raw)
        deaths_cleaned = replace_empty_province(deaths_renamed)
        
        # Drop rows where Lat or Long are NaN, these rows are non-significant
        deaths_cleaned.dropna(inplace=True, subset=['Lat', 'Long'])

        # Fill missing death values left to right
        deaths_cleaned = deaths_cleaned.ffill(axis=1)

        return deaths_cleaned
    except Exception as err:
        logger.error(f"An unexpected error occurred {str(err)}", exc_info=True)

def handle_confirmed_cases_missing_data(confirmed_cases_raw):
    """
    Takes in raw dataframe of the confirmed_cases and handle the missing values
    in the columns, deletes lat/long non-significant rows and whereever province
    is empty, write 'All Provinces'

    Parameters:
        confirmed_cases_raw: Raw DataFrame of the deaths csv
    
    Returns:
        confirmed_cases_cleaned: Cleaned DataFrame of the confirmed_cases csv
    """
    try:
        confirmed_cases_raw = replace_empty_province(confirmed_cases_raw)
        
        # Drop rows where Lat or Long are NaN, these rows are non-significant
        confirmed_cases_cleaned = confirmed_cases_raw.dropna(subset=['Lat', 'Long'])

        return confirmed_cases_cleaned
    except Exception as err:
        logger.error(f"An unexpected error occurred {str(err)}", exc_info=True)

def handle_recovered_missing_data(recovered_raw):
    """
    Takes in raw dataframe of the recovered cases and handle the missing
    values in the columns, deletes lat/long non-significant rows and ffill 
    the cases from left to right, and whereever province is empty,
    write 'All Provinces'

    Parameters:
        recovered_raw: Raw DataFrame of the recovered csv
    
    Returns:
        recovered_cleaned: Cleaned DataFrame of the recovered cases csv
    """
    try:
        recovered_renamed = rename_column_first_row(recovered_raw)
        recovered_cleaned = replace_empty_province(recovered_renamed)
        
        # Drop rows where Lat or Long are NaN, these rows are non-significant
        recovered_cleaned.dropna(inplace=True, subset=['Lat', 'Long'])

        # Fill missing death values left to right
        recovered_cleaned = recovered_cleaned.ffill(axis=1)

        return recovered_cleaned
    except Exception as err:
        logger.error(f"An unexpected error occurred {str(err)}", exc_info=True)

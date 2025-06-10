import pandas as pd

from src.logger.logger import logger
from src.utils.enums import DatasetType


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
    return raw_df.fillna({"Province/State": "All Provinces"})


def drop_non_existing_provinces(raw_df):
    """
    Takes in raw dataframe and drop every row which has a province mentioned
    which doesnt really exist

    Parameters:
        raw_df: Raw DataFrame

    Returns:
        cleaned_df: DataFrame with the rows with non existing provinces dropped
    """
    return raw_df[
        ~raw_df["Province/State"].isin(["Diamond Princess", "Grand Princess"])
    ]


def fix_datatypes(raw_df):
    """
    Takes in raw dataframe and make sure that each column has proper data types

    Parameters:
        raw_df: Raw DataFrame

    Returns:
        datatype_fixed_df: DataFrame with properly updated datatypes
    """
    datatype_fixed_df = raw_df.copy()
    datatype_fixed_df["Province/State"] = datatype_fixed_df["Province/State"].astype(
        "string"
    )
    datatype_fixed_df["Country/Region"] = datatype_fixed_df["Country/Region"].astype(
        "string"
    )
    datatype_fixed_df["Lat"] = datatype_fixed_df["Lat"].astype(float)
    datatype_fixed_df["Long"] = datatype_fixed_df["Long"].astype(float)
    date_columns = datatype_fixed_df.loc[:, "1/22/20":"5/29/21"].columns
    datatype_fixed_df[date_columns] = datatype_fixed_df[date_columns].astype(int)

    return datatype_fixed_df


def handle_missing_data(raw_df, data_type):
    """
    Takes in raw dataframe and handle the missing values in the columns,
    deletes lat/long non-significant rows and ffill from left to right,
    and whereever province is empty, write 'All Provinces'

    Parameters:
        raw_df: Raw DataFrame of the deaths csv
        data_type: DatasetType enum value

    Returns:
        cleaned_df: Cleaned DataFrame
    """
    try:
        if data_type in [DatasetType.DEATHS, DatasetType.RECOVERED]:
            raw_df = rename_column_first_row(raw_df)

        cleaned_df = replace_empty_province(raw_df)
        cleaned_df = drop_non_existing_provinces(cleaned_df)

        # Drop rows where Lat or Long are NaN, these rows are non-significant
        cleaned_df.dropna(inplace=True, subset=["Lat", "Long"])

        # Fill missing values left to right
        cleaned_df = cleaned_df.ffill(axis=1)

        cleaned_df = drop_non_existing_provinces(cleaned_df)
        return fix_datatypes(cleaned_df)
    except Exception as err:
        logger.error(f"An unexpected error occurred {str(err)}", exc_info=True)


def transform_from_wide_to_long(wide_df, data_type):
    """
    Takes in any clean dataframe and converts the dataset from wide to
    long format

    Parameters:
        wide_df: DataFrame in wide format
        data_type: DatasetType enum value

    Returns:
        long_df: DataFrame in long format
    """
    try:
        if data_type == DatasetType.DEATHS:
            value_column_title = "Deaths"
        elif data_type == DatasetType.CONFIRMED_CASES:
            value_column_title = "Confirmed Cases"
        elif data_type == DatasetType.RECOVERED:
            value_column_title = "Recovered"

        long_df = pd.melt(
            wide_df,
            id_vars=["Province/State", "Country/Region", "Lat", "Long"],
            var_name="Date",
            value_name=value_column_title,
        )
        long_df["Date"] = pd.to_datetime(long_df["Date"], format="%m/%d/%y")

        return long_df
    except Exception as err:
        logger.error(f"An unexpected error occurred {str(err)}", exc_info=True)


def merge_datasets(deaths_cleaned, confirmed_cases_cleaned, recovered_cleaned):
    """
    Takes in any clean dataframes of deaths, confirmed, and recovered cases
    and converts the datasets from wide to long format and merge them

    Parameters:
        deaths_cleaned: Deaths DataFrame in wide format
        confirmed_cases_cleaned: Confirmed Cases DataFrame in wide format
        recovered_cleaned: Recovered Cases DataFrame in wide format

    Returns:
        merged_df: DataFrame built by merging them
    """
    try:
        confirmed_cases_long = transform_from_wide_to_long(
            confirmed_cases_cleaned, DatasetType.CONFIRMED_CASES
        )
        deaths_long = transform_from_wide_to_long(deaths_cleaned, DatasetType.DEATHS)
        recovered_long = transform_from_wide_to_long(
            recovered_cleaned, DatasetType.RECOVERED
        )

        confirmed_cases_grouped = (
            confirmed_cases_long.groupby(["Country/Region", "Date"])["Confirmed Cases"]
            .sum()
            .reset_index()
        )
        deaths_grouped = (
            deaths_long.groupby(["Country/Region", "Date"])["Deaths"]
            .sum()
            .reset_index()
        )
        recovered_grouped = (
            recovered_long.groupby(["Country/Region", "Date"])["Recovered"]
            .sum()
            .reset_index()
        )

        merged_df = confirmed_cases_grouped.merge(
            deaths_grouped, on=["Country/Region", "Date"]
        )
        merged_df = merged_df.merge(recovered_grouped, on=["Country/Region", "Date"])

        return merged_df
    except Exception as err:
        logger.error(f"An unexpected error occurred {str(err)}", exc_info=True)

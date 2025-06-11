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
        filtered_countries = confirmed_cases_cleaned[
            confirmed_cases_cleaned["Country/Region"].isin(countries)
        ]
        filtered_countries = filtered_countries.groupby("Country/Region").sum()
        filtered_countries = filtered_countries.drop(
            columns=["Province/State", "Lat", "Long"]
        )
        max_values = filtered_countries.max(axis=1)
        max_value_columns = filtered_countries.idxmax(axis=1)

        peak_daily_cases = pd.DataFrame(
            {"Max Confirmed Cases Per Day": max_values, "Date": max_value_columns}
        )
        peak_daily_cases.sort_values(
            by="Max Confirmed Cases Per Day", ascending=False, inplace=True
        )

        return peak_daily_cases
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def compare_recovery_rate(
    recovered_cleaned, confirmed_cases_cleaned, country_one, country_two, date
):
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
        filtered_recovered = recovered_cleaned[
            recovered_cleaned["Country/Region"].isin([country_one, country_two])
        ]
        filtered_recovered = filtered_recovered.drop(
            columns=["Province/State", "Lat", "Long"]
        )
        filtered_recovered = filtered_recovered.groupby("Country/Region").sum()

        filtered_confirmed = confirmed_cases_cleaned[
            confirmed_cases_cleaned["Country/Region"].isin([country_one, country_two])
        ]
        filtered_confirmed = filtered_confirmed.drop(
            columns=["Province/State", "Lat", "Long"]
        )
        filtered_confirmed = filtered_confirmed.groupby("Country/Region").sum()

        recovery_rates = (
            ((filtered_recovered / filtered_confirmed) * 100).fillna(0.0).round(2)
        )
        recovery_rates = recovery_rates.loc[:, date]

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
        filtered_deaths = deaths_cleaned[deaths_cleaned["Country/Region"] == country]
        filtered_deaths = filtered_deaths.drop(
            columns=["Lat", "Long", "Country/Region"]
        )
        filtered_deaths = filtered_deaths.groupby("Province/State").sum()

        filtered_confirmed = confirmed_cases_cleaned[
            deaths_cleaned["Country/Region"] == country
        ]
        filtered_confirmed = filtered_confirmed.drop(
            columns=["Lat", "Long", "Country/Region"]
        )
        filtered_confirmed = filtered_confirmed.groupby("Province/State").sum()

        death_rates = (
            ((filtered_deaths / filtered_confirmed) * 100).fillna(0.0).round(2)
        )
        death_rates = death_rates[[date]]
        death_rates.columns = ["Death Rates"]

        return death_rates
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def get_extreme_death_rates(death_rates):
    """
    Takes in death rates dataframe, and returns a dataframe of with
    provinces and death rate of the highest and lowest death rates

    Parameters:
        death_rates: A DataFrame containing comparison of death rates at specific date

    Returns:
        extremes_df: A DataFrame containing rows for the highest and lowest death rates
    """
    try:
        if death_rates.empty:
            return pd.DataFrame(columns=["Province/State", "Death Rates"])

        max_row = death_rates.loc[[death_rates["Death Rates"].idxmax()]]
        min_row = death_rates.loc[[death_rates["Death Rates"].idxmin()]]

        extremes_df = pd.concat([max_row, min_row]).drop_duplicates()

        return extremes_df
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def get_total_deaths_per_country(long_deaths_df):
    """
    Takes in cleaned deaths dataframe in long format, and returns a dataframe with
    total deaths per country

    Parameters:
        long_deaths_df: Cleaned DataFrame of death cases in long format

    Returns:
        total_deaths_df: A DataFrame containing total deaths per country
    """
    try:
        latest_date = long_deaths_df["Date"].max()

        total_deaths_df = long_deaths_df[long_deaths_df["Date"] == latest_date]
        total_deaths_df = total_deaths_df.drop(
            columns=["Lat", "Long", "Province/State"]
        )
        total_deaths_df = (
            total_deaths_df.groupby("Country/Region")
            .sum(numeric_only=True)
            .sort_values(by="Deaths", ascending=False)
            .reset_index()
        )

        return total_deaths_df
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def get_highest_avg_daily_deaths(long_deaths_df, number_of_countries=5):
    """
    Takes in cleaned deaths dataframe, and returns a dataframe of top 5 countries with
    highest average daily deaths

    Parameters:
        long_deaths_df: Cleaned DataFrame of death cases in long format
        number_of_countries: Integer number of countries you want

    Returns:
        average_daily_deaths: A DataFrame with highest average daily deaths countries
    """
    try:
        long_deaths_df = long_deaths_df.drop(columns=["Lat", "Long", "Province/State"])
        long_deaths_df = long_deaths_df.sort_values(["Country/Region", "Date"])
        long_deaths_df["Average Daily Deaths"] = (
            long_deaths_df.groupby("Country/Region")["Deaths"].diff().fillna(0.0)
        )

        average_daily_deaths = (
            long_deaths_df.groupby("Country/Region")["Average Daily Deaths"]
            .mean()
            .sort_values(ascending=False)
            .head(number_of_countries)
        )

        return average_daily_deaths
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def total_deaths_overtime(long_deaths_df, country_name):
    """
    Takes in cleaned deaths dataframe, and returns a dataframe of deaths
    overtime.

    Parameters:
        long_deaths_df: Cleaned DataFrame of death cases in long format
        country_name: Name of the country you want the overtime deaths for

    Returns:
        overtime_deaths: A DataFrame with overtime deaths of the specified country
    """
    try:
        overtime_deaths = long_deaths_df[
            long_deaths_df["Country/Region"] == country_name
        ]

        # Drop unnecessary columns
        overtime_deaths = overtime_deaths.sort_values(["Date"]).reset_index()
        overtime_deaths = overtime_deaths.drop(
            columns=["Lat", "Long", "Province/State", "Country/Region", "index"]
        )

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
        merged_df.sort_values(by=["Country/Region", "Date"], inplace=True)

        merged_df["Monthly Confirmed Cases"] = merged_df.groupby("Country/Region")[
            "Confirmed Cases"
        ].diff()
        merged_df["Monthly Deaths"] = merged_df.groupby("Country/Region")[
            "Deaths"
        ].diff()
        merged_df["Monthly Recovered"] = merged_df.groupby("Country/Region")[
            "Recovered"
        ].diff()

        merged_df["Month"] = merged_df["Date"].dt.to_period("M")

        monthly_sum = (
            merged_df.groupby(["Country/Region", "Month"])[
                ["Monthly Confirmed Cases", "Monthly Deaths", "Monthly Recovered"]
            ]
            .sum()
            .reset_index()
        )

        return monthly_sum
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def highest_avg_death_rates_2020(merged_df, number_of_countries=3):
    """
    Takes in merged dataframe of confirmed, deaths, and recovered cases, and number_of_countries
    and returns a dataframe death rates of top n countries.

    Parameters:
        merged_df: Merged DataFrame of confirmed, deaths, recovered cases in long format
        number_of_countries: Number of countries of which you want to see death rates

    Returns:
        death_rates: A DataFrame with death rates of n countries
    """
    try:
        df_2020 = merged_df[
            (merged_df["Date"] >= "2020-01-01") & (merged_df["Date"] <= "2020-12-31")
        ]

        death_rates = (
            df_2020.sort_values("Date").groupby("Country/Region").last().reset_index()
        )

        death_rates["Death Rate"] = (
            (death_rates["Deaths"] / death_rates["Confirmed Cases"])
            .fillna(0.0)
            .round(2)
        )
        death_rates = death_rates.sort_values("Death Rate", ascending=False).head(
            number_of_countries
        )

        return death_rates
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def recovery_death_ratio(merged_df, country_name):
    """
    Takes in merged dataframe of confirmed, deaths, and recovered cases, and name of the country
    and returns a recovery death ratio of that country.

    Parameters:
        merged_df: Merged DataFrame of confirmed, deaths, recovered cases in long format
        country_name: Name of country of which you want to see recovery death ratio

    Returns:
        recovery_death_ratio: Recovery death ratio of specified country
    """
    try:
        country_df = merged_df[merged_df["Country/Region"] == country_name]

        latest_data = country_df.sort_values("Date").iloc[-1]

        total_recovered = latest_data["Recovered"]
        total_deaths = latest_data["Deaths"]

        recovery_death_ratio = (
            total_recovered / total_deaths if total_deaths > 0 else None
        )

        return (
            recovery_death_ratio.round(2)
            if isinstance(recovery_death_ratio, float)
            else recovery_death_ratio
        )
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)


def highest_recovery_confirmed_ratio(merged_df, country_name):
    """
    Takes in merged dataframe of confirmed, deaths, and recovered cases, and name of the country
    and returns a recovery confirmed cases ratio of that country.

    Parameters:
        merged_df: Merged DataFrame of confirmed, deaths, recovered cases in long format
        country_name: Name of country of which you want to see recovery confirm cases

    Returns:
        recovery_confirm_ratio: Recovery confirm cases ratio of specified country
    """
    try:
        country_df = merged_df[merged_df["Country/Region"] == country_name]

        date_filtered = country_df[
            (country_df["Date"] >= "2020-03-01") & (country_df["Date"] <= "2021-05-31")
        ].copy()
        date_filtered["Month"] = date_filtered["Date"].dt.to_period("M")
        recovery_confirm_ratio = (
            date_filtered.sort_values("Date").groupby("Month").last().reset_index()
        )

        recovery_confirm_ratio["Recovery Ratio"] = (
            recovery_confirm_ratio["Recovered"]
            / recovery_confirm_ratio["Confirmed Cases"]
        ).round(2)
        recovery_confirm_ratio = recovery_confirm_ratio.sort_values(
            "Recovery Ratio", ascending=False
        )

        return recovery_confirm_ratio
    except Exception as err:
        logger.error(f"An unexpected error occured: {str(err)}", exc_info=True)

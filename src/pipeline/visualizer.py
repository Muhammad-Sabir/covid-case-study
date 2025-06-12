from src.logger.logger import logger

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns


def get_top_countries_confirmed_cases_plot(confirmed_cases_df):
    """
    Takes in the raw dataframe of confirmed cases and cleans it as needed
    and saves the plot of top 5 countries in output directory

    Parameters:
        confirmed_cases_df: df (Pandas DataFrame) of confirmed cases

    Returns:
        fig: matplotlib.figure.Figure
    """
    try:
        confirmed_cases_df = confirmed_cases_df.copy()

        # Group the countries based on Country/Region and sum their cases and drop unnecessary data
        confirmed_cases_df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
        grouped_countries = confirmed_cases_df.groupby("Country/Region").sum()

        # Pick 5 countries with most cases of all time
        top_5_countries_index = grouped_countries.iloc[:, -1].nlargest(5).index
        top_5_countries = grouped_countries.loc[top_5_countries_index]

        # Convert the columns to proper datetime format
        columns_datetime = pd.to_datetime(top_5_countries.columns, format="%m/%d/%y")

        # Customize and plot overtime, and save the figure
        fig, ax = plt.subplots(figsize=(14, 6))

        for index, row in top_5_countries.iterrows():
            ax.plot(columns_datetime, row.values, label=f"{index}")

        ax.set_title("Confirmed Cases in Top 5 Countries")
        ax.set_xlabel("Date")
        ax.set_ylabel("Confirmed Cases")
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
        ax.legend()
        fig.tight_layout()
        fig.subplots_adjust(bottom=0.14)
        plt.setp(ax.get_xticklabels(), rotation=15)
        ax.grid(True)

        return fig
    except Exception as err:
        logger.error(f"An unexpected error occured: {err}")


def get_china_countries_confirmed_cases_plot(confirmed_cases_df):
    """
    Takes in the raw dataframe of confirmed cases and cleans it as needed
    and saves the plot of china's confirmed cases overtime

    Parameters:
        confirmed_cases_df: df (Pandas DataFrame) of confirmed cases

    Returns:
        fig: matplotlib.figure.Figure
    """
    try:
        confirmed_cases_df = confirmed_cases_df.copy()

        # Remove unnecessary columns
        confirmed_cases_df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)

        # Filter out all of the china regions and group them up and sum their cases
        china_confirmed_cases = confirmed_cases_df[
            confirmed_cases_df["Country/Region"] == "China"
        ]
        grouped_china_confirmed_cases = china_confirmed_cases.groupby(
            "Country/Region"
        ).sum()

        # Convert the columns to proper datetime format
        columns_datetime = pd.to_datetime(
            grouped_china_confirmed_cases.columns, format="%m/%d/%y"
        )

        # Create the plot
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(columns_datetime, grouped_china_confirmed_cases.iloc[0], label="China")

        ax.set_title("Confirmed Cases in China Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Confirmed Cases")
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
        ax.legend()
        fig.tight_layout()
        fig.subplots_adjust(bottom=0.14)
        plt.setp(ax.get_xticklabels(), rotation=15)
        ax.grid(True)

        return fig
    except Exception as err:
        logger.error(f"An unexpected error occured: {err}")


def plot_peak_daily_cases(peak_daily_cases_df):
    """
    Plots a bar chart of peak daily confirmed cases per country.

    Parameters:
        peak_daily_cases_df: DataFrame with columns ["Max Confirmed Cases Per Day", "Date"]

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        x=peak_daily_cases_df.index,
        y="Max Confirmed Cases Per Day",
        data=peak_daily_cases_df,
        palette="coolwarm",
        ax=ax,
    )
    ax.set_title("Peak Daily Confirmed Cases")
    ax.set_ylabel("Number of Cases")
    ax.set_xlabel("Country")
    for i, v in enumerate(peak_daily_cases_df["Max Confirmed Cases Per Day"]):
        ax.text(
            i,
            v + max(peak_daily_cases_df["Max Confirmed Cases Per Day"]) * 0.02,
            f"{v:,}",
            ha="center",
        )

    return fig


def plot_recovery_rates(recovery_rates, date):
    """
    Plots a bar chart comparing recovery rates of two countries.

    Parameters:
        recovery_rates: Recovery rates with country names as index.
        date: Date of comparison.

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    recovery_rates.plot(kind="bar", color=["#4CAF50", "#2196F3"], ax=ax)
    ax.set_title(f"Recovery Rates as of {date}")
    ax.set_ylabel("Recovery Rate (%)")
    ax.set_ylim(0, 110)
    for i, v in enumerate(recovery_rates):
        ax.text(i, v + 2, f"{v:.2f}%", ha="center")

    return fig


def plot_death_rate_distribution(death_rate_distribution_df, country, date):
    """
    Plots horizontal bar chart of death rates across provinces.

    Parameters:
        death_rate_distribution_df: DataFrame with index as province/state and "Death Rates" column.
        country: Country name.
        date: Date of comparison.

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    df = death_rate_distribution_df.sort_values(by="Death Rates", ascending=True)
    sns.barplot(x="Death Rates", y=df.index, data=df, palette="Reds_r", ax=ax)
    ax.set_title(f"COVID-19 Death Rates in {country} as of {date}")
    ax.set_xlabel("Death Rate (%)")
    ax.set_ylabel("Province/State")
    for i, (val, name) in enumerate(zip(df["Death Rates"], df.index)):
        ax.text(val + 0.5, i, f"{val:.2f}%", va="center")

    return fig


def plot_total_deaths_per_country(total_deaths_per_country_df):
    """
    Plots total deaths per country as a horizontal bar chart.

    Parameters:
        total_deaths_per_country_df: DataFrame with total deaths per country

    Returns:
        fig: matplotlib.figure.Figure
    """
    df = total_deaths_per_country_df.sort_values(by="Deaths", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 45))
    sns.barplot(x="Deaths", y="Country/Region", data=df, ax=ax)

    ax.set_title("Total Deaths Per Country")
    ax.set_xlabel("Number of Deaths")
    ax.set_ylabel("Country")
    return fig


def plot_highest_avg_daily_deaths(avg_death_series):
    """
    Plots top countries by average daily deaths.

    Parameters:
        avg_death_series: Series of avg daily deaths

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    avg_death_series.sort_values().plot(kind="barh", color="orange", ax=ax)

    ax.set_title("Top 5 Countries by Average Daily Deaths")
    ax.set_xlabel("Average Daily Deaths")
    ax.set_ylabel("Country")

    return fig


def plot_deaths_overtime(overtime_deaths_df, country_name="US"):
    """
    Plots cumulative deaths over time for a country.

    Parameters:
        overtime_deaths_df: Dataframe with overtime deaths

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        overtime_deaths_df["Date"],
        overtime_deaths_df["Deaths"],
        color="crimson",
        linewidth=2,
    )

    ax.set_title(f"Total COVID-19 Deaths Over Time in {country_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Deaths")
    ax.tick_params(axis="x", rotation=45)

    return fig


def plot_global_monthly_sums(monthly_sum_df):
    """
    Plots global monthly sum trends of confirmed, deaths, and recovered cases.

    Parameters:
        monthly_sum_df: Dataframe with monthly sums

    Returns:
        fig: matplotlib.figure.Figure
    """
    monthly_sum_df["Month"] = monthly_sum_df["Month"].dt.to_timestamp()

    global_monthly = monthly_sum_df.groupby("Month")[
        ["Monthly Confirmed Cases", "Monthly Deaths", "Monthly Recovered"]
    ].sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    global_monthly.plot(ax=ax, marker="o")
    ax.set_title("Global Monthly COVID-19 Trends")
    ax.set_ylabel("Number of Cases")
    ax.set_xlabel("Month")
    ax.legend(title="Case Type")
    ax.grid(True)

    return fig


def plot_monthly_trends_by_country(filtered_monthly_sum_df, countries):
    """
    Plots monthly trends for confirmed, deaths, and recovered for given countries.

    Parameters:
        filtered_monthly_sum_df: Dataframe with monthly sums
        countries: List of countries of which data is available

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

    case_types = {
        "Monthly Confirmed Cases": "blue",
        "Monthly Deaths": "red",
        "Monthly Recovered": "green",
    }

    for i, (case_type, color) in enumerate(case_types.items()):
        ax = axes[i]
        for country in countries:
            country_df = filtered_monthly_sum_df[
                filtered_monthly_sum_df["Country/Region"] == country
            ]
            ax.plot(
                country_df["Month"], country_df[case_type], label=country, marker="o"
            )

        ax.set_title(case_type.replace("Monthly ", "") + " per Month")
        ax.set_ylabel("Cases")
        ax.legend()
        ax.grid(True)

    axes[-1].set_xlabel("Month")

    return fig


def plot_highest_avg_death_rates(highest_avg_death_rate_df):
    """
    Plots average death rates.

    Parameters:
        highest_avg_death_rate_df: Dataframe with highest avg death rates

    Returns:
        fig: matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=highest_avg_death_rate_df,
        x="Death Rate",
        y="Country/Region",
        palette="Reds_r",
        ax=ax,
    )
    ax.set_title("Top Countries by Average Death Rate (2020)")
    ax.set_xlabel("Death Rate")
    ax.set_ylabel("Country")

    return fig


def plot_us_monthly_recovery_ratio(us_ratio_df):
    """
    Plots monthly recovery ratio of US as a bar chart.

    Parameters:
        us_ratio_df: DataFrame with 'Month' (datetime) and 'Recovery Ratio'

    Returns:
        fig: matplotlib.figure.Figure
    """
    us_ratio_df["Month"] = us_ratio_df["Month"].dt.to_timestamp()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(us_ratio_df["Month"], us_ratio_df["Recovery Ratio"], color="green", width=20)

    ax.set_title("US Monthly Recovery Ratio (Mar 2020 - May 2021)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Recovery Ratio")
    ax.grid(True, axis="y")
    fig.autofmt_xdate()

    return fig

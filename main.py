from src.pipeline.data_loader import load_data, get_dataset_info
from src.pipeline.visualizer import (
    save_top_countries_confirmed_cases_plot, save_china_countries_confirmed_cases_plot
)
from src.pipeline.data_cleaner import (
    handle_missing_data, transform_from_wide_to_long, merge_datasets
)
from src.pipeline.analyzer import (
    peak_daily_cases_by_country, compare_recovery_rate, distribution_of_death_rates,
    get_total_deaths_per_country, get_highest_avg_daily_deaths, total_deaths_overtime,
    merged_monthly_sum
)
from src.utils.constants import DATASET_DIR
from src.utils.enums import DatasetType

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

def main():
    # Q1.1
    deaths_raw = load_data(DATASET_DIR / 'covid_19_deaths_v1.csv')
    confirmed_cases_raw = load_data(DATASET_DIR / 'covid_19_confirmed_v1.csv')
    recovered_raw = load_data(DATASET_DIR / 'covid_19_recovered_v1.csv')

    # Q2.1
    # print(get_dataset_info(deaths_raw))
    # print(get_dataset_info(confirmed_cases_raw))
    # print(get_dataset_info(recovered_raw))

    # Q2.2
    # save_top_countries_confirmed_cases_plot(confirmed_cases_raw)

    # Q2.3
    # save_china_countries_confirmed_cases_plot(confirmed_cases_raw)
    
    
    # Q3 - 4
    confirmed_cases_cleaned = handle_missing_data(confirmed_cases_raw, DatasetType.CONFIRMED_CASES)
    deaths_cleaned = handle_missing_data(deaths_raw, DatasetType.DEATHS)
    recovered_cleaned = handle_missing_data(recovered_raw, DatasetType.RECOVERED)
    # print(confirmed_cases_cleaned)
    # print(deaths_cleaned)
    # print(recovered_cleaned)
    # columns_with_na = confirmed_cases_cleaned.columns[confirmed_cases_cleaned.isnull().any()].tolist()
    # print(columns_with_na)
    # columns_with_na = deaths_cleaned.columns[deaths_cleaned.isnull().any()].tolist()
    # print(columns_with_na)
    # columns_with_na = recovered_cleaned.columns[recovered_cleaned.isnull().any()].tolist()
    # print(columns_with_na)

    # Q5.1
    # peak_daily_cases = peak_daily_cases_by_country(confirmed_cases_cleaned, ['Germany', 'France', 'Italy'])
    # print(peak_daily_cases)
    # TODO: Plot these

    # Q5.2
    # recovery_rates = compare_recovery_rate(
    #     recovered_cleaned=recovered_cleaned,
    #     confirmed_cases_cleaned=confirmed_cases_cleaned,
    #     country_one='Australia',
    #     country_two='Canada',
    #     date='12/31/20'
    # )
    # print(recovery_rates)
    # TODO: Plot above
    # TODO: Identify mean of above

    # Q5.3
    # death_rate_distribution = distribution_of_death_rates(
    #     deaths_cleaned=deaths_cleaned,
    #     confirmed_cases_cleaned=confirmed_cases_cleaned,
    #     country='Canada',
    #     date='5/29/21'
    # )
    # print(death_rate_distribution)
    # TODO: Plot above
    # TODO: Provide Insights

    # Q6.1
    # long_deaths_df = transform_from_wide_to_long(deaths_cleaned, DatasetType.DEATHS)
    # print(long_deaths_df)

    # Q6.2
    # total_deaths_per_country = get_total_deaths_per_country(deaths_cleaned)
    # print(total_deaths_per_country)

    # Q6.3
    # highest_avg_daily_deaths = get_highest_avg_daily_deaths(deaths_cleaned, 5)
    # print(highest_avg_daily_deaths)

    # Q6.4
    # deaths_overtime = total_deaths_overtime(deaths_cleaned, 'US')
    # print(deaths_overtime)

    # Q7.1
    merged_df = merge_datasets(
        deaths_cleaned=deaths_cleaned,
        confirmed_cases_cleaned=confirmed_cases_cleaned,
        recovered_cleaned=recovered_cleaned
    )
    # print(merged_df)

    # Q7.2
    monthly_sum = merged_monthly_sum(merged_df)
    # print(monthly_sum)
    # columns_with_na = monthly_sum.columns[monthly_sum.isnull().any()].tolist()
    # print(columns_with_na)
    
    """DONE"""


if __name__ == "__main__":
    main()
from src.pipeline.data_loader import load_data, get_dataset_info
from src.pipeline.visualizer import (
    save_top_countries_confirmed_cases_plot, save_china_countries_confirmed_cases_plot
)
from src.pipeline.data_cleaner import handle_deaths_missing_data, handle_confirmed_cases_missing_data, handle_recovered_missing_data
from src.pipeline.analyzer import peak_daily_cases_by_country, compare_recovery_rate, distribution_of_death_rates
from src.logger.logger import logger
from src.utils.constants import DATASET_DIR

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
    deaths_cleaned = handle_deaths_missing_data(deaths_raw)
    confirmed_cases_cleaned = handle_confirmed_cases_missing_data(confirmed_cases_raw)
    recovered_cleaned = handle_recovered_missing_data(recovered_raw)
    # print(deaths_cleaned)
    # print(confirmed_cases_cleaned)
    # print(recovered_cleaned)

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

    """DONE"""
    # Q6.1


if __name__ == "__main__":
    main()
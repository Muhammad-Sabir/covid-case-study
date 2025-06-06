from src.pipeline.data_loader import load_data, get_dataset_info
from src.pipeline.visualizer import (
    save_top_countries_confirmed_cases_plot, save_china_countries_confirmed_cases_plot
)
from src.pipeline.data_cleaner import handle_deaths_missing_data, handle_confirmed_cases_missing_data, handle_recovered_missing_data
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

    # Q 2.3
    # save_china_countries_confirmed_cases_plot(confirmed_cases_raw)
    
    
    # Q. 3 - 4
    deaths_cleaned = handle_deaths_missing_data(deaths_raw)
    confirmed_cases_cleaned = handle_confirmed_cases_missing_data(confirmed_cases_raw)
    recovered_cleaned = handle_recovered_missing_data(recovered_raw)
    # print(deaths_cleaned)
    # print(confirmed_cases_cleaned)
    # print(recovered_cleaned)

    """DONE"""
    


if __name__ == "__main__":
    main()
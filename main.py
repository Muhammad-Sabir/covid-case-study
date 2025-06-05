from src.pipeline.data_loader import load_data, get_dataset_info
from src.pipeline.visualizer import (
    save_top_countries_confirmed_cases_plot, save_china_countries_confirmed_cases_plot
)
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
    save_top_countries_confirmed_cases_plot(confirmed_cases_raw)

    # Q 2.3
    save_china_countries_confirmed_cases_plot(confirmed_cases_raw)
    
    """DONE"""


    # Q. 3 - 4
    # remained_deaths_columns = deaths_df.rename(columns=deaths_df.iloc[0])
    # print("\n")
    # remained_deaths_columns = remained_deaths_columns.drop(remained_deaths_columns.index[0]).reset_index(drop=True)
    # print("remained_deaths_columns: \n", remained_deaths_columns.tail(60))
    # remained_deaths_columns.info()
    # print(remained_deaths_columns.isnull().sum(c))
    # print(remained_deaths_columns.isna().sum())
    # print(remained_deaths_columns.isna().sum()[remained_deaths_columns.isna().sum() > 0].index.tolist())
    # remained_deaths_columns["Province/State"].fillna("All Provinces", inplace=True)
    # print(remained_deaths_columns.shape)
    # remained_deaths_columns.dropna(inplace=True, subset=["Lat", "Lat"])
    # remained_deaths_columns.ffill(inplace=True, axis=1)
    # print(remained_deaths_columns[['4/17/20', '4/18/20', '4/19/20', '4/20/20', '4/21/20', '4/22/20', '4/23/20']].head())
    # print(remained_deaths_columns.isna().sum()[remained_deaths_columns.isna().sum() > 0].index.tolist())
    # print(remained_deaths_columns.shape)
    # print(remained_deaths_columns.isna().sum())
    # print(remained_deaths_columns.isna().sum())
    # print(remained_deaths_columns[50: 100])
    # print(deaths_df.head())
    # print(deaths_df.tail())
    # print(confirmed_deaths_df.head())
    # print("\n")
    # print(recovered_df.head())

    # Q4
    # remained_deaths_columns.fillna({"Province/State": "All Provinces"}, inplace=True)

if __name__ == "__main__":
    main()
from pathlib import Path

from src.pipeline.data_loader import load_data, get_dataset_info
from src.logger.logger import logger

def main():
    BASE_DIR = Path(__file__).resolve().parent
    DATASET_DIR = BASE_DIR / "dataset"

    logger.debug("HELLO")
    # Question 1
    deaths_raw = load_data(DATASET_DIR / "covid_19_deaths_v1.csv")
    confirmed_cases_raw = load_data(DATASET_DIR / "covid_19_confirmed_v1.csv")
    recovered_raw = load_data(DATASET_DIR / "covid_19_recovered_v1.csv")

    # Question 2.1
    print(get_dataset_info(deaths_raw))
    print(get_dataset_info(confirmed_cases_raw))
    print(get_dataset_info(recovered_raw))

    # print("DEATHS")
    # print(deaths_df.head())
    # print(deaths_df.shape)
    # print(deaths_df.dtypes)
    
    # print("CONFIRMED DEATHS")
    # print(confirmed_deaths_df.head(1))
    # print(confirmed_deaths_df.tail())
    # print(confirmed_deaths_df.shape)
    # print(confirmed_deaths_df.dtypes)
    # print(confirmed_deaths_df.info())
    
    # print("RECOVERED")
    # print(recovered_df.head())
    # print(recovered_df.shape)
    # print(recovered_df.dtypes)

    # Question 2.2
    # confirmed_deaths_df['date'] = 0
    # confirmed_deaths_df['deaths'] = 0
    # print(confirmed_deaths_df.head())
    # confirmed_deaths_columns = confirmed_deaths_df.columns
    # print(confirmed_deaths_df.loc['1/22/20'])
    # top_countries_confirmed_deaths = confirmed_deaths_df.drop(columns=['Province/State', 'Lat', 'Long'])
    # print("columns_to_drop: \n", top_countries_confirmed_deaths.head())

    # pakistan_confirmed_deaths = top_countries_confirmed_deaths[top_countries_confirmed_deaths['Country/Region'] == 'Pakistan']
    # print("pakistan_confirmed_deaths: \n", pakistan_confirmed_deaths)

    
    # data_against_dates = pakistan_confirmed_deaths.loc[:, '1/22/20': '5/29/21']
    # print("date_columns: \n", data_against_dates)
    # print("columns_to_drop: ", columns_to_drop)
    # confirmed_deaths_columns = confirmed_deaths_df.drop(columns=columns_to_drop)
    # print(confirmed_deaths_columns)

    # date_columns = pd.to_datetime(grouped_china_confirmed_deaths.columns, format='%m/%d/%y')
    # print("date_columns: ", date_columns)
    # print("data_against_dates.columns: ", type(data_against_dates.columns.to_series()))
    # plt.plot(date_columns, data_against_dates.values[0])
    # plt.plot(data_against_dates.values[0], data_against_dates.columns)
    # plt.grid(True)
    # plt.show()

    # Q 2.3
    # china_confirmed_deaths = top_countries_confirmed_deaths[top_countries_confirmed_deaths['Country/Region'] == 'China']
    # print("china_confirmed_deaths: \n", china_confirmed_deaths)
    # grouped_china_confirmed_deaths = china_confirmed_deaths.groupby('Country/Region').sum()
    # print("grouped_china_confirmed_deaths: \n", grouped_china_confirmed_deaths)
    # date_columns = pd.to_datetime(grouped_china_confirmed_deaths.columns, format='%m/%d/%y')
    # plt.figure(figsize=(14, 6))
    # plt.plot(date_columns, grouped_china_confirmed_deaths.values[0], label='Confirmed Deaths')
    # plt.title('COVID-19 Confirmed Deaths in China')
    # plt.xlabel('Date')
    # plt.ylabel('Deaths')
    # plt.legend()
    # plt.tight_layout()
    # plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # plt.xticks(rotation=15)
    # plt.grid(True)
    # plt.show()

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
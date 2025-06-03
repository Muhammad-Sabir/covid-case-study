import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print("Hello from covid-case-study!")
    
    # Question 1
    deaths_df = pd.read_csv("./dataset/covid_19_deaths_v1.csv")
    confirmed_deaths_df = pd.read_csv("./dataset/covid_19_confirmed_v1.csv")
    recovered_df = pd.read_csv("./dataset/covid_19_recovered_v1.csv")

    # Question 2.1
    # print("DEATHS")
    # print(deaths_df.head())
    # print(deaths_df.shape)
    # print(deaths_df.dtypes)
    
    print("CONFIRMED DEATHS")
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
    top_countries_confirmed_deaths = confirmed_deaths_df.drop(columns=['Province/State', 'Lat', 'Long'])
    print("columns_to_drop: \n", top_countries_confirmed_deaths.head())
    # print("columns_to_drop: ", columns_to_drop)
    # confirmed_deaths_columns = confirmed_deaths_df.drop(columns=columns_to_drop)
    # print(confirmed_deaths_columns)

    # plt.plot(top_countries_confirmed_deaths.columns, top_countries_confirmed_deaths.values)
    # plt.grid(True)
    # plt.show()

if __name__ == "__main__":
    main()
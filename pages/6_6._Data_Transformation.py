import inspect

import streamlit as st

from src.utils.enums import DatasetType
from src.utils.constants import DATASET_DIR
from src.pipeline.data_loader import load_data
from src.pipeline.data_cleaner import (
    handle_missing_data,
    rename_column_first_row,
    replace_empty_province,
    drop_non_existing_provinces,
    fix_datatypes,
    transform_from_wide_to_long,
    handle_missing_data,
    merge_datasets,
)
from src.pipeline.analyzer import (
    peak_daily_cases_by_country,
    compare_recovery_rate,
    distribution_of_death_rates,
    get_extreme_death_rates,
    get_total_deaths_per_country,
    get_highest_avg_daily_deaths,
    total_deaths_overtime,
    merged_monthly_sum,
    highest_avg_death_rates_2020,
    recovery_death_ratio,
    highest_recovery_confirmed_ratio,
)


confirmed_cases_raw = load_data(DATASET_DIR / "covid_19_confirmed_v1.csv")
deaths_raw = load_data(DATASET_DIR / "covid_19_deaths_v1.csv")
recovered_raw = load_data(DATASET_DIR / "covid_19_recovered_v1.csv")

confirmed_cases_cleaned = handle_missing_data(
    confirmed_cases_raw, DatasetType.CONFIRMED_CASES
)
deaths_cleaned = handle_missing_data(deaths_raw, DatasetType.DEATHS)
recovered_cleaned = handle_missing_data(recovered_raw, DatasetType.RECOVERED)

st.set_page_config(layout="wide")

st.title("Data Transformation")
st.caption(
    "This section is about transforming data and performing function in long format data."
)

# Question 6.1
st.markdown("**Q6.1**: Transform 'deaths' dataset from wide to long format.")

long_deaths_df = transform_from_wide_to_long(deaths_cleaned, DatasetType.DEATHS)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `transform_from_wide_to_long` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(transform_from_wide_to_long))

with output_tab:
    st.markdown("### Deaths DataFrame in Long Format")
    st.dataframe(long_deaths_df)

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 6.2
st.markdown("**Q6.2**: Total deaths per country to date.")

total_deaths_per_country = get_total_deaths_per_country(long_deaths_df)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `get_total_deaths_per_country` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(get_total_deaths_per_country))

with output_tab:
    st.markdown("### Total Deaths Per Country To Date")
    st.dataframe(total_deaths_per_country)

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 6.3
st.markdown("**Q6.3**: Top 5 countries by average daily deaths.")

highest_avg_daily_deaths = get_highest_avg_daily_deaths(long_deaths_df, 5)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `get_highest_avg_daily_deaths` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(get_highest_avg_daily_deaths))

with output_tab:
    st.markdown("### Top 5 Average Daily Deaths")
    st.dataframe(highest_avg_daily_deaths)

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 6.4
st.markdown("**Q6.4**: Evolution of total deaths in the US over time.")

deaths_overtime = total_deaths_overtime(long_deaths_df, "US")

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `total_deaths_overtime` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(total_deaths_overtime))

with output_tab:
    st.markdown("### US Total Death Evolution")
    st.dataframe(deaths_overtime)

with ai_insights_tab:
    st.markdown("### Coming soon...")

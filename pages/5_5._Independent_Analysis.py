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

st.title("Independent Dataset Analysis")
st.caption(
    "Deep-dive into specific country metrics and comparisons based on cleaned COVID-19 data."
)

# Question 5.1
st.markdown("**Q5.1**: Peak daily new cases in Germany, France, and Italy.")

peak_daily_cases = peak_daily_cases_by_country(
    confirmed_cases_cleaned, ["Germany", "France", "Italy"]
)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `peak_daily_cases_by_country` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(peak_daily_cases_by_country))

with output_tab:
    st.markdown("### Peak Daily Confirmed Cases")
    st.dataframe(peak_daily_cases)

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 5.2
st.markdown("**Q5.2**: Compare recovery rates: Canada vs Australia (as of Dec 31, 2020).")

recovery_rates = compare_recovery_rate(
    recovered_cleaned=recovered_cleaned,
    confirmed_cases_cleaned=confirmed_cases_cleaned,
    country_one='Australia',
    country_two='Canada',
    date='12/31/20'
)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `compare_recovery_rate` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(compare_recovery_rate))

with output_tab:
    st.markdown("### Recovery Rates: Canada vs Australia")
    st.dataframe(recovery_rates)

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 5.3
st.markdown("**Q5.3**: Death rate distribution among Canadian provinces.")

death_rate_distribution = distribution_of_death_rates(
    deaths_cleaned=deaths_cleaned,
    confirmed_cases_cleaned=confirmed_cases_cleaned,
    country='Canada',
    date='5/29/21'
)
max_death_rate = get_extreme_death_rates(death_rate_distribution)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `distribution_of_death_rates` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(distribution_of_death_rates))
    
    st.markdown("Source code of `get_extreme_death_rates` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(get_extreme_death_rates))

with output_tab:
    st.markdown("### Canadian Provinces Death Rate Distribution")
    st.dataframe(death_rate_distribution)

    st.markdown("### Provinces With Max Death Rate")
    st.dataframe(max_death_rate)

with ai_insights_tab:
    st.markdown("### Coming soon...")

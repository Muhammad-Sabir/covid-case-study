import inspect

import streamlit as st

from src.utils.enums import DatasetType
from src.utils.constants import DATASET_DIR
from src.pipeline.data_loader import load_data
from src.pipeline.data_cleaner import (
    handle_missing_data,
    merge_datasets,
)
from src.pipeline.analyzer import (
    highest_avg_death_rates_2020,
    recovery_death_ratio,
    highest_recovery_confirmed_ratio,
)
from src.pipeline.visualizer import (
    plot_highest_avg_death_rates,
    plot_us_monthly_recovery_ratio,
)
from src.llm.prompt import format_prompt
from src.llm.client import get_ai_insights


confirmed_cases_raw = load_data(DATASET_DIR / "covid_19_confirmed_v1.csv")
deaths_raw = load_data(DATASET_DIR / "covid_19_deaths_v1.csv")
recovered_raw = load_data(DATASET_DIR / "covid_19_recovered_v1.csv")

confirmed_cases_cleaned = handle_missing_data(
    confirmed_cases_raw, DatasetType.CONFIRMED_CASES
)
deaths_cleaned = handle_missing_data(deaths_raw, DatasetType.DEATHS)
recovered_cleaned = handle_missing_data(recovered_raw, DatasetType.RECOVERED)

merged_df = merge_datasets(
    deaths_cleaned=deaths_cleaned,
    confirmed_cases_cleaned=confirmed_cases_cleaned,
    recovered_cleaned=recovered_cleaned,
)

st.set_page_config(layout="wide")

st.title("Combined Data Analysis")
st.caption("This section performs analysis on merged data.")

# Question 8.1
st.markdown("**Q8.1**: Countries with highest average death rates in 2020.")

top_3_avg = highest_avg_death_rates_2020(merged_df, 3)
prompt = format_prompt(
    question="For the combined dataset, identify the three countries with the highest average death rates (deaths/confirmed cases) throughout 2020. What might this indicate about the pandemic's impact in these countries?",
    data=top_3_avg.to_markdown(index=False),
)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `highest_avg_death_rates_2020` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(highest_avg_death_rates_2020))
    with st.expander("View Source Code"):
        st.code(inspect.getsource(plot_highest_avg_death_rates))

with output_tab:
    st.markdown("### Highest Average Death Rate Countries in 2020")
    st.dataframe(top_3_avg)
    st.pyplot(plot_highest_avg_death_rates(top_3_avg))

with ai_insights_tab:
    if st.button("Generate Insights", key="generate_insights_button_1"):
        get_ai_insights(prompt)

st.markdown("---")

# Question 8.2
st.markdown("**Q8.2**: Compare total recoveries vs deaths in South Africa.")

sa_ratio = recovery_death_ratio(merged_df, "South Africa")
prompt = format_prompt(
    question="Using the merged dataset, compare the total number of recoveries to the total number of deaths in South Africa. What can this tell us about the outcomes of COVID-19 cases in the country?",
    data=str(sa_ratio),
)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `recovery_death_ratio` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(recovery_death_ratio))

with output_tab:
    st.markdown("### South Africa Recoveries vs Deaths")
    st.code("South Africa Recoveries to Death Ratio: " + str(sa_ratio))

with ai_insights_tab:
    if st.button("Generate Insights", key="generate_insights_button_2"):
        get_ai_insights(prompt)

st.markdown("---")

# Question 8.3
st.markdown("**Q8.3**: US recovery ratio (monthly) from Mar 2020 to May 2021.")

us_ratio = highest_recovery_confirmed_ratio(merged_df, "US")
prompt = format_prompt(
    question="Analyze the ratio of recoveries to confirmed cases for the United States monthly from March 2020 to May 2021. Which month experienced the highest recovery ratio, and what could be the potential reasons?",
    data=us_ratio.to_markdown(index=False),
)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of getting `highest_recovery_confirmed_ratio` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(highest_recovery_confirmed_ratio))
    with st.expander("View Source Code"):
        st.code(inspect.getsource(plot_us_monthly_recovery_ratio))

with output_tab:
    st.markdown("### US Monthly Recovery Ratio")
    st.dataframe(us_ratio)
    st.pyplot(plot_us_monthly_recovery_ratio(us_ratio))

with ai_insights_tab:
    if st.button("Generate Insights", key="generate_insights_button_3"):
        get_ai_insights(prompt)

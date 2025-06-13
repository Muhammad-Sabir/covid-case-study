import inspect

import streamlit as st

from src.utils.enums import DatasetType
from src.utils.constants import DATASET_DIR
from src.pipeline.data_loader import load_data
from src.pipeline.data_cleaner import (
    handle_missing_data,
    merge_datasets,
)
from src.pipeline.analyzer import merged_monthly_sum
from src.pipeline.visualizer import (
    plot_global_monthly_sums,
    plot_monthly_trends_by_country,
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

st.title("Data Merging")
st.caption("This section merges all three datasets and analyze monthly sums.")

# Question 7.1
st.markdown("**Q7.1**: Merge confirmed, deaths, and recovery datasets.")

merged_df = merge_datasets(
    deaths_cleaned=deaths_cleaned,
    confirmed_cases_cleaned=confirmed_cases_cleaned,
    recovered_cleaned=recovered_cleaned,
)

code_tab, output_tab = st.tabs(["Code", "Results"])

with code_tab:
    st.markdown("Source code of `merge_datasets` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(merge_datasets))

with output_tab:
    st.markdown("### Merrged Dataset")
    st.dataframe(merged_df)

st.markdown("---")

# Question 7.2
st.markdown("**Q7.2**: Monthly sums of confirmed, deaths, recoveries by country.")

monthly_sum = merged_monthly_sum(merged_df)

code_tab, output_tab = st.tabs(["Code", "Results"])

with code_tab:
    st.markdown("Source code of `merged_monthly_sum` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(merged_monthly_sum))
    with st.expander("View Source Code"):
        st.code(inspect.getsource(plot_global_monthly_sums))

with output_tab:
    st.markdown("### Monthly Sum")
    st.dataframe(monthly_sum)
    st.pyplot(plot_global_monthly_sums(monthly_sum))

st.markdown("---")

# Question 7.3
st.markdown("**Q7.3**: Repeat Q7.2 for US, Italy, Brazil.")

countries = ["US", "Italy", "Brazil"]
filtered_monthly_sum = monthly_sum[monthly_sum["Country/Region"].isin(countries)]

code_tab, output_tab = st.tabs(["Code", "Results"])

with code_tab:
    st.markdown("Source code of getting `filtered_monthly_sum`")
    with st.expander("View Source Code"):
        st.code(
            """
            countries = ['US', 'Italy', 'Brazil'] 
            filtered_monthly_sum = monthly_sum[monthly_sum['Country/Region'].isin(countries)]
            """
        )
    with st.expander("View Source Code"):
        st.code(inspect.getsource(plot_monthly_trends_by_country))

with output_tab:
    st.markdown("### Monthly Sum for US, Brazil, Italy")
    st.dataframe(filtered_monthly_sum)
    st.pyplot(plot_monthly_trends_by_country(filtered_monthly_sum, countries))

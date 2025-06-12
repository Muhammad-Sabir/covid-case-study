import inspect

import streamlit as st

from src.utils.constants import DATASET_DIR
from src.pipeline.data_loader import load_data

st.set_page_config(layout="wide")

st.title("Data Loading")
st.caption(
    "This section loads and displays COVID-19 datasets using custom data loading logic."
)

st.markdown("**Q1.1**: Load the COVID-19 datasets using Pandas")

confirmed_cases_raw = load_data(DATASET_DIR / "covid_19_confirmed_v1.csv")
deaths_raw = load_data(DATASET_DIR / "covid_19_deaths_v1.csv")
recovered_raw = load_data(DATASET_DIR / "covid_19_recovered_v1.csv")

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `load_data` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(load_data))

with output_tab:
    st.markdown("### Confirmed Cases")
    st.dataframe(confirmed_cases_raw)
    st.markdown("### Deaths")
    st.dataframe(deaths_raw)
    st.markdown("### Recovered Cases")
    st.dataframe(recovered_raw)

with ai_insights_tab:
    st.markdown("### Coming soon...")

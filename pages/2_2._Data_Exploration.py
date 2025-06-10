import inspect

import streamlit as st

from src.utils.constants import DATASET_DIR
from src.pipeline.data_loader import load_data, get_dataset_info
from src.pipeline.visualizer import (
    get_top_countries_confirmed_cases_plot,
    get_china_countries_confirmed_cases_plot,
)

st.set_page_config(layout="wide")

st.title("Data Exploration")
st.caption("Explore the structure and trends in the COVID-19 dataset.")

# Question 2.1
st.markdown("**Q2.1**: Examine structure — rows, columns, data types.")

confirmed_cases_raw = load_data(DATASET_DIR / "covid_19_confirmed_v1.csv")
deaths_raw = load_data(DATASET_DIR / "covid_19_deaths_v1.csv")
recovered_raw = load_data(DATASET_DIR / "covid_19_recovered_v1.csv")

confirmed_info = get_dataset_info(confirmed_cases_raw)
deaths_info = get_dataset_info(deaths_raw)
recovered_info = get_dataset_info(recovered_raw)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source Code of `get_dataset_info` Function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(get_dataset_info))

with output_tab:
    st.markdown("### Confirmed Cases")
    st.code(confirmed_info)
    st.markdown("### Deaths")
    st.code(deaths_info)
    st.markdown("### Recovered Cases")
    st.code(recovered_info)

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 2.2
st.markdown("**Q2.2**: Plot confirmed cases over time for top countries.")

top_countries_fig = get_top_countries_confirmed_cases_plot(confirmed_cases_raw)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source Code of `get_top_countries_confirmed_cases_plot` Function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(get_top_countries_confirmed_cases_plot))

with output_tab:
    st.markdown("### Confirmed Cases")

    if top_countries_fig:
        st.pyplot(top_countries_fig)
    else:
        st.error("Failed to generate the plot.")

with ai_insights_tab:
    st.markdown("### Coming soon...")

st.markdown("---")

# Question 2.3
st.markdown("**Q2.3**: Plot confirmed cases over time for China.")

china_confirmed_fig = get_china_countries_confirmed_cases_plot(confirmed_cases_raw)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source Code of `get_china_countries_confirmed_cases_plot` Function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(get_china_countries_confirmed_cases_plot))

with output_tab:
    st.markdown("### Confirmed Cases")

    if china_confirmed_fig:
        st.pyplot(china_confirmed_fig)
    else:
        st.error("Failed to generate the plot.")

with ai_insights_tab:
    st.markdown("### Coming soon...")
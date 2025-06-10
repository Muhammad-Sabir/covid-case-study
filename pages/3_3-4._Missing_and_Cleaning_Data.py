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

confirmed_cases_raw = load_data(DATASET_DIR / "covid_19_confirmed_v1.csv")
deaths_raw = load_data(DATASET_DIR / "covid_19_deaths_v1.csv")
recovered_raw = load_data(DATASET_DIR / "covid_19_recovered_v1.csv")

confirmed_cases_cleaned = handle_missing_data(
    confirmed_cases_raw, DatasetType.CONFIRMED_CASES
)
deaths_cleaned = handle_missing_data(deaths_raw, DatasetType.DEATHS)
recovered_cleaned = handle_missing_data(recovered_raw, DatasetType.RECOVERED)

st.set_page_config(layout="wide")

st.title("Handling Missing Data & Cleaning")
st.caption(
    "This section handles missing values and cleans the COVID-19 dataset for further analysis."
)

# Question 3.1 - 4.1
st.markdown("**Q3.1**: Identify and impute missing values using forward fill.")
st.markdown(
    "**Q4.1**: Replace blank values in the Province column with `'All Provinces'`."
)

code_tab, output_tab, ai_insights_tab = st.tabs(["Code", "Results", "AI Insights"])

with code_tab:
    st.markdown("Source code of `handle_missing_data` function")
    with st.expander("View Source Code"):
        st.code(inspect.getsource(handle_missing_data))

    st.markdown(
        "Source code of helper functions and enums used in `handle_missing_data`"
    )
    with st.expander("View Source Code of `rename_column_first_row`"):
        st.code(inspect.getsource(rename_column_first_row))

    with st.expander("View Source Code of `replace_empty_province`"):
        st.code(inspect.getsource(replace_empty_province))

    with st.expander("View Source Code of `drop_non_existing_provinces`"):
        st.code(inspect.getsource(drop_non_existing_provinces))

    with st.expander("View Source Code of `fix_datatypes`"):
        st.code(inspect.getsource(fix_datatypes))

    with st.expander("View Source Code of `DatasetType`"):
        st.code(inspect.getsource(DatasetType))

with output_tab:
    st.markdown("### Cleaned Confirmed Cases")
    st.dataframe(confirmed_cases_cleaned)
    st.markdown("### Cleaned Deaths")
    st.dataframe(deaths_cleaned)
    st.markdown("### Cleaned Recovered Cases")
    st.dataframe(recovered_cleaned)

with ai_insights_tab:
    st.markdown("### Coming soon...")

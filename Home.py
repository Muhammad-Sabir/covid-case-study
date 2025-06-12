import streamlit as st


def main():
    st.set_page_config(page_title="COVID-19 Case Study", layout="wide", page_icon="🦠")

    st.title("COVID-19 Data Analysis Case Study")

    st.markdown("### Background")
    st.write(
        """
        The COVID-19 pandemic, caused by the SARS-CoV-2 virus, emerged in late 2019 and rapidly spread globally, leading to significant health, economic, and social impacts.
        This unprecedented health crisis highlighted the crucial role of data analysis in managing such pandemics. By meticulously tracking and analyzing data on 
        confirmed cases, recoveries, and deaths, policymakers and health professionals can make informed decisions to control the spread of the virus and allocate 
        resources effectively.
        """
    )

    st.markdown("### Dataset Details")
    st.write("""
    This case study utilizes three key datasets, each providing daily updates on different aspects of the pandemic for various countries and regions:
    - **Confirmed Cases Dataset**: Cumulative confirmed COVID-19 cases per day from Jan 22, 2020 to May 29, 2021 across over 276 regions.
    - **Deaths Dataset**: Cumulative deaths attributed to COVID-19 over the same period and locations.
    - **Recovered Cases Dataset**: Cumulative recoveries to assess progression and treatment effectiveness.

    Each dataset includes:
    - Province/State
    - Country/Region
    - Geographic coordinates (Lat, Long)
    - Daily cumulative totals
    """)

    st.markdown("### Objective of the Case Study")
    st.write("""
    - **Practical Application of Python**: Enhance Python skills through real-world data tasks including cleaning, transformation, and visualization.
    - **Insightful Data Analysis**: Derive key insights into the spread and impact of COVID-19 across time and geographies.
    - **Skill Development**: Use essential Python libraries: `Pandas`, `Numpy`, `Matplotlib`, and `Seaborn`.
    """)

    st.markdown("### Data Analysis Problems")
    with st.expander("Question 1: Data Loading"):
        st.markdown("**Q1.1**: Load the COVID-19 datasets using Pandas.")

    with st.expander("Question 2: Data Exploration"):
        st.markdown("**Q2.1**: Examine structure: rows, columns, data types.")
        st.markdown("**Q2.2**: Plot confirmed cases over time for top countries.")
        st.markdown("**Q2.3**: Plot confirmed cases over time for China.")

    with st.expander("Question 3: Handling Missing Data"):
        st.markdown("**Q3.1**: Identify and impute missing values using forward fill.")

    with st.expander("Question 4: Data Cleaning and Preparation"):
        st.markdown(
            "**Q4.1**: Replace blank values in the Province column with 'All Provinces'."
        )

    with st.expander("Question 5: Independent Dataset Analysis"):
        st.markdown("**Q5.1**: Peak daily new cases in Germany, France, and Italy.")
        st.markdown(
            "**Q5.2**: Compare recovery rates: Canada vs Australia (as of Dec 31, 2020)."
        )
        st.markdown("**Q5.3**: Death rate distribution among Canadian provinces.")

    with st.expander("Question 6: Data Transformation"):
        st.markdown("**Q6.1**: Transform 'deaths' dataset from wide to long format.")
        st.markdown("**Q6.2**: Total deaths per country to date.")
        st.markdown("**Q6.3**: Top 5 countries by average daily deaths.")
        st.markdown("**Q6.4**: Evolution of total deaths in the US over time.")

    with st.expander("Question 7: Data Merging"):
        st.markdown("**Q7.1**: Merge confirmed, deaths, and recovery datasets.")
        st.markdown(
            "**Q7.2**: Monthly sums of confirmed, deaths, recoveries by country."
        )
        st.markdown("**Q7.3**: Repeat Q7.2 for US, Italy, Brazil.")

    with st.expander("Question 8: Combined Data Analysis"):
        st.markdown("**Q8.1**: Countries with highest average death rates in 2020.")
        st.markdown("**Q8.2**: Compare total recoveries vs deaths in South Africa.")
        st.markdown("**Q8.3**: US recovery ratio (monthly) from Mar 2020 to May 2021.")

    st.markdown("---")
    st.success("Use the sidebar to explore data visualizations and insights!")


if __name__ == "__main__":
    main()

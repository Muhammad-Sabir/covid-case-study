# Covid-19 Case Study

This repository contains an interactive COVID-19 data analysis project built using Python and Streamlit. The application analyzes pandemic data, provides visual insights, and incorporates AI-generated analysis on selected questions using the Gemini Flash 1.5 API.

Live Application: [https://muhammad-sabir-covid-case-study-home-jmlzdt.streamlit.app/](https://muhammad-sabir-covid-case-study-home-jmlzdt.streamlit.app/)

---

## Project Overview

The goal of this project is to explore COVID-19 data through various statistical methods and present findings in an accessible dashboard. The analysis is enhanced by AI-generated insights for selected case study questions. All data processing and visualizations are done in Python, and the results are displayed using a Streamlit web interface.

---

## Features

- Case study analysis using pandas
- Visualizations using matplotlib and seaborn
- Interactive dashboard built with Streamlit
- Custom logging for internal monitoring
- Integration of AI insights using Gemini Flash 1.5 API
- Deployed on Streamlit Cloud

---

## AI Integration

AI-generated insights were included for the following questions:

- 5.1
- 5.2
- 5.3
- 6.3
- 6.4
- 8.1
- 8.2
- 8.3

These insights are retrieved using the Gemini Flash 1.5 model and supplement the manual analysis performed in the project.

---

## Installation and Usage

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Steps to Run Locally

1. Install `uv` if not already installed
2. Launch the Streamlit app:
```bash
uv run streamlit run Home.py
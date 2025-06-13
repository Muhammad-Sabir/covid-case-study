# General base prompt template
BASE_INSIGHT_PROMPT = """You are a data analyst helping interpret COVID-19 data.

Background
The COVID-19 pandemic, caused by the SARS-CoV-2 virus, emerged in late 2019 and rapidly spread globally, leading to significant health, economic, and social impacts. This unprecedented health crisis highlighted the crucial role of data analysis in managing such pandemics. By meticulously tracking and analyzing data on confirmed cases, recoveries, and deaths, policymakers and health professionals can make informed decisions to control the spread of the virus and allocate resources effectively.

Given the following data and the analysis question, provide insights in plain English:
- Identify trends, anomalies, and possible explanations.
- Make sure your answer is clear, concise, and understandable for a non-technical audience.

Question:
{question}

Data:
{data}
"""


def format_prompt(question, data, template=BASE_INSIGHT_PROMPT):
    """
    Formats a prompt for the LLM using the provided question and data.

    Args:
        question: The analysis question.
        data: The result of the analysis in plain text or tabular string format.
        template: A custom prompt template (defaults to BASE_INSIGHT_PROMPT).

    Returns:
        str: A formatted prompt string to send to the LLM.
    """
    return template.format(question=question.strip(), data=data.strip())

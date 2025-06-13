import time
import streamlit as st
from google import genai


GEMINI_API_KEY = st.secrets.GEMINI_API_KEY


def get_ai_insights(prompt):
    """
    Fetches AI insights from the Gemini model with streaming.

    Args:
        prompt: The input prompt for the AI model.
    """
    model_name = "models/gemini-1.5-flash"
    client = genai.Client(api_key=GEMINI_API_KEY)

    response_placeholder = st.empty()
    full_response_text = ""

    try:
        # Call generate_content with stream=True to enable streaming
        stream_response = client.models.generate_content_stream(model=model_name, contents=prompt)

        # Iterate over the streamed chunks and update the placeholder
        for chunk in stream_response:
            # Check if the chunk has text content before appending
            if chunk.text:
                full_response_text += chunk.text
                response_placeholder.markdown(full_response_text + "▌") # Add a blinking cursor effect
                
            time.sleep(0.05)

    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # After streaming is complete, display the final text without the cursor
        response_placeholder.markdown(full_response_text)

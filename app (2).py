
import streamlit as st
from groq import Groq
from crewai import Crew
from crewai import Agent, Task
import config # Import the config file

# Use GROQ_API_KEY from config.py
GROQ_API_KEY = config.GROQ_API_KEY

st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="🚀",
    layout="wide"
)

st.title(f"🚀 {config.APP_NAME}")
st.subheader("Your AI Marketing Assistant")

client = Groq(api_key=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)

idea = st.text_area(
    "Enter your marketing idea",
    placeholder="Example: Promote luxury plots at Vannahills Estate with flexible payment plans."
)

if st.button("Generate Campaign"):

    if not idea.strip():
        st.warning("Please enter a marketing idea.")
    else:

        with st.spinner("Generating campaign..."):

            prompt = f'''
You are an expert marketing strategist.

Generate:

1. Marketing Strategy
2. Target Audience
3. Facebook Post
4. Instagram Caption
5. LinkedIn Post
6. Five Hashtags
7. Call To Action

Idea:

{idea}
'''

            response = client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = response.choices[0].message.content

        st.success("Campaign Generated Successfully!")

        st.markdown(result)

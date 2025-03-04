import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY") 

# Configure the API key (ideally from an environment variable)
genai.configure(api_key=API_KEY)  # Replace with your actual API key or use os.getenv("GOOGLE_API_KEY")

st.header("Welcome! to AI Chatbot")
text = st.text_input("Write me your query")

if st.button("Click Me!"):
    if text:  # Check if the input is not empty
        with st.spinner("🤖 Thinking... Please wait!"):
        # Specify the model
            model = genai.GenerativeModel("gemini-2.0-flash")  # Use an appropriate model name, e.g., "gemini-pro"
        
        # Generate content
            response = model.generate_content(text)
        
        # Display the response
            st.write(response.candidates[0].content.parts[0].text)
    else:
        st.write("Please enter a query first!")        
import streamlit as st
import requests

# Streamlit UI setup
st.title('Market Brief Assistant')

# Text input for stock symbol
symbol = st.text_input('Enter Stock Symbol', 'AAPL')

# Button to request market brief
if st.button('Get Market Brief'):
    # Send a GET request to the FastAPI backend
    response = requests.get(f'http://127.0.0.1:8000/market_brief/{symbol}')

    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Display the generated narrative from the backend
        st.write("Market Brief Narrative:")
        st.write(data['narrative'])
    else:
        st.write("Error fetching data. Please try again.")

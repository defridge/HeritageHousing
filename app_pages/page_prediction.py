import streamlit as st
import pandas as pd
import requests  # To send the data to the Flask API

def app():
    st.title("House Price Prediction")

    # Flask API URL (update this with your actual Flask API URL)
    API_URL = 'https://housingmodel-api-6a6b8e797fa2.herokuapp.com/predict' # Update with your actual API URL if running remotely

    st.write(
        """
        ### Predict House Sale Prices
        Use the form below to input house features and predict the sale price using the trained model.
        """
    )

    # Create input fields for house attributes
    grlivarea = st.number_input("Above grade (ground) living area square feet:", min_value=0, value=1500)
    total_sf = st.number_input("Total square footage (first floor + second floor + basement):", min_value=0, value=2000)
    garage_area = st.number_input("Garage area (square feet):", min_value=0, value=500)
    year_built = st.number_input("Year the house was built:", min_value=1800, max_value=2023, value=2000)
    overall_qual = st.slider("Overall quality (1-10):", min_value=1, max_value=10, value=5)

    # Prepare the input data for the API
    input_data = {
        'GrLivArea': grlivarea,
        'TotalSF': total_sf,
        'GarageArea': garage_area,
        'YearBuilt': year_built,
        'OverallQual': overall_qual
    }

    # Display the user inputted data
    st.write("#### Your Inputted House Features")
    st.write(pd.DataFrame([input_data]))

    # Predict the sale price using the API
    if st.button("Predict Sale Price"):
        try:
            # Send the request to the Flask API and get the response
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                prediction = response.json()['prediction']
                st.write(f"### Predicted Sale Price: ${prediction:,.2f}")
            else:
                st.write(f"Error: {response.status_code}. Failed to get prediction from API.")
        except Exception as e:
            st.write(f"Error: {str(e)}")

    st.write("---")
    st.write("### Predicted Prices for Inherited Houses")

    # (Optional) You could add similar logic to send the inherited houses data to the Flask API as well,
    # but for now, we'll keep it simple and focus on the single house prediction.

import streamlit as st
import pandas as pd
import requests

def app():
    st.title("House Price Prediction")

    
    API_URL = 'https://housingmodel-api-6a6b8e797fa2.herokuapp.com/predict'

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

    # Load the inherited houses dataset
    inherited_houses = pd.read_csv('outputs/datasets/collection/inherited_houses_cleaned.csv')

    # Align columns with expected API input
    X_train = pd.read_csv('outputs/datasets/collection/X_train.csv')
    inherited_houses_data = inherited_houses.reindex(columns=X_train.columns, fill_value=0)

    # Prepare the input data for the API (as a list of dictionaries)
    inherited_houses_json = inherited_houses_data.to_dict(orient='records')

    # Send the request to the Flask API for the inherited houses predictions
    try:
        response = requests.post(API_URL, json=inherited_houses_json)
        if response.status_code == 200:
            predictions = response.json()['predictions']
            inherited_houses['Predicted_SalePrice'] = predictions

            # Display the inherited houses with their predicted sale prices
            st.write(inherited_houses[['GrLivArea', 'TotalSF', 'GarageArea', 'YearBuilt', 'OverallQual', 'Predicted_SalePrice']])
        else:
            st.write(f"Error: {response.status_code}. Failed to get predictions from API for inherited houses.")
    except Exception as e:
        st.write(f"Error: {str(e)}")

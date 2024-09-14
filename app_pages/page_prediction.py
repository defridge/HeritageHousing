import streamlit as st
import pandas as pd
import joblib

def app():
    st.title("House Price Prediction")

    # Load the trained XGBoost model
    model = joblib.load('outputs/models/xgb_model.pkl')

    # Load the cleaned dataset for inherited houses
    inherited_houses_cleaned = pd.read_csv('outputs/datasets/collection/inherited_houses_cleaned.csv')
    
    # Load the X_train dataset to ensure feature alignment
    X_train = pd.read_csv('outputs/datasets/collection/X_train.csv')
    
    # Align inherited_houses_cleaned columns with X_train (ensure same columns and order)
    inherited_houses_data = inherited_houses_cleaned.reindex(columns=X_train.columns, fill_value=0)
    
    st.write(
        """
        ### Predict House Sale Prices
        Use the form below to input house features and predict the sale price using the trained XGBoost model.
        """
    )

    # Create input fields for house attributes
    grlivarea = st.number_input("Above grade (ground) living area square feet:", min_value=0, value=1500)
    total_sf = st.number_input("Total square footage (first floor + second floor + basement):", min_value=0, value=2000)
    garage_area = st.number_input("Garage area (square feet):", min_value=0, value=500)
    year_built = st.number_input("Year the house was built:", min_value=1800, max_value=2023, value=2000)
    overall_qual = st.slider("Overall quality (1-10):", min_value=1, max_value=10, value=5)

    # Prepare the input data for the model
    input_data = pd.DataFrame({
        'GrLivArea': [grlivarea],
        'TotalSF': [total_sf],
        'GarageArea': [garage_area],
        'YearBuilt': [year_built],
        'OverallQual': [overall_qual]
    })

    # Display the user inputted data
    st.write("#### Your Inputted House Features")
    st.write(input_data)

    # Predict the sale price using the trained model
    if st.button("Predict Sale Price"):
        # Align input_data columns with X_train
        input_data_aligned = input_data.reindex(columns=X_train.columns, fill_value=0)
        prediction = model.predict(input_data_aligned)[0]
        st.write(f"### Predicted Sale Price: ${prediction:,.2f}")

    st.write("---")
    st.write("### Predicted Prices for Inherited Houses")
    st.write("Below are the predicted sale prices for Lydia's inherited houses.")

    # Predict the prices for the inherited houses
    inherited_houses_cleaned['Predicted_SalePrice'] = model.predict(inherited_houses_data)

    # Display the inherited houses with their predicted sale prices
    st.write(inherited_houses_cleaned[['GrLivArea', 'TotalSF', 'GarageArea', 'YearBuilt', 'OverallQual', 'Predicted_SalePrice']])

    st.write(
        """
        ---
        The predicted sale prices for Lydia’s inherited houses, along with any house in Ames, Iowa, 
        can be calculated based on the input features above. The model achieves more than 75% accuracy,
        ensuring that the predictions are aligned with the business requirements.
        """
    )

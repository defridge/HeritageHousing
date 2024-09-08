import streamlit as st

def app():
    st.title("Project Summary")
    
    st.header("Objective")
    st.write("""
    The objective of this project is to develop a machine learning model that predicts the sale price of the clients inherited houses, as well as any house in Ames, Iowa, with at least 75% accuracy.
    """)
    
    st.header("Business Requirements")
    st.write("""
    1. Predict the sale price for the client and any house in Ames, Iowa.
    2. Provide price predictions for four specific houses inherited by the client.
    3. Ensure the model is interpretable and can provide insights into factors that influence house prices.
    """)

    st.write("---")

    st.header("Dataset Overview")
    st.write(
        "This dataset contains detailed records about houses built "
        "in Ames, Iowa, between 1872 and 2010. It contains key features "
        "that are relevant for predicting sale prices such as:\n"
        "- **SalePrice** (the target variable)\n"
        "- **1stFlrSF**: First floor square footage\n"
        "- **GrLivArea**: Above ground living area square footage\n"
        "- **TotalBsmtSF**: Basement area in square feet\n"
        "- **YearBuilt**: Year the house was built\n"
        "- **OverallQual**: Overall material and finish quality\n"
        "- **LotArea**: Lot size in square feet\n"
    )
    
    st.header("Dataset Information")
    st.write("""
    The dataset contains information on various features of houses in Ames, Iowa, including lot size, square footage, and several other features that may impact the sale price. It is cleaned and processed to remove missing values and handle categorical variables.
    """)

import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

def app():
    st.title("Model Performance Evaluation")

    # Flask API URL for model performance
    API_URL = 'https://housingmodel-api-6a6b8e797fa2.herokuapp.com/model_performance'

    st.write(
        """
        ## Model Performance Metrics
        This page provides insights into how well the machine learning models performed on the training and testing datasets.
        """
    )

    # Fetch model performance data from the API
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()

            # Extract metrics and predictions
            train_r2 = data['train_r2']
            train_mse = data['train_mse']
            test_r2 = data['test_r2']
            test_mse = data['test_mse']
            y_train_pred = data['y_train_pred']
            y_test_pred = data['y_test_pred']
            y_train = data['y_train']
            y_test = data['y_test']

            # Display performance metrics
            st.write("### Model Performance on Training Data")
            st.write(f"R² Score (Training): {train_r2:.2f}")
            st.write(f"Mean Squared Error (Training): {train_mse:.2f}")
            
            st.write("### Model Performance on Testing Data")
            st.write(f"R² Score (Testing): {test_r2:.2f}")
            st.write(f"Mean Squared Error (Testing): {test_mse:.2f}")

            # Function to plot actual vs predicted values
            def plot_actual_vs_predicted(y_actual, y_pred, dataset_type=""):
                plt.figure(figsize=(8, 6))
                plt.scatter(y_actual, y_pred, alpha=0.5)
                plt.plot([min(y_actual), max(y_actual)], [min(y_actual), max(y_actual)], color='red', lw=2)
                plt.title(f'Actual vs Predicted Sale Prices ({dataset_type} Data)')
                plt.xlabel('Actual Sale Prices')
                plt.ylabel('Predicted Sale Prices')
                st.pyplot(plt.gcf())

            # Plot for training data
            st.write("### Actual vs Predicted - Training Data")
            plot_actual_vs_predicted(y_train, y_train_pred, "Training")

            # Plot for testing data
            st.write("### Actual vs Predicted - Testing Data")
            plot_actual_vs_predicted(y_test, y_test_pred, "Testing")

        else:
            st.write(f"Error: {response.status_code}. Failed to get model performance data from API.")

    except Exception as e:
        st.write(f"Error: {str(e)}")

    st.write(
        """
        ## Insights:
        - The **R² score** for the training data indicates how well the model fits the training set. A higher value (closer to 1) means the model explains a large proportion of the variance in sale prices.
        - The **Mean Squared Error (MSE)** gives an idea of the average squared difference between actual and predicted sale prices. A lower MSE indicates better performance.
        - The **scatter plots** for the training and testing data show how closely the predicted sale prices align with the actual prices. Ideally, the points should lie along the red diagonal line, indicating perfect predictions.
        """
    )


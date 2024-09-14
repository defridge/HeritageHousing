import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

def app():
    st.title("Model Performance Evaluation")

    # Load the necessary data and models
    model = joblib.load('outputs/models/xgb_model.pkl')
    X_train = pd.read_csv('outputs/datasets/collection/X_train.csv')
    y_train = pd.read_csv('outputs/datasets/collection/y_train.csv')
    X_test = pd.read_csv('outputs/datasets/collection/X_test.csv')
    y_test = pd.read_csv('outputs/datasets/collection/y_test.csv')

    st.write(
        """
        ## Model Performance Metrics
        This page provides insights into how well the machine learning models performed on the training and testing datasets.
        """
    )

    def evaluate_model_performance(model, X_train, y_train, X_test, y_test):
        # Predictions for training and testing data
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        # Calculate metrics for training data
        train_r2 = r2_score(y_train, y_train_pred)
        train_mse = mean_squared_error(y_train, y_train_pred)

        # Calculate metrics for testing data
        test_r2 = r2_score(y_test, y_test_pred)
        test_mse = mean_squared_error(y_test, y_test_pred)

        # Display metrics
        st.write("### Model Performance on Training Data")
        st.write(f"R² Score (Training): {train_r2:.2f}")
        st.write(f"Mean Squared Error (Training): {train_mse:.2f}")
        
        st.write("### Model Performance on Testing Data")
        st.write(f"R² Score (Testing): {test_r2:.2f}")
        st.write(f"Mean Squared Error (Testing): {test_mse:.2f}")

        return y_train_pred, y_test_pred

    # Call the function to evaluate model performance
    y_train_pred, y_test_pred = evaluate_model_performance(model, X_train, y_train, X_test, y_test)

    def plot_actual_vs_predicted(y_actual, y_pred, dataset_type=""):
        plt.figure(figsize=(8, 6))
        plt.scatter(y_actual, y_pred, alpha=0.5)
        plt.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], color='red', lw=2)
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

    st.write(
        """
        ## Insights:
        - The **R² score** for the training data indicates how well the model fits the training set. A higher value (closer to 1) means the model explains a large proportion of the variance in sale prices.
        - The **Mean Squared Error (MSE)** gives an idea of the average squared difference between actual and predicted sale prices. A lower MSE indicates better performance.
        - The **scatter plots** for the training and testing data show how closely the predicted sale prices align with the actual prices. Ideally, the points should lie along the red diagonal line, indicating perfect predictions.
        """
    )

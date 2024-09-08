# src/model_evaluation.py

import joblib
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd

def train_linear_regression(X_train, y_train):
    """
    Train a linear regression model.
    :param X_train: pd.DataFrame, training features
    :param y_train: pd.Series, training target
    :return: trained linear regression model
    """
    from sklearn.linear_model import LinearRegression
    
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    return lr_model


def train_random_forest(X_train, y_train):
    """
    Train a random forest regression model.
    :param X_train: pd.DataFrame, training features
    :param y_train: pd.Series, training target
    :return: trained random forest model
    """
    from sklearn.ensemble import RandomForestRegressor
    
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model


def train_xgboost(X_train, y_train):
    """
    Train an XGBoost regression model.
    :param X_train: pd.DataFrame, training features
    :param y_train: pd.Series, training target
    :return: trained XGBoost model
    """
    from xgboost import XGBRegressor
    
    xgb_model = XGBRegressor(n_estimators=100, random_state=42)
    xgb_model.fit(X_train, y_train)
    return xgb_model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model using R² and MSE.
    :param model: trained model
    :param X_test: pd.DataFrame, test features
    :param y_test: pd.Series, test target
    :return: R² and MSE
    """
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    return r2, mse


def save_model(model, model_name):
    """
    Save the trained model to a file.
    :param model: trained model
    :param model_name: str, name for the model file
    """
    joblib.dump(model, f'outputs/models/{model_name}.pkl')


def load_model(model_name):
    """
    Load a trained model from a file.
    :param model_name: str, name of the model file
    :return: loaded model
    """
    return joblib.load(f'outputs/models/{model_name}.pkl')


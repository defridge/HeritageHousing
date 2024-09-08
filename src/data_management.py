# src/data_management.py

import pandas as pd

def load_data(file_path):
    """
    Load the data from a given CSV file path.
    :param file_path: str, path to the dataset CSV file
    :return: pd.DataFrame
    """
    return pd.read_csv(file_path)


def clean_data(df):
    """
    Clean the dataset: Handle missing values and engineer necessary features.
    :param df: pd.DataFrame, raw dataset
    :return: pd.DataFrame, cleaned dataset
    """
    # Fill missing values for numerical columns
    df['EnclosedPorch'].fillna(0, inplace=True)
    df['WoodDeckSF'].fillna(0, inplace=True)
    df['LotFrontage'].fillna(df['LotFrontage'].median(), inplace=True)
    df['GarageFinish'].fillna('No Garage', inplace=True)
    df['GarageYrBlt'].fillna(0, inplace=True)
    df['BsmtFinType1'].fillna('No Basement', inplace=True)
    df['BsmtExposure'].fillna('No Exposure', inplace=True)
    df['BedroomAbvGr'].fillna(df['BedroomAbvGr'].mode()[0], inplace=True)
    df['2ndFlrSF'].fillna(0, inplace=True)
    df['MasVnrArea'].fillna(0, inplace=True)

    # Feature engineering: Create 'TotalSF'
    df['TotalSF'] = df['1stFlrSF'] + df['2ndFlrSF'] + df['TotalBsmtSF']

    # Encode categorical variables
    bsmt_exposure_mapping = {'No': 0, 'Mn': 1, 'Av': 2, 'Gd': 3, 'No Exposure': 4}
    bsmt_fin_type_mapping = {'No Basement': 0, 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6}
    garage_finish_mapping = {'No Garage': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3}
    kitchen_qual_mapping = {'Fa': 0, 'TA': 1, 'Gd': 2, 'Ex': 3}

    df['BsmtExposure'] = df['BsmtExposure'].map(bsmt_exposure_mapping)
    df['BsmtFinType1'] = df['BsmtFinType1'].map(bsmt_fin_type_mapping)
    df['GarageFinish'] = df['GarageFinish'].map(garage_finish_mapping)
    df['KitchenQual'] = df['KitchenQual'].map(kitchen_qual_mapping)

    return df


def get_training_and_test_data(df):
    """
    Split the dataset into training and testing sets.
    :param df: pd.DataFrame, dataset with features and target variable
    :return: X_train, X_test, y_train, y_test
    """
    from sklearn.model_selection import train_test_split

    X = df.drop(columns=['SalePrice'])
    y = df['SalePrice']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

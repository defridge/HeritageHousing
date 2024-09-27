# Heritage Housing

This project aims to help Lydia Doe estimate the sale prices of her inherited houses in Ames, Iowa, using machine learning and data visualization.

Link to deployed app can be found here: **Streamlit App**: [Heritage Housing App](https://heritagehousingpp5-5d67c321f61a.herokuapp.com/)

## Table of Contents

1. [Project Dataset](#project-dataset)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)
4. [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
   - [Epics](#epics)
   - [User Stories](#user-stories)
6. [Actionable Insights from Data Analysis](#actionable-insights-from-data-analysis)
7. [Machine Learning Business Case](#machine-learning-business-case)
8. [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
   - [Page 1: Project Summary](#page-1-project-summary)
   - [Page 2: Data Study](#page-2-data-study)
   - [Page 3: Hypothesis and Analysis](#page-3-hypothesis-and-analysis)
   - [Page 4: Prediction](#page-4-prediction)
   - [Page 5: Model Performance](#page-5-model-performance)
9. [Flask API](#flask-api)
9. [Deployment](#deployment)
10. [Main Data Analysis & Machine Learning Libraries](#main-data-analysis--machine-learning-libraries)
11. [Run Locally](#run-locally)
12. [Credits](#credits)

## Project Dataset

The dataset used for this project is publicly available and sourced from the [Kaggle Ames Housing dataset](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). It contains detailed house features, including sale prices, and is ideal for building predictive models.

### Key Features:
- **1stFlrSF:** First Floor square feet (334 - 4692)
- **2ndFlrSF:** Second floor square feet (0 - 2065)
- **BedroomAbvGr:** Bedrooms above grade (0 - 8)
- **BsmtExposure:** Walkout or garden level walls (Gd: Good, Av: Average, Mn: Minimum, No: No Exposure, None: No Basement)
- **BsmtFinType1:** Rating of basement finished area (GLQ: Good Living Quarters, ALQ: Average Living Quarters, BLQ: Below Average Living Quarters, etc.)
- **TotalBsmtSF:** Total square feet of basement area (0 - 6110)
- **GarageArea:** Size of the garage in square feet (0 - 1418)
- **GarageYrBlt:** Year garage was built (1900 - 2010)
- **GrLivArea:** Above grade (ground) living area square feet (334 - 5642)
- **KitchenQual:** Kitchen quality (Ex: Excellent, Gd: Good, TA: Typical/Average, Fa: Fair, Po: Poor)
- **OverallQual:** Overall quality rating of the house (1-10)
- **YearBuilt:** Year the house was built (1872 - 2010)
- **SalePrice:** Sale price of the house (34900 - 755000)

## Business Requirements

Lydia Doe inherited four properties in Ames, Iowa, and seeks to estimate the sale prices of these properties using historical housing data from Ames.

### Client Expectations:
1. Insight into how house attributes (size, condition, etc.) correlate with sale prices.
2. A predictive model to estimate the sale price of her houses and any other house in Ames.
3. Data visualizations to understand key correlations between features and sale price.

## Hypothesis and Validation

### Hypothesis:

- **GrLivArea:** Larger living areas will result in higher sale prices.
- **TotalSF:** Houses with larger total square footage will sell for higher prices.
- **GarageArea:** The larger the garage, the more likely it is to increase the sale price.
- **YearBuilt:** Newer houses will have higher sale prices, with older houses potentially losing value over time.
- **OverallQual:** Houses with higher overall quality will command higher sale prices.

### Validation:
We will validate this hypothesis by conducting a correlation study using both Spearman and Pearson correlation coefficients.

## The Rationale to Map the Business Requirements to Data Visualizations and ML Tasks

The goal of this project is to help Lydia estimate the sale prices of her inherited houses and to provide insights into the Ames, Iowa housing market. The business requirements are addressed through data visualizations and machine learning tasks, which are structured into distinct epics and user stories.

### Epics:

1. **Data Exploration and Hypothesis Validation**
2. **Data Preparation**
3. **Model Development and Validation**
4. **Dashboard Development and Deployment**

### User Stories:

#### Epic 1: Data Exploration and Hypothesis Validation

1. **User Story:** As a developer, I want to understand the relationship between house attributes and sale prices.
   - **Task:** Conduct data exploration and visualize the relationships between house features and sale prices.

2. **User Story:** As a developer, I want to validate my hypothesis about which factors most affect house prices.
   - **Task:** Use correlation studies (Spearman and Pearson) to validate the hypothesis.

#### Epic 2: Data Preparation

1. **User Story:** As a developer, I want to ensure that the dataset is clean and free from inconsistencies.
   - **Task:** Clean the dataset by handling missing values, outliers, and ensuring data consistency.

2. **User Story:** As a developer, I want to create new features and select the most relevant ones to improve model accuracy.
   - **Task:** Perform feature engineering to create additional features such as `TotalSF` and select key features for modeling.

#### Epic 3: Model Development and Validation

1. **User Story:** As a developer, I want to develop a model that can accurately predict house sale prices.
   - **Task:** Train and evaluate regression models (e.g., XGBoost) to predict sale prices.

2. **User Story:** As a developer, I want to optimize the model’s performance through hyperparameter tuning.
   - **Task:** Use techniques like GridSearchCV to find optimal hyperparameters for the model.

3. **User Story:** As a developer, I want to validate the model’s predictions against real data to ensure accuracy.
   - **Task:** Evaluate the model's performance using R² and mean squared error (MSE), and plot residuals to assess accuracy.

#### Epic 4: Dashboard Development and Deployment

1. **User Story:** As a developer, I want an interactive dashboard where I can visualize data correlations and model predictions.
   - **Task:** Develop an interactive Streamlit dashboard that includes both visualizations and the ability to make live predictions.

2. **User Story:** As a developer, I want the dashboard to be accessible online for easy access to the insights.
   - **Task:** Deploy the Streamlit app on a cloud platform like Heroku and ensure it is accessible to Lydia for real-time use.

## Actionable Insights from Data Analysis

1. **GrLivArea and SalePrice**:
   - There is a strong positive correlation between **GrLivArea** (above-ground living area) and **SalePrice** (correlation of 0.71 Pearson, 0.73 Spearman).
   - Larger houses tend to sell for significantly higher prices.

2. **Total Square Footage and SalePrice**:
   - **TotalSF** (total square footage, including basement) shows a very strong positive correlation with **SalePrice** (correlation of 0.77 Pearson, 0.80 Spearman).
   - Houses with more overall square footage tend to have higher sale prices.

3. **Overall Quality and SalePrice**:
   - **OverallQual** (a measure of the overall quality of the house) is one of the most significant predictors of **SalePrice** (correlation of 0.79 Pearson, 0.80 Spearman).
   - Higher quality ratings are strongly associated with higher sale prices.

4. **Garage Area and SalePrice**:
   - **GarageArea** has a moderate correlation with **SalePrice** (correlation of 0.62 Pearson, 0.66 Spearman).
   - Houses with larger garages tend to fetch higher prices, although the impact is less significant compared to GrLivArea and TotalSF.

5. **Year Built and SalePrice**:
   - **YearBuilt** shows a moderate positive correlation with **SalePrice** (correlation of 0.59 for both Pearson and Spearman).
   - Newer houses tend to sell for more, but older houses with high-quality renovations can still command high sale prices.

## Machine Learning Business Case

The client, Lydia, has inherited several properties in Ames, Iowa, and requires a reliable and accurate model to predict the sale price of these properties. The project objective is to develop a predictive model with an accuracy of at least **75%** (measured by **R²** score) for any house in Ames, including the four inherited houses.

### Machine Learning Task:
The business problem is framed as a **regression task**, where the goal is to predict the continuous target variable `SalePrice` using house attributes. Multiple machine learning models will be used to determine which one performs best for this task.

### XGBoost Model Performance:
- **Training R²**: 0.99
- **Testing R²**: 0.90

The model achieved an **R² score of 0.90** on the testing dataset, exceeding the target of 0.75. This indicates that the model successfully generalizes to unseen data and can make accurate predictions of house sale prices. 

The XGBoost model has been selected as the final model for making predictions on Lydia's inherited houses.

## Dashboard Design (Streamlit App User Interface)

The Streamlit dashboard consists of five pages that address the business requirements and provide a user-friendly interface for Lydia to explore the data, generate insights, and make predictions about house sale prices.

### Page 1: Project Summary
- **Purpose**: This page introduces the project and outlines the business problem, objectives, and key features of the dataset.
- **Content**:
  - Brief overview of the problem Lydia faces and the solution provided.
  - Key dataset features and a summary of how the data was used for analysis and prediction.
  - Explanation of the machine learning model chosen for predictions.
  
### Page 2: Data Study
- **Purpose**: This page provides a detailed exploration of the data used in the project.
- **Content**:
  - Visualizations of key variables such as `GrLivArea`, `TotalSF`, `GarageArea`, and `OverallQual`.
  - Heatmaps showing correlations between features and sale price.
  - Insights derived from these visualizations, addressing Lydia's interest in understanding key factors influencing house prices.

### Page 3: Hypothesis and Analysis
- **Purpose**: This page presents the hypotheses about factors affecting house prices and validates them using data analysis.
- **Content**:
  - Hypotheses regarding the relationship between house attributes and sale price (e.g., larger houses, newer houses, higher quality ratings leading to higher sale prices).
  - Correlation studies (Spearman and Pearson) and visualizations validating these hypotheses.

### Page 4: Prediction
- **Purpose**: This page allows Lydia to input data about her inherited properties or any other properties and receive predicted sale prices.
- **Content**:
  - Form to input house attributes such as `GrLivArea`, `TotalSF`, `GarageArea`, `YearBuilt`, and `OverallQual`.
  - Button to generate the predicted sale price using the machine learning model.
  - Display of the predicted sale price along with an explanation of how the prediction was made.

### Page 5: Model Performance
- **Purpose**: This page shows the performance of the machine learning model used to predict house sale prices.
- **Content**:
  - Model performance metrics such as R² and MSE for both training and testing data.
  - Visualizations of actual vs predicted sale prices.

## Flask API

### Purpose:
The Flask API was developed to offload the heavy machine learning computations, specifically the use of the XGBoost package, to a separate service. This approach helps reduce the slug size of the Streamlit app deployed on Heroku, as the XGBoost package significantly increases the slug size beyond Heroku's 500MB limit.

### Overview:
The Flask API acts as a bridge between the Streamlit dashboard and the machine learning model. When a user inputs house data in the Streamlit app to predict sale prices, the Streamlit app sends a POST request to the Flask API. The Flask API processes the request, runs the prediction using the pre-trained XGBoost model, and returns the result back to the Streamlit app.

### Key Features:
- The Flask API is hosted separately from the Streamlit app and only focuses on handling machine learning predictions to reduce overhead.
- It utilizes the XGBoost model to predict house sale prices based on house attributes like `GrLivArea`, `TotalSF`, `GarageArea`, `YearBuilt`, and `OverallQual`.
- The API allows for seamless interaction with the machine learning model without affecting the performance or deployment size of the Streamlit app.

### Requirements Management:
To accommodate the heavy dependencies of the XGBoost package in the development environment while ensuring a lightweight deployment to Heroku, two `requirements.txt` files are used:
1. **requirements-notebooks.txt** – This file contains all the necessary dependencies for full development, including XGBoost for local training and testing of the machine learning model.
2. **requirements.txt** – This file excludes the XGBoost package, ensuring the Streamlit app remains lightweight during deployment on Heroku. The app uses the Flask API to handle model predictions externally.

By separating the dependencies, the XGBoost package is excluded from the Heroku deployment but is still available for development purposes.

### How It Works:
1. The Streamlit app sends a POST request with house attribute data to the Flask API.
2. The Flask API receives the request, processes the input data, and runs the prediction using the pre-trained XGBoost model.
3. The predicted sale price is returned as a JSON response to the Streamlit app, where it is displayed to the user.
4. The API is designed to be scalable and maintainable, with a simple structure to handle future model updates.

### Link to Flask API Repository:
The full code for the Flask API can be found in the [Flask API Repository](https://github.com/defridge/model.api).

### Summary:
By offloading the XGBoost model and its dependencies to the Flask API, the Streamlit app remains within the Heroku slug size limits while still providing accurate predictions of house sale prices. This setup ensures smooth functionality across both development and deployment environments.

## Deployment

This project involves deploying both the **Streamlit app** and the **Flask API** to Heroku. The two-part deployment was designed to reduce the slug size of the Streamlit app by offloading the heavy XGBoost model to a separate Flask API service.

### Steps to Deploy the Streamlit App:

1. **Create a Heroku Account**:
   - If you don't have one already, create an account at [Heroku](https://heroku.com/).

2. **Set up the GitHub Repository**:
   - Ensure your project is pushed to a GitHub repository.
   - The repository should include:
     - `app.py` for the Streamlit app.
     - `Procfile` to specify the command to run the Streamlit app.
     - `setup.sh` for setting up the configuration for Streamlit.
     - `requirements-notebooks.txt` to include only the lightweight dependencies required for deployment.

3. **Create a Heroku App**:
   - In your Heroku dashboard, click **New** and create a new app.
   - Choose a unique name for your app and select the appropriate region.

4. **Connect Heroku to GitHub**:
   - Go to the **Deploy** tab in your Heroku app.
   - Under **Deployment method**, select **GitHub** and connect your GitHub account.
   - Search for your repository and select it.

5. **Manual Deployment**:
   - To deploy manually, click **Deploy Branch** in the **Deploy** tab.

6. **Slug Size Management**:
   - The Streamlit app uses a separate `requirements-notebooks.txt` file to exclude heavy dependencies such as XGBoost. This keeps the slug size under Heroku’s 500MB limit.

### Steps to Deploy the Flask API:

1. **Set up the Flask API in a Separate Repository**:
   - Create a separate repository for the Flask API. This ensures that the XGBoost package and its dependencies are contained within the API, reducing the size of the Streamlit app.
   - The repository should include:
     - `app.py` to define the Flask API.
     - `requirements.txt` to include all dependencies, including XGBoost.

2. **Create a Heroku App for the Flask API**:
   - In your Heroku dashboard, create a new app specifically for the Flask API.
   - Follow similar steps as described for the Streamlit app.

3. **Deploy the Flask API**:
   - Follow the same steps to connect to GitHub, enable automatic/manual deployments, and manage dependencies.

4. **Connect Streamlit to the Flask API**:
   - Once both the Streamlit app and Flask API are deployed, update the Streamlit app to send POST requests to the deployed Flask API’s URL (e.g., `https://housingmodel-api-6a6b8e797fa2.herokuapp.com/predict`).

### Additional Considerations:

- **Two Requirements Files**:
  - The project uses two `requirements.txt` files to handle dependencies effectively:
    - `requirements-notebooks.txt` (for local development) includes all dependencies, including XGBoost.
    - `requirements.txt` (for Heroku deployment) excludes XGBoost, which is handled by the Flask API.

### Links to Deployed Applications:

- **Streamlit App**: [Deployed Streamlit App](https://heritagehousingpp5-5d67c321f61a.herokuapp.com/)
- **Flask API**: [Deployed Flask API](https://housingmodel-api-6a6b8e797fa2.herokuapp.com/)

By separating the Streamlit app and the Flask API, the deployment size was reduced, and the heavy computations are handled by the API, ensuring smoother performance and faster deployment times.

## Main Data Analysis & Machine Learning Libraries

The project leverages several essential libraries for data manipulation, visualization, and machine learning. Below is a list of the key libraries used in this project:

### Main Data Analysis Libraries:

- **Pandas:**
  - Used for data manipulation and analysis, especially for handling structured data in DataFrames.
  - Key functions: handling missing values, generating summary statistics, and creating new features like `TotalSF`.
  
- **NumPy:**
  - Essential for numerical computing in Python, used for efficient data storage and manipulation.
  - Provides support for large, multi-dimensional arrays and matrices.
  
- **Matplotlib:**
  - A popular library for creating static, interactive, and animated visualizations in Python.
  - Used primarily for generating plots like scatter plots, histograms, and line graphs in this project.

- **Seaborn:**
  - A data visualization library based on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.
  - Used for generating heatmaps and correlation plots to understand relationships between features.

### Main Machine Learning Libraries:

- **Scikit-learn:**
  - Used for splitting the dataset, preprocessing data, and evaluating machine learning models.
  - Key functions include model evaluation metrics like `mean_squared_error` and `r2_score`.
  
- **XGBoost:**
  - A powerful, efficient, and scalable implementation of gradient boosting framework.
  - Utilized for training the regression model to predict house sale prices.
  - Due to its size, it is excluded from the deployed app to avoid increasing slug size but is used during model training and development.

### Other Libraries:

- **Joblib:**
  - Used for saving and loading the trained model efficiently in the `.pkl` format for later use in prediction tasks.
  
- **Flask:**
  - A lightweight web framework used to build the API that communicates between the machine learning model and the Streamlit app.
  
- **Streamlit:**
  - Used to build the interactive web dashboard for visualizing data, making predictions, and displaying model performance metrics.

These libraries were crucial in building an end-to-end machine learning solution, from data preprocessing to model deployment.

## Run Locally

This repository contains the entire process for creating a machine learning model to predict house prices, from data collection and processing to model training, evaluation, and deployment via a Streamlit dashboard.

### To use this repository, follow these steps:

1. **Fork or Clone the Repository**

   First, fork or clone this repository to your local machine:

   ```bash
   git clone https://github.com/defridge/HeritageHousing
   cd HeritageHousing
   ```

2. **Install Dependencies**

   Install the required dependencies by running one of the following commands, depending on your environment:

   For development (including xgboost for model training):

   ```bash
   pip install -r requirements-notebooks.txt
   ```

   For deployment (excluding xgboost to reduce slug size):

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Datasets**

   Register an account with [Kaggle](https://www.kaggle.com/) and create a new API token, download the kaggle.json and place it in the projects root directory.

   If you're using a Jupyter notebook for exploratory analysis or model training, ensure the dataset paths are correct.

4. **Run the Jupyter Notebooks**

   In the development phase, run the Jupyter notebooks in the following order:

   -  **data_collection.ipynb:** Downloads the data from source. Inspects the data and saves to correct folders.

   -  **data_exploration_correlation_study.ipynb:** Preprocesses the dataset, handles missing values, and generates new features such as `TotalSF`.

   - **model_building_and_evaluation.ipynb:** Provides an evaluation of the trained model with key metrics such as R², RMSE, and visualizations of predictions vs actual values.

5. **Run the Streamlit Dashboard**

   Start the Streamlit web app by running the following command:

   ```bash
   streamlit run app.py
   ```

   This will launch the interactive dashboard where you can visualize data, analyze predictions, and see model performance.

## Credits

This project was made possible by the support and guidance of several key resources and contributors. Special thanks to the following:

- **[Kaggle Ames Housing Dataset](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**: For providing the dataset used in this project.
- **[Streamlit documentation](https://docs.streamlit.io/)**: For guiding the development of the interactive web app.
- **[XGBoost documentation](https://xgboost.readthedocs.io/)**: For providing resources on the XGBoost machine learning library, which was used for model training and evaluation.
- **[Heroku documentation](https://devcenter.heroku.com/)**: For deploying both the Streamlit app and Flask API.
- **Code Institute**: For project guidance and structure ideas drawn from past educational resources.
- **[Churnometer repo by Code Institute](https://github.com/Code-Institute-Solutions/churnometer#readme):** For the Readme template/structure.
- **[Walkthrough project 1 - Malaria](https://github.com/Code-Institute-Solutions/WalkthroughProject01/tree/main):** For the code structure and parts of the code for the notebooks. 

All third-party libraries and frameworks used in the project have been credited in the `requirements.txt` and `requirements-notebooks.txt` files.


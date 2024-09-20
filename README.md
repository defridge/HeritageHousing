# Business Understanding (CRISP-DM Phase 1)

We have been approached by Lydia Doe, who has inherited a number of properties (4 in total) from a deceased great-grandfather in Ames, Iowa, USA. Lydia has plenty of knowledge of home pricing in her home country of Belgium, but she is worried that this may not transfer over to the housing market in the USA. Lydia is looking to get an accurate report of what the 4 houses are worth.

### Here’s a breakdown of the business problem:
- **Client:** Lydia Doe, who inherited 4 properties in Ames, Iowa.
- **Objective:** Help Lydia estimate the sale prices of these properties based on historical data from Ames.
- **Why this is important:** Lydia doesn’t want to risk inaccurate estimates and potential financial loss.

### Client Expectations:
- Insight into how house attributes (size, condition, etc.) correlate with sale prices.
- A predictive model to predict the sale price of her houses and any other house in Ames.
- Data visualizations to understand key correlations between features and sale price.

# Data Understanding (CRISP-DM Phase 2)

In this phase, we focus on exploring and understanding the dataset provided for predicting house prices in Ames, Iowa. The dataset includes various features that describe the properties, such as square footage, number of bedrooms, quality ratings, and more.

### Dataset Source:
The dataset used in this project is publicly available and sourced from the [Kaggle Ames Housing dataset](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). It contains detailed house features, including sale prices, and is ideal for building predictive models.

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

### CRISP-DM Process Overview:
1. **Business Understanding:** Help Lydia price her inherited properties using historical housing data from Ames, Iowa.
2. **Data Understanding:** Explore key features of the dataset, including house size, quality, and year built.
3. **Data Preparation:** Handle missing values, encode categorical variables, and create additional features such as TotalSF.
4. **Modeling:** Develop regression models to predict sale prices.
5. **Evaluation:** Test model performance using R² and MSE, ensuring it meets the required 75% accuracy.
6. **Deployment:** Build an interactive dashboard using Streamlit for user-friendly predictions.

---

# Hypothesis and Validation

### Hypothesis:
Based on research in the real estate domain and existing knowledge, several factors are believed to significantly influence the sale price of a house:

- **Overall Quality:** Houses with higher quality materials and finishes will command higher sale prices.
- **Total Square Footage:** Larger houses will generally sell for more.
- **Bedrooms and Bathrooms:** The number of bedrooms and bathrooms impacts the sale price.
- **Kitchen and Bathroom Condition:** Newly renovated kitchens and bathrooms significantly increase sale price.
- **Year Built:** Newer houses tend to have higher sale prices, but older houses with renovations can still maintain value.

### Validation:
We will validate this hypothesis by conducting a correlation study using both Spearman and Pearson correlation coefficients.

---

# Rationale: Mapping Business Requirements to Data Visualizations and ML Tasks

The purpose of this project is to help Lydia Doe estimate the sale prices of her inherited houses and to provide her with insights into the housing market in Ames, Iowa. The project is structured into distinct tasks that directly address these business requirements using data analysis, visualization, and machine learning (ML) models.

### Business Requirement 1: Understanding House Attributes and Sale Prices

Lydia needs insights into how various house attributes (such as square footage, garage area, and year built) correlate with house sale prices. The following actions were taken:

1. **Data Exploration and Initial Analysis:**
   - We loaded and explored the dataset to identify any missing values, outliers, and data inconsistencies.
   - Correlation studies (Pearson and Spearman) were conducted to identify the most relevant features that impact sale price.
   - Visualizations such as scatter plots and heatmaps were generated to provide Lydia with an intuitive understanding of key relationships.

   **ML Mapping:**
   - These actions directly inform the feature selection process for the machine learning model. The insights derived from this analysis guide the selection of relevant features such as `GrLivArea`, `TotalSF`, `GarageArea`, and `OverallQual`.

---

# Actionable Insights from Data Analysis

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

---

# Machine Learning Business Case

### Business Requirement 2:
The client, Lydia, has inherited several properties in Ames, Iowa, and requires a reliable and accurate model to predict the sale price of these properties. The project objective is to develop a predictive model with an accuracy of at least **75%** (measured by **R²** score) for any house in Ames, including the four inherited houses.

### Machine Learning Task:
The business problem is framed as a **regression task**, where the goal is to predict the continuous target variable `SalePrice` using house attributes. Multiple machine learning models will be used to determine which one performs best for this task.

---

# Machine Learning Model Performance

The primary objective of the machine learning model is to predict the sale price of houses in Ames, Iowa, with at least 75% accuracy (measured by **R² score**).

### XGBoost Model Performance:
- **Training R²**: 0.99
- **Testing R²**: 0.90

The model achieved an **R² score of 0.90** on the testing dataset, exceeding the target of 0.75. This indicates that the model successfully generalizes to unseen data and can make accurate predictions of house sale prices. 

The XGBoost model has been selected as the final model for making predictions on Lydia's inherited houses.

---

# User Stories and Epics

The project development process was driven by user stories that reflect Lydia’s business needs and map directly to actionable tasks within the project. Here’s a breakdown of the major user stories and their connection to the tasks:

### Epic 1: Data Exploration and Hypothesis Validation
1. **User Story:** *As a developer, I want to understand the relationship between house attributes and sale prices.*
   - This user story covers the initial data exploration process, ensuring that all relevant house attributes are analyzed to identify how they impact sale price.

2. **User Story:** *As a developer, I want to validate my hypothesis about which factors most affect house prices.*
   - This user story is focused on hypothesis validation, using exploratory data analysis and visualizations to confirm which house attributes (e.g., `OverallQual`, `GrLivArea`, `YearBuilt`) most affect sale prices.

### Epic 2: Data Preparation
1. **User Story:** *As a developer, I want to ensure that the dataset is clean and free from inconsistencies.*
   - This story addresses the data cleaning process, ensuring the dataset is properly prepared for modeling by handling missing values, outliers, and inconsistencies.

2. **User Story:** *As a developer, I want to create new features and select the most relevant ones to improve model accuracy.*
   - This story involves feature engineering, where new features (e.g., `TotalSF`) are created and key features are selected to optimize the machine learning model.

### Epic 3: Model Development and Validation
1. **User Story:** *As a developer, I want to develop a model that can accurately predict house sale prices.*
   - The focus of this story is on training different regression models and evaluating them using key performance metrics (R², RMSE, MAE).

2. **User Story:** *As a developer, I want to optimize the model’s performance through hyperparameter tuning.*
   - This user story ensures that the machine learning models are tuned to achieve maximum performance, meeting the 75% accuracy goal.

3. **User Story:** *As a developer, I want to validate the model’s predictions against real data to ensure accuracy.*
   - This story focuses on evaluating the model’s predictions, comparing predicted prices with actual sale prices, and plotting residuals to ensure accuracy.

### Epic 4: Dashboard Development and Deployment
1. **User Story:** *As a developer, I want an interactive dashboard where I can visualize data correlations and model predictions.*
   - This user story drives the creation of the Streamlit dashboard, ensuring it includes both correlation visualizations and model predictions.

2. **User Story:** *As a developer, I want the dashboard to be accessible online for easy access to the insights.*
   - This story ensures the dashboard is deployed on a cloud platform (e.g., Heroku) and made accessible to Lydia for real-time use.


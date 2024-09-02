## Business Understanding (CRISP-DM Phase 1)
We have been appracohed by Lydia Doe who has inherated a number of properties (4 in total) from a deceased great grand-father in Ames, Iowa, USA. Lydia has plenty of knowledge of home pricing in her home country of Belgium but is worried this may not transfer over to the housing market in the USA and is looking to get an accurate report of what the 4 houses are worth.

### Here’s a breakdown of the business problem:
- **Client**: Lydia Doe, who inherited 4 properties in Ames, Iowa.
- **Objective**: Help Lydia estimate the sale prices of these properties based on historical data from Ames.
- **Why this is important**: Lydia doesn’t want to risk inaccurate estimates and potential financial loss. 
- **Client Expectations**:
  - **Insight into how house attributes (size, condition, etc.) correlate with sale prices.**
  - **A predictive model**: To predict the sale price of her houses and any other house in Ames.
  - **Data visualizations**: To understand key correlations between features and sale price.


## Data Understanding (CRISP-DM Phase 2)
In this phase, we focus on exploring and understanding the dataset provided for predicting house prices in Ames, Iowa. The dataset includes various features that describe the properties, such as square footage, number of bedrooms, quality ratings, and more. Below is an overview of the key features and their corresponding descriptions:

- **1stFlrSF**: First Floor square feet
  - Range: 334 - 4692

- **2ndFlrSF**: Second floor square feet
  - Range: 0 - 2065

- **BedroomAbvGr**: Bedrooms above grade (does NOT include basement bedrooms)
  - Range: 0 - 8

- **BsmtExposure**: Refers to walkout or garden level walls
  - Categories:
    - Gd: Good Exposure
    - Av: Average Exposure
    - Mn: Minimum Exposure
    - No: No Exposure
    - None: No Basement

- **BsmtFinType1**: Rating of basement finished area
  - Categories:
    - GLQ: Good Living Quarters
    - ALQ: Average Living Quarters
    - BLQ: Below Average Living Quarters
    - Rec: Average Rec Room
    - LwQ: Low Quality
    - Unf: Unfinished
    - None: No Basement

- **BsmtFinSF1**: Type 1 finished square feet
  - Range: 0 - 5644

- **BsmtUnfSF**: Unfinished square feet of basement area
  - Range: 0 - 2336

- **TotalBsmtSF**: Total square feet of basement area
  - Range: 0 - 6110

- **GarageArea**: Size of garage in square feet
  - Range: 0 - 1418

- **GarageFinish**: Interior finish of the garage
  - Categories:
    - Fin: Finished
    - RFn: Rough Finished
    - Unf: Unfinished
    - None: No Garage

- **GarageYrBlt**: Year garage was built
  - Range: 1900 - 2010

- **GrLivArea**: Above grade (ground) living area square feet
  - Range: 334 - 5642

- **KitchenQual**: Kitchen quality
  - Categories:
    - Ex: Excellent
    - Gd: Good
    - TA: Typical/Average
    - Fa: Fair
    - Po: Poor

- **LotArea**: Lot size in square feet
  - Range: 1300 - 215245

- **LotFrontage**: Linear feet of street connected to property
  - Range: 21 - 313

- **MasVnrArea**: Masonry veneer area in square feet
  - Range: 0 - 1600

- **EnclosedPorch**: Enclosed porch area in square feet
  - Range: 0 - 286

- **OpenPorchSF**: Open porch area in square feet
  - Range: 0 - 547

- **OverallCond**: Rates the overall condition of the house
  - Categories:
    - 10: Very Excellent
    - 9: Excellent
    - 8: Very Good
    - 7: Good
    - 6: Above Average
    - 5: Average
    - 4: Below Average
    - 3: Fair
    - 2: Poor
    - 1: Very Poor

- **OverallQual**: Rates the overall material and finish of the house
  - Categories:
    - 10: Very Excellent
    - 9: Excellent
    - 8: Very Good
    - 7: Good
    - 6: Above Average
    - 5: Average
    - 4: Below Average
    - 3: Fair
    - 2: Poor
    - 1: Very Poor

- **WoodDeckSF**: Wood deck area in square feet
  - Range: 0 - 736

- **YearBuilt**: Original construction date
  - Range: 1872 - 2010

- **YearRemodAdd**: Remodel date (same as construction date if no remodeling or additions)
  - Range: 1950 - 2010

- **SalePrice**: Sale Price
  - Range: 34900 - 755000

This dataset provides a comprehensive view of various factors that could potentially influence the sale price of a house in Ames, Iowa. Understanding these features is crucial for building a predictive model that accurately estimates house prices based on these attributes.

## Hypothesis and Validation

### Hypothesis

Based on research in the real estate domain and existing knowledge, several factors are believed to significantly influence the sale price of a house. These factors can be broadly categorized into external and internal attributes:

- **External Factors**: 
  - Location is typically the most critical factor affecting sale price. Proximity to public transportation, grocery stores, and educational institutions also plays a crucial role.
  
  However, since our dataset does not include location-based data for properties in Ames, Iowa, we are unable to validate this aspect.

- **Internal Factors**: The following attributes are hypothesized to have the greatest impact on house prices:
  - Overall quality of the house.
  - Total square footage.
  - Number of bedrooms and bathrooms.
  - Condition of the kitchen and bathroom, with newly renovated spaces often significantly increasing the sale price.
  - Year of construction.

### Validation

- The hypothesis will be validated through a correlation study using both Spearman and Pearson correlation coefficients.

---

## Rationale for Mapping Business Requirements to Data Visualizations and Machine Learning Tasks

### Business Requirement 1:
- **Objective**: Investigate the relationship between house attributes and sale prices.
  - **Actions**:
    - Conduct a detailed correlation study using both Spearman and Pearson methods.
    - Visualize the strength of correlations with sale price.
    - Generate plots for the variables that show the highest correlations with sale price to derive actionable insights.

### Business Requirement 2:
- **Objective**: Develop a machine learning model to predict the sale price of Lydia's four inherited houses and any house in Ames, Iowa, with at least 75% accuracy.
  - **Actions**:
    - Employ a variety of machine learning algorithms to identify the best-performing model.
    - Perform extensive hyperparameter tuning to optimize the model's performance and ensure it meets the accuracy threshold.

---

## Machine Learning Business Case

**1. Business Requirements**:
- The client seeks to understand how various house attributes correlate with sale prices. This requires data visualizations showing these correlations.
- Additionally, the client needs a predictive model to estimate the sale prices of her four inherited houses and other properties in Ames, Iowa.

**2. Can conventional data analysis address any business requirements?**
- Yes, conventional data analysis can be used to explore and visualize how house attributes correlate with sale prices.

**3. What is the preferred output: a dashboard or an API?**
- The client requires a dashboard for interactive exploration of the data and model predictions.

**4. What defines a successful project outcome for the client?**
- A detailed study highlighting the most significant variables correlated with sale price.
- A reliable predictive model for estimating the sale price of both inherited and other houses in Ames, Iowa.

**5. Can the project be divided into Epics and User Stories?**
- Yes, the project can be broken down as follows:
  - Gathering and collecting data.
  - Data visualization, cleaning, and preparation.
  - Training, optimizing, and validating the model.
  - Planning, designing, and developing the dashboard.
  - Deploying and releasing the dashboard.

**6. Are there any ethical or privacy concerns?**
- No, the dataset is publicly available and free of ethical or privacy concerns.

**7. Does the data suggest a specific type of model?**
- The data indicates that a regression model, with the sale price as the target variable, is appropriate.

**8. What are the model’s inputs and outputs?**
- **Inputs**: House attributes.
- **Outputs**: Predicted sale price.

**9. What are the performance criteria for the model?**
- The model should achieve an R2 score of at least 0.75 on both the training and testing sets.

**10. How will the client benefit?**
- The client will be able to maximize the sale price of the inherited properties by using insights from the correlation study and the predictions from the machine learning model.

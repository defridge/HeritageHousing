import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("Hypothesis and Analysis")

    st.write("### Hypothesis and Validation")
    st.write(
        "After analyzing the available data and exploring key attributes, "
        "I formulated the following hypothesis regarding house prices."
    )
    
    st.write("**Key Parameters Considered in the Hypothesis:**")
    st.write(
        "- **GrLivArea**: Above grade (ground) living area square feet\n"
        "- **TotalSF**: Total square footage (including basement)\n"
        "- **GarageArea**: Size of the garage in square feet\n"
        "- **YearBuilt**: Year the house was built\n"
        "- **OverallQual**: Overall quality rating of the house (scale of 1-10)\n"
    )

    st.write("---")
    st.write("**Hypothesis**")
    st.write(
        "Based on the key features, I hypothesize that the following factors "
        "have the greatest influence on house sale prices:\n\n"
        "- **GrLivArea**: Larger living areas will result in higher sale prices.\n\n"
        "- **TotalSF**: Houses with larger total square footage will sell for higher prices.\n\n"
        "- **GarageArea**: The larger the garage, the more likely it is to increase the sale price.\n\n"
        "- **YearBuilt**: Newer houses will have higher sale prices, with older houses potentially losing value over time.\n\n"
        "- **OverallQual**: Houses with higher overall quality will command higher sale prices."
    )

    st.write("---")
    
    st.write("**Validation**")
    st.write(
        "We validate the hypothesis by performing a Correlation Study, "
        "analyzing how each key feature correlates with the sale price."
    )

    st.write(
        "**The Correlation study confirms the following:**\n\n"
        "- **GrLivArea** shows a strong positive correlation with sale prices, "
        "confirming that houses with larger living areas tend to sell for more.\n\n"
        "- **TotalSF** also shows a positive correlation, further validating "
        "that overall square footage is a key factor in sale prices.\n\n"
        "- **GarageArea** has a moderate positive correlation with sale prices, "
        "confirming that garage size plays a role, but not as strongly as living space.\n\n"
        "- **YearBuilt** shows a moderate correlation, confirming that newer houses "
        "generally sell for more, but older houses with better quality or renovations "
        "may still have high values.\n\n"
        "- **OverallQual** has one of the strongest correlations with sale prices, "
        "confirming that houses with higher quality ratings consistently command higher prices."
    )

    # Load the dataset
    df = pd.read_csv('outputs/datasets/collection/HousePricing_cleaned.csv')

    # Plotting the correlation heatmap for the key attributes
    st.write("### Correlation Heatmap")
    key_attributes = ['GrLivArea', 'TotalSF', 'GarageArea', 'YearBuilt', 'OverallQual', 'SalePrice']
    correlation_matrix = df[key_attributes].corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Matrix of Key Features with Sale Price")
    st.pyplot(plt.gcf())

    # Scatter plot for GrLivArea vs SalePrice
    st.write("### GrLivArea vs SalePrice")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['GrLivArea'], y=df['SalePrice'])
    plt.title('GrLivArea vs SalePrice')
    plt.xlabel('GrLivArea')
    plt.ylabel('SalePrice')
    st.pyplot(plt.gcf())

    # Scatter plot for TotalSF vs SalePrice
    st.write("### TotalSF vs SalePrice")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['TotalSF'], y=df['SalePrice'])
    plt.title('TotalSF vs SalePrice')
    plt.xlabel('TotalSF')
    plt.ylabel('SalePrice')
    st.pyplot(plt.gcf())

    # Scatter plot for GarageArea vs SalePrice
    st.write("### GarageArea vs SalePrice")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['GarageArea'], y=df['SalePrice'])
    plt.title('GarageArea vs SalePrice')
    plt.xlabel('GarageArea')
    plt.ylabel('SalePrice')
    st.pyplot(plt.gcf())

    # Scatter plot for YearBuilt vs SalePrice
    st.write("### YearBuilt vs SalePrice")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['YearBuilt'], y=df['SalePrice'])
    plt.title('YearBuilt vs SalePrice')
    plt.xlabel('YearBuilt')
    plt.ylabel('SalePrice')
    st.pyplot(plt.gcf())

    # Bar plot for OverallQual vs SalePrice
    st.write("### OverallQual vs SalePrice")
    plt.figure(figsize=(8, 6))
    sns.barplot(x=df['OverallQual'], y=df['SalePrice'], errorbar=None)
    plt.title('OverallQual vs SalePrice')
    plt.xlabel('OverallQual')
    plt.ylabel('SalePrice')
    st.pyplot(plt.gcf())

    st.write("---")

    # Add a section that refers to Business Requirements
    st.write("**Business Requirements and Stakeholder Alignment**")
    st.write(
        """
        This hypothesis directly aligns with the key business requirements of the project:
        
        1. **Discovering how house attributes correlate with sale prices**: The features selected in the hypothesis, such as living area, total square footage, garage area, and overall quality, are identified as critical variables that stakeholders believe have a direct impact on sale price. By validating these features, we can provide meaningful insights and data-driven recommendations for decision-making.
        
        2. **Providing accurate sale price predictions**: The correlation analysis of the selected features ensures that the machine learning model can deliver accurate predictions based on attributes that matter most to the business. This alignment ensures that the model addresses stakeholder needs and maximizes the relevance of predictions.
        """
    )

    # Validation and Conclusion Section
    st.write("---")
    st.write("### Validation of Hypothesis")
    st.write(
        """
        The correlation analysis validates the initial hypothesis to a significant degree. 
        The most important findings are:
        - **GrLivArea** and **TotalSF** are strongly correlated with `SalePrice`, confirming that larger houses tend to sell for more.
        - **GarageArea** has a moderate influence on sale prices, but its effect is not as strong as living area and total square footage.
        - **YearBuilt** has a positive correlation, but older houses with high-quality materials can still fetch a high sale price.
        - **OverallQual** is one of the most significant predictors of `SalePrice`, with higher-quality houses consistently commanding higher prices.
        """
    )

    st.write("---")
    st.write("### Conclusion")
    st.write(
        """
        The hypothesis that larger houses, better quality, newer build, and larger garages positively impact house sale prices is largely validated. 
        Among the factors, **OverallQual** and **GrLivArea** have the strongest relationships with house prices. 
        This insight will be valuable when focusing on key features for building predictive models and providing recommendations for the real estate market.
        """
    )
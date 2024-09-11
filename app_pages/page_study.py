import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("Data Study")

    # Load the datasets
    df = pd.read_csv('outputs/datasets/collection/HousePricing.csv')
    inherited_houses = pd.read_csv('outputs/datasets/collection/InheritedHouses.csv')
    cleaned_data = pd.read_csv('outputs/datasets/collection/HousePricing_cleaned.csv')

    st.write("### Dataset Overview")
    st.write("This page provides a detailed study of the housing dataset, exploring key attributes and their relationships with the sale price.")

    st.write("### Key Terms and Variables")
    st.write(
        """
        **Key Variables Explained:**
        - **SalePrice**: The sale price of the house.
        - **GrLivArea**: Above grade (ground) living area square feet.
        - **TotalSF**: Total square footage (first floor + second floor + basement).
        - **GarageArea**: Size of the garage in square feet.
        - **YearBuilt**: The year the house was built.
        - **OverallQual**: Rates the overall material and finish of the house on a scale of 1-10.
        """
    )

    # Show dataset and data description
    if st.checkbox("View raw dataset"):
        st.write(df)

    st.write("### Summary Statistics")
    st.write("Let's look at the summary statistics of the dataset to understand its key features and distributions.")
    st.write(df.describe())

    # Correlation Matrix
    st.write("### Correlation Matrix")
    st.write(
        "The correlation matrix shows the linear relationship between the different variables in the dataset. "
        "A positive correlation indicates that as one variable increases, the other tends to increase as well. "
        "A negative correlation suggests the opposite relationship."
    )
    
    corr_matrix = cleaned_data.corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    st.pyplot(plt.gcf())

    st.write(
        """
        **Key Correlations:**
        - `GrLivArea`, `TotalSF`, and `OverallQual` are highly positively correlated with `SalePrice`, indicating that larger and higher-quality houses tend to have higher sale prices.
        - `YearBuilt` has a moderate positive correlation with `SalePrice`, suggesting newer houses generally sell for more.
        - Interestingly, `GarageArea` also shows a positive correlation, but to a lesser extent, indicating that a larger garage may add value to a property.
        """
    )

    # Key attributes - Scatter plots
    st.write("### Key Attribute Visualizations")
    st.write("Below, we explore how some key features relate to the `SalePrice` using scatter plots.")

    key_attributes = ['GrLivArea', 'TotalSF', 'GarageArea', 'YearBuilt']
    plt.figure(figsize=(15, 12))

    for i, attribute in enumerate(key_attributes, 1):
        plt.subplot(2, 2, i)
        sns.scatterplot(x=cleaned_data[attribute], y=df['SalePrice'])
        plt.title(f'SalePrice vs {attribute}')
        plt.xlabel(attribute)
        plt.ylabel('SalePrice')
        

    plt.tight_layout()
    st.pyplot(plt.gcf())

    st.write(
        """
        **Insights from Scatter Plots:**
        - Houses with larger living areas (`GrLivArea`) and total square footage (`TotalSF`) tend to have higher sale prices.
        - There is a positive relationship between the `GarageArea` and `SalePrice`, though the effect is less pronounced compared to other attributes.
        - Newer houses (`YearBuilt`) generally sell for more, but there are exceptions, as houses with higher-quality materials (captured by `OverallQual`) can still fetch a high price even if older.
        """
    )

    # Interactive filter - for YearBuilt and SalePrice range
    st.write("### Interactive Data Exploration")
    st.write("Use the filters below to explore how `SalePrice` changes with `YearBuilt`.")

    year_range = st.slider("Select Year Range", int(df["YearBuilt"].min()), int(df["YearBuilt"].max()), (1900, 2020))
    filtered_df = df[(df["YearBuilt"] >= year_range[0]) & (df["YearBuilt"] <= year_range[1])]

    st.write(f"Displaying houses built between {year_range[0]} and {year_range[1]}.")
    st.write(filtered_df[['YearBuilt', 'SalePrice']])

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=filtered_df['YearBuilt'], y=filtered_df['SalePrice'])
    plt.title('SalePrice vs YearBuilt (Filtered)')
    plt.xlabel('YearBuilt')
    plt.ylabel('SalePrice')
    st.pyplot(plt.gcf())

    st.write(
        "The filtered scatter plot allows you to observe how the sale price of houses changes "
        "depending on the year they were built within the selected range."
    )

    st.write("### Inherited Houses Data Overview")
    st.write(
        "Finally, let's take a quick look at the four inherited houses' data, which will be used for price prediction later in the project."
    )

    st.write(inherited_houses)

    st.write("---")
    st.write("This concludes the data study section. The insights gained here will be valuable for predictive modeling and understanding the relationships between house attributes and sale prices.")



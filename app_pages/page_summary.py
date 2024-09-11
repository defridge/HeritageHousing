import streamlit as st

def app():
    st.title("Heritage Hosuing")

    st.header("Project Summary")
    
    st.header("Objective")
    st.write("""
    The objective of this project is to develop a machine learning model that predicts the sale price of the clients inherited houses, as well as any house in Ames, Iowa, with at least 75% accuracy.
    """)
    
    st.header("Business Requirements")
    st.write("""
    1. Investigate the relationship between house attributes and sale prices.
    2. Develop a machine learning model to predict the sale price of Lydia's four inherited houses and any house in Ames, Iowa, with at least 75% accuracy.
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
    st.write(
        "**For better understanding and interpretation, you can view the complete metadata below.**"
    )
    
    if st.checkbox("View complete metadata"):
        st.write(
            "- **2ndFlrSF**: Second floor square feet.\n"
            "- **BedroomAbvGr**: Bedrooms above grade (does NOT include basement bedrooms).\n"
            "- **BsmtExposure**: Refers to walkout or garden level walls.\n"
            "   - **Gd**: Good Exposure\n"
            "   - **Av**: Average Exposure\n"
            "   - **Mn**: Minimum Exposure\n"
            "   - **No**: No Exposure\n"
            "   - **No Basement**: No Basement\n"
            "- **BsmtFinType1**: Rating of basement finished area.\n"
            "   - **GLQ**: Good Living Quarters\n"
            "   - **ALQ**: Average Living Quarters\n"
            "   - **BLQ**: Below Average Living Quarters\n"
            "   - **Rec**: Average Rec Room\n"
            "   - **LwQ**: Low Quality\n"
            "   - **Unf**: Unfinished\n"
            "   - **No Basement**: No Basement\n"
            "- **BsmtFinSF1**: Type 1 finished square feet.\n"
            "- **BsmtUnfSF**: Unfinished square feet of basement area.\n"
            "- **GarageFinish**: Interior finish of the garage.\n"
            "   - **Fin**: Finished\n"
            "   - **RFn**: Rough Finished\n"
            "   - **Unf**: Unfinished\n"
            "   - **No Garage**: No Garage\n"
            "- **KitchenQual**: Kitchen quality.\n"
            "   - **Ex**: Excellent\n"
            "   - **Gd**: Good\n"
            "   - **TA**: Typical/Average\n"
            "   - **Fa**: Fair\n"
            "   - **Po**: Poor\n"
            "- **LotFrontage**: Linear feet of street connected to property.\n"
            "- **MasVnrArea**: Masonry veneer area in square feet.\n"
            "- **OpenPorchSF**: Open porch area in square feet.\n"
            "- **OverallCond**: Rates the overall condition of the house (scale from 1 to 10).\n"
            "- **YearRemodAdd**: Remodel date (same as construction date if no remodeling or additions).\n"
            "- **SalePrice**: Sale price of the house.\n"
        )
    st.write("---")

    st.write(
        "To view the dataset with all the information, click here: "
        "[Housing Prices Dataset](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)."
    )
    st.write(
        "*For additional information, please visit and **read** the "
        "[Project README file](https://github.com/defridge/HeritageHousing/blob/main/README.md).*"
    )

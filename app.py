import streamlit as st
from app_pages.multipage import MultiPage
from app_pages import page_summary, page_study, page_prediction, page_model_performance, page_hypothesis

# Initialize the multipage app
app = MultiPage()

# Add pages to the app
app.add_page("Project Summary", page_summary.app)
app.add_page("Data Study", page_study.app)
app.add_page("Hypothesis and Analysis", page_hypothesis.app)
app.add_page("Prediction", page_prediction.app)
app.add_page("Model Performance", page_model_performance.app)


# Run the app
app.run()

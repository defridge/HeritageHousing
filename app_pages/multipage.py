import streamlit as st

# A class to manage multiple Streamlit app pages
class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        """Adds a page to the app
        Parameters
        ----------
        title: str
            The title of the page
        func: function
            The function that runs the page
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        # Display the dropdown to select the page
        page = st.sidebar.selectbox('Navigation', self.pages, format_func=lambda page: page['title'])
        # Run the selected page's function
        page['function']()

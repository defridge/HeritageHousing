#!/bin/bash

# Ensure correct requirements file is used
echo "Installing dependencies from requirements_prod.txt..."
pip install -r requirements_prod.txt

# Create the Streamlit configuration directory
mkdir -p ~/.streamlit/

# Create the Streamlit config file
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

echo "Setup complete. Streamlit configuration written to ~/.streamlit/config.toml"

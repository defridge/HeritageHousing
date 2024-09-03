import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import streamlit as st

print("All packages imported successfully!")

# Load a sample dataset from seaborn for testing
df = sns.load_dataset('iris')
print(df.head())

# Plot the data to ensure matplotlib works
sns.pairplot(df, hue='species')
plt.show()

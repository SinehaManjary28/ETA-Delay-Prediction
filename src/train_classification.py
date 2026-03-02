# ---------------------------------------
# Import required libraries
# ---------------------------------------

import pandas as pd

# Train-test split
from sklearn.model_selection import train_test_split

# Encoding + preprocessing pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Baseline model
from sklearn.ensemble import RandomForestClassifier

# Evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ---------------------------------------
# Load preprocessed dataset
# ---------------------------------------

df = pd.read_csv("../data/processed/processed_data.csv")

print("Dataset Loaded:", df.shape)

# ---------------------------------------
# Load preprocessed dataset
# ---------------------------------------

df = pd.read_csv("../data/processed/processed_data.csv")

print("Dataset Loaded:", df.shape)


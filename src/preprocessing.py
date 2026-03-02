# src/preprocessing.py

import pandas as pd
import numpy as np

def load_data(path):
    """
    Load dataset from given path
    """
    df = pd.read_csv(path)
    return df
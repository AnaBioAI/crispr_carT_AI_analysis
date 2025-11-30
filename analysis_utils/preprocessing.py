import pandas as pd
import numpy as np

def load_counts(path):
    """Load raw count matrix from CSV."""
    return pd.read_csv(path, index_col=0)

def log1p_transform(counts):
    """Return log1p(counts)."""
    return np.log1p(counts)

def filter_low_expression(counts, min_cpm=1, min_samples=3):
    """Basic CPM filter to remove unexpressed genes."""
    lib_sizes = counts.sum(axis=1)
    cpm = counts.divide(lib_sizes, axis=0) * 1e6
    keep = (cpm > min_cpm).sum(axis=1) >= min_samples
    return counts.loc[keep]

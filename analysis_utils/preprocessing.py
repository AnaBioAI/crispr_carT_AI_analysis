import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def run_pca(expr_logcpm, n_components=5, random_state=0):
    """
    Run PCA on log-normalized expression matrix.

    expr_logcpm: DataFrame (genes x samples)
    Returns: fitted PCA object and DataFrame of PC scores (samples x PCs).
    """
    # Transpose to samples x genes
    X = expr_logcpm.T

    scaler = StandardScaler(with_mean=True, with_std=True)
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=n_components, random_state=random_state)
    X_pca = pca.fit_transform(X_scaled)

    pcs_df = pd.DataFrame(
        X_pca,
        index=expr_logcpm.columns,
        columns=[f"PC{i+1}" for i in range(n_components)]
    )
    return pca, pcs_df

def gene_loadings(pca, genes_index):
    """
    Return gene loadings for each PC as a DataFrame (genes x PCs).
    """
    comps = pca.components_  # shape: (n_PCs x n_genes)
    loadings = {
        f"PC{i+1}": pd.Series(comps[i], index=genes_index)
        for i in range(comps.shape[0])
    }
    return pd.DataFrame(loadings)

def assign_quadrant(pc1, pc2):
    """
    Assign a quadrant based on PC1 and PC2 loading signs.
    Q1: PC1>=0, PC2>=0
    Q2: PC1<0,  PC2>=0
    Q3: PC1<0,  PC2<0
    Q4: PC1>=0, PC2<0
    """
    if pc1 >= 0 and pc2 >= 0:
        return "Q1"
    if pc1 < 0 and pc2 >= 0:
        return "Q2"
    if pc1 < 0 and pc2 < 0:
        return "Q3"
    return "Q4"

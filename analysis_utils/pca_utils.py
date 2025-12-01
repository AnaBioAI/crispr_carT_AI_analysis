from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np


def run_pca(expr_logcpm: pd.DataFrame, n_components: int = 5, random_state: int = 0):
    """
    Run PCA on an expression matrix (genes × samples, log-transformed).

    Returns
    -------
    pca : PCA object
    pcs_df : DataFrame of PCs (samples × PCs)
    """
    X = expr_logcpm.T  # samples × genes
    scaler = StandardScaler(with_mean=True, with_std=True)
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=n_components, random_state=random_state)
    X_pca = pca.fit_transform(X_scaled)

    pcs_df = pd.DataFrame(
        X_pca,
        index=expr_logcpm.columns,
        columns=[f"PC{i+1}" for i in range(n_components)],
    )
    return pca, pcs_df


def gene_loadings(pca: PCA, genes_index) -> pd.DataFrame:
    """
    Return gene loadings for each PC as a DataFrame (genes × PCs).
    """
    comps = pca.components_  # (PCs × genes)
    loadings = {
        f"PC{i+1}": pd.Series(comps[i], index=genes_index)
        for i in range(comps.shape[0])
    }
    return pd.DataFrame(loadings)


def assign_quadrant(pc1: float, pc2: float) -> str:
    """
    Assign point in PC1–PC2 space to quadrant label.
    """
    if pc1 >= 0 and pc2 >= 0:
        return "Q1"
    if pc1 < 0 and pc2 >= 0:
        return "Q2"
    if pc1 < 0 and pc2 < 0:
        return "Q3"
    return "Q4"

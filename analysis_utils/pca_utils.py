# analysis_utils/pca_utils.py

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# -----------------------------
# Core PCA helpers (your original functions)
# -----------------------------

def run_pca(
    expr_logcpm: pd.DataFrame,
    n_components: int = 5,
    random_state: int = 0,
):
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


# -----------------------------
# New helpers for Module D
# -----------------------------

def ensure_dir(path: str):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def assign_quadrants_scores(
    scores_df: pd.DataFrame,
    pc_x: str = "PC1",
    pc_y: str = "PC2",
    column_name: str | None = None,
) -> pd.DataFrame:
    """
    Assign quadrants to each sample based on its scores on (pc_x, pc_y).
    Adds a new categorical column and returns a copy.
    """
    if column_name is None:
        column_name = f"quadrant_{pc_x}_{pc_y}"

    df = scores_df.copy()
    df[column_name] = [
        assign_quadrant(x, y) for x, y in zip(df[pc_x], df[pc_y])
    ]
    return df


def assign_quadrants_loadings(
    loadings_df: pd.DataFrame,
    pc_x: str = "PC1",
    pc_y: str = "PC2",
    column_name: str | None = None,
) -> pd.DataFrame:
    """
    Assign quadrants to each gene based on its loadings on (pc_x, pc_y).
    Adds a new categorical column and returns a copy.
    """
    if column_name is None:
        column_name = f"quadrant_{pc_x}_{pc_y}"

    df = loadings_df.copy()
    df[column_name] = [
        assign_quadrant(x, y) for x, y in zip(df[pc_x], df[pc_y])
    ]
    return df


def run_pca_and_save(
    expr_logcpm: pd.DataFrame,
    out_dir: str,
    n_components: int = 20,
    random_state: int = 0,
    assign_quadrants: bool = True,
    quadrant_pcs: tuple[str, str] = ("PC1", "PC2"),
):
    """
    High-level helper for Module D.

    - Runs PCA on expr_logcpm
    - Computes sample scores and gene loadings
    - Optionally assigns quadrants in (PC1, PC2) space
    - Saves results to CSVs in `out_dir`:
        * pca_scores.csv
        * pca_loadings.csv
        * pca_explained_variance.csv

    Returns
    -------
    scores_df, loadings_df, explained_df
    """
    ensure_dir(out_dir)

    # Use your original run_pca to keep backward compatibility
    pca, scores_df = run_pca(
        expr_logcpm=expr_logcpm,
        n_components=n_components,
        random_state=random_state,
    )

    loadings_df = gene_loadings(pca, genes_index=expr_logcpm.index)

    pc_names = [f"PC{i+1}" for i in range(pca.n_components_)]
    explained_df = pd.DataFrame({
        "PC": pc_names,
        "explained_variance": pca.explained_variance_,
        "explained_variance_ratio": pca.explained_variance_ratio_,
    })

    if assign_quadrants:
        pc_x, pc_y = quadrant_pcs
        scores_df = assign_quadrants_scores(scores_df, pc_x=pc_x, pc_y=pc_y)
        loadings_df = assign_quadrants_loadings(loadings_df, pc_x=pc_x, pc_y=pc_y)

    # Save
    scores_df.to_csv(os.path.join(out_dir, "pca_scores.csv"))
    loadings_df.to_csv(os.path.join(out_dir, "pca_loadings.csv"))
    explained_df.to_csv(os.path.join(out_dir, "pca_explained_variance.csv"))

    return scores_df, loadings_df, explained_df

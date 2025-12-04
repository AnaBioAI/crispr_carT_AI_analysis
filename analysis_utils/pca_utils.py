"""
pca_utils.py

Core PCA utilities for the CRISPR CAR-T AI analysis project.

Responsibilities
----------------
- Run PCA on logCPM expression matrices (genes x samples)
- Return scores (samples x PCs), loadings (genes x PCs),
  and explained-variance summary
- Assign quadrants in PC space for interpretability
- Save standard PCA outputs to disk

Assumptions
-----------
- Input expression matrices are log-transformed counts (e.g. logCPM)
- Rows   = genes
- Columns = samples (cells / bulk libraries)

This module is intentionally *stateless*: it does not depend on
project-specific config, so it’s easy to reuse.
"""

from __future__ import annotations

import os
from typing import Tuple, Optional

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


# ---------------------------------------------------------------------
# Generic utilities
# ---------------------------------------------------------------------


def ensure_dir(path: str) -> None:
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


# ---------------------------------------------------------------------
# PCA core
# ---------------------------------------------------------------------


def run_pca(
    expr_logcpm: pd.DataFrame,
    n_components: int = 20,
    center: bool = True,
    scale: bool = False,
    random_state: int = 0,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, PCA]:
    """
    Run PCA on a logCPM expression matrix.

    Parameters
    ----------
    expr_logcpm:
        DataFrame of shape (n_genes, n_samples).
        Index   = gene IDs
        Columns = sample IDs

    n_components:
        Number of principal components to compute.

    center:
        Whether to manually mean-center features (genes).
        PCA from scikit-learn already centers by default, but this hook
        is kept for explicitness and potential future tweaks.

    scale:
        Whether to scale genes to unit variance before PCA.
        For logCPM with comparable dispersion, `scale=False` is usually
        appropriate. Set to True if you want each gene to contribute
        equally regardless of variance.

    random_state:
        Random seed for PCA (for reproducible sign conventions when
        using randomized SVD under the hood).

    Returns
    -------
    scores_df:
        DataFrame of shape (n_samples, n_components).
        Rows = samples; Columns = PC1..PCn.

    loadings_df:
        DataFrame of shape (n_genes, n_components).
        Rows = genes; Columns = PC1..PCn.
        Each entry is the loading (weight) of a gene on a PC.

    explained_df:
        DataFrame with columns:
            - "PC"
            - "explained_variance"
            - "explained_variance_ratio"

    pca:
        The fitted sklearn PCA object (for projecting new data, etc.).
    """
    # X will be samples x genes (as required by sklearn PCA)
    X = expr_logcpm.T  # (n_samples, n_genes)

    # Centering
    if center:
        X = X - X.mean(axis=0)

    # Optional scaling
    if scale:
        # Use pandas ops to preserve column alignment
        std = X.std(axis=0)
        # Avoid division by zero
        std_replaced = std.replace(0, 1.0)
        X = X / std_replaced

    pca = PCA(
        n_components=n_components,
        random_state=random_state,
    )
    scores = pca.fit_transform(X)  # (n_samples, n_components)

    pc_names = [f"PC{i + 1}" for i in range(pca.n_components_)]

    scores_df = pd.DataFrame(
        scores,
        index=expr_logcpm.columns,  # sample IDs
        columns=pc_names,
    )

    loadings = pca.components_.T  # (n_genes, n_components)
    loadings_df = pd.DataFrame(
        loadings,
        index=expr_logcpm.index,  # gene IDs
        columns=pc_names,
    )

    explained_df = pd.DataFrame(
        {
            "PC": pc_names,
            "explained_variance": pca.explained_variance_,
            "explained_variance_ratio": pca.explained_variance_ratio_,
        }
    )

    return scores_df, loadings_df, explained_df, pca


# ---------------------------------------------------------------------
# Quadrant helpers
# ---------------------------------------------------------------------


def _assign_quadrant(x: float, y: float) -> str:
    """
    Assign (x, y) to a quadrant label in the usual Cartesian sense.

    Q1: x >= 0, y >= 0
    Q2: x <  0, y >= 0
    Q3: x <  0, y <  0
    Q4: x >= 0, y <  0
    """
    if x >= 0 and y >= 0:
        return "Q1"
    if x < 0 and y >= 0:
        return "Q2"
    if x < 0 and y < 0:
        return "Q3"
    return "Q4"


def assign_quadrants_scores(
    scores_df: pd.DataFrame,
    pc_x: str = "PC1",
    pc_y: str = "PC2",
    column_name: Optional[str] = None,
) -> pd.DataFrame:
    """
    Add a quadrant label to each sample based on (pc_x, pc_y).

    Parameters
    ----------
    scores_df:
        DataFrame of PCA scores (samples x PCs).

    pc_x, pc_y:
        Names of the PCs to use as x / y axes.

    column_name:
        Name of the new column to add. If None, a default name
        "quadrant_{pc_x}_{pc_y}" is used.

    Returns
    -------
    DataFrame copy with an extra categorical column of quadrant labels.
    """
    if column_name is None:
        column_name = f"quadrant_{pc_x}_{pc_y}"

    df = scores_df.copy()
    df[column_name] = [
        _assign_quadrant(x, y) for x, y in zip(df[pc_x], df[pc_y])
    ]
    return df


def assign_quadrants_loadings(
    loadings_df: pd.DataFrame,
    pc_x: str = "PC1",
    pc_y: str = "PC2",
    column_name: Optional[str] = None,
) -> pd.DataFrame:
    """
    Add a quadrant label to each gene based on (pc_x, pc_y) loadings.

    Parameters
    ----------
    loadings_df:
        DataFrame of PCA loadings (genes x PCs).

    pc_x, pc_y:
        Names of the PCs to use as x / y axes.

    column_name:
        Name of the new column to add. If None, a default name
        "quadrant_{pc_x}_{pc_y}" is used.

    Returns
    -------
    DataFrame copy with an extra categorical column of quadrant labels.
    """
    if column_name is None:
        column_name = f"quadrant_{pc_x}_{pc_y}"

    df = loadings_df.copy()
    df[column_name] = [
        _assign_quadrant(x, y) for x, y in zip(df[pc_x], df[pc_y])
    ]
    return df


# ---------------------------------------------------------------------
# High-level convenience wrapper
# ---------------------------------------------------------------------


def run_pca_and_save(
    expr_logcpm: pd.DataFrame,
    out_dir: str,
    n_components: int = 20,
    center: bool = True,
    scale: bool = False,
    random_state: int = 0,
    assign_quadrants: bool = True,
    quadrant_pcs: Tuple[str, str] = ("PC5", "PC6"),
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, PCA]:
    """
    Run PCA, optionally assign quadrants, and save outputs to CSVs.

    Parameters
    ----------
    expr_logcpm:
        Expression matrix (genes x samples), logCPM.

    out_dir:
        Directory where PCA outputs will be written.

    n_components, center, scale, random_state:
        Passed through to `run_pca`.

    assign_quadrants:
        Whether to add quadrant labels to scores and loadings.

    quadrant_pcs:
        Pair of PC names used for quadrant computation
        (e.g. ("PC5", "PC6") for effector vs regulatory axes).

    Saves
    -----
        out_dir/pca_scores.csv
        out_dir/pca_loadings.csv
        out_dir/pca_explained_variance.csv

    Returns
    -------
    scores_df, loadings_df, explained_df, pca
    """
    ensure_dir(out_dir)

    scores_df, loadings_df, explained_df, pca = run_pca(
        expr_logcpm=expr_logcpm,
        n_components=n_components,
        center=center,
        scale=scale,
        random_state=random_state,
    )

    if assign_quadrants:
        pc_x, pc_y = quadrant_pcs
        scores_df = assign_quadrants_scores(scores_df, pc_x=pc_x, pc_y=pc_y)
        loadings_df = assign_quadrants_loadings(loadings_df, pc_x=pc_x, pc_y=pc_y)

    scores_path = os.path.join(out_dir, "pca_scores.csv")
    loadings_path = os.path.join(out_dir, "pca_loadings.csv")
    explained_path = os.path.join(out_dir, "pca_explained_variance.csv")

    scores_df.to_csv(scores_path)
    loadings_df.to_csv(loadings_path)
    explained_df.to_csv(explained_path)

    return scores_df, loadings_df, explained_df, pca

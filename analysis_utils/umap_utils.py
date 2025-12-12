# analysis_utils/umap_utils.py

import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
import umap

from .config_utils import ensure_dirs  # relative import inside the package


def compute_sample_umap(
    expr_logcpm: pd.DataFrame,
    metadata: pd.DataFrame | None = None,
    metadata_cols: list[str] | None = None,
    n_hvg: int = 2000,
    n_neighbors: int = 10,
    min_dist: float = 0.3,
    metric: str = "euclidean",
    random_state: int | None = 42,
) -> tuple[pd.DataFrame, umap.UMAP]:
    """
    Compute UMAP on samples using logCPM expression.

    Parameters
    ----------
    expr_logcpm
        DataFrame of shape (n_genes, n_samples), logCPM or log1p normalized.
    metadata
        Optional DataFrame indexed by sample IDs with extra columns.
    metadata_cols
        Optional list of metadata column names to attach to the resulting UMAP.
        If None and metadata is provided, no extra columns are added.
    n_hvg
        Number of highly variable genes to keep.
    n_neighbors, min_dist, metric, random_state
        UMAP hyperparameters.

    Returns
    -------
    umap_df
        DataFrame with columns ["UMAP1", "UMAP2"] and optional metadata.
        Index = sample IDs.
    umap_model
        Fitted umap.UMAP object.
    """
    # 1) Select highly variable genes
    gene_var = expr_logcpm.var(axis=1)
    hvg = gene_var.sort_values(ascending=False).head(n_hvg).index
    expr_hvg = expr_logcpm.loc[hvg]  # genes x samples

    # 2) Build sample matrix
    X_samples = expr_hvg.T  # samples x genes

    # 3) Scale features
    scaler = StandardScaler(with_mean=True, with_std=True)
    X_scaled = scaler.fit_transform(X_samples)

    # 4) UMAP
    umap_model = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        metric=metric,
        random_state=random_state,
    )
    X_umap = umap_model.fit_transform(X_scaled)

    # 5) Build output DataFrame
    umap_df = pd.DataFrame(
        X_umap,
        index=X_samples.index,
        columns=["UMAP1", "UMAP2"],
    )

    # 6) Attach metadata if provided
    if metadata is not None and metadata_cols is not None:
        cols_to_add = [c for c in metadata_cols if c in metadata.columns]
        if cols_to_add:
            umap_df = umap_df.join(metadata[cols_to_add], how="left")

    return umap_df, umap_model


def save_sample_umap(
    umap_df: pd.DataFrame,
    out_dir: Path,
    base_name: str = "sample_umap",
) -> Path:
    """
    Save sample UMAP coordinates to CSV in out_dir.

    Returns
    -------
    coords_path : Path to the saved CSV file.
    """
    ensure_dirs(out_dir)
    coords_path = out_dir / f"{base_name}_coordinates.csv"
    umap_df.to_csv(coords_path)
    return coords_path

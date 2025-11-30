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

functions & helper scripts
We don’t have to write everything now, but we can sketch the main ones:
preprocessing.py (Module A)
import pandas as pd
import numpy as np

def load_counts(path):
    return pd.read_csv(path, index_col=0)

def filter_low_expression(counts, min_cpm=1, min_samples=3):
    # simple CPM-like filter
    lib_sizes = counts.sum(axis=0)
    cpm = counts.divide(lib_sizes, axis=1) * 1e6
    keep = (cpm > min_cpm).sum(axis=1) >= min_samples
    return counts.loc[keep]

def log1p_counts(counts):
    return np.log1p(counts)
pca_utils.py (Module D)
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

def run_pca(expr_logcpm, n_components=5, random_state=0):
    X = expr_logcpm.T  # samples × genes
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
    comps = pca.components_  # (PCs × genes)
    loadings = {
        f"PC{i+1}": pd.Series(comps[i], index=genes_index)
        for i in range(comps.shape[0])
    }
    return pd.DataFrame(loadings)

def assign_quadrant(pc1, pc2):
    if pc1 >= 0 and pc2 >= 0: return "Q1"
    if pc1 < 0  and pc2 >= 0: return "Q2"
    if pc1 < 0  and pc2 < 0:  return "Q3"
    return "Q4"
umap_utils.py, de_utils.py, pathway_utils.py can then wrap the code we’ve already written in the notebook into functions.

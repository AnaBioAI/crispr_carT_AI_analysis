# analysis_utils/config_utils.py

import os
import json
from pathlib import Path

# ---------------------------------------------------------------------
# Base directory of the project (folder that contains analysis_utils, data, results, etc.)
# ---------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pathlib-style project root
PROJECT_ROOT = Path(BASE_DIR)

# Core data directories
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"  # use later if needed

# Results directories
RESULTS_DIR = PROJECT_ROOT / "results"
PCA_RESULTS_DIR = RESULTS_DIR / "pca"
MODULE_RESULTS_DIR = RESULTS_DIR / "modules"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# ---------------------------------------------------------------------
# Gene set utilities
# ---------------------------------------------------------------------
DEFAULT_GENE_SET_PATH = os.path.join(BASE_DIR, "data", "gene_sets", "gene_sets.json")


def load_gene_sets(path=None):
    """
    Load gene sets from a JSON file.

    Parameters
    ----------
    path : str or None
        Optional path to the gene set JSON file.
        If None, uses data/gene_sets/gene_sets.json at the project root.

    Returns
    -------
    gene_sets : dict
        Dictionary mapping category name -> list of gene symbols.
    """
    if path is None:
        path = DEFAULT_GENE_SET_PATH

    if not os.path.exists(path):
        raise FileNotFoundError(f"Gene set file not found at: {path}")

    with open(path, "r") as f:
        gene_sets = json.load(f)

    return gene_sets


def ensure_dirs(*paths):
    """Create directories if they don't exist."""
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)
 

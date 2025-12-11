import os
import json

# Base directory of the project (folder that contains analysis_utils, data, results, etc.)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

# analysis_utils/config_utils.py

from pathlib import Path

# Path to project root:
# analysis_utils/config_utils.py

from pathlib import Path

# Path to project root (this file lives inside <root>/analysis_utils/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"

RESULTS_DIR = PROJECT_ROOT / "results"
PCA_RESULTS_DIR = RESULTS_DIR / "pca"
MODULE_RESULTS_DIR = RESULTS_DIR / "modules"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

def ensure_dirs(*paths):
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)

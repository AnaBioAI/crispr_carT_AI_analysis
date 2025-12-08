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



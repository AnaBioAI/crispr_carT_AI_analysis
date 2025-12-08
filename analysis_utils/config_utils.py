import os
import json


def load_config(config_path=None):
    """
    Load config.json from the project root by default.
    """
    if config_path is None:
        # <project_root>/analysis_utils/config_utils.py -> go up twice -> project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(project_root, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, "r") as f:
        cfg = json.load(f)

    return cfg

import json
import os

def load_gene_sets(path="data/gene_sets/gene_sets.json"):
    with open(path, "r") as f:
        return json.load(f)


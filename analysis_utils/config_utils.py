import os
import json
from typing import Any, Dict


def get_project_root() -> str:
    """
    Return the absolute path to the project root directory.
    Assumes this file lives in <project_root>/analysis_utils/.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config(config_path: str | None = None) -> Dict[str, Any]:
    """
    Load the JSON config file.

    If config_path is None, it will look for 'config.json'
    in the project root directory.
    """
    if config_path is None:
        project_root = get_project_root()
        config_path = os.path.join(project_root, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, "r") as f:
        cfg = json.load(f)

    return cfg

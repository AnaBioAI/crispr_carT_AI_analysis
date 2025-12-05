# Systematic discovery of CRISPR-boosted CAR T cell immunotherapies — Reproduction & Extension

This repository reproduces and extends the analysis from *Seki et al., Nature 2023*, integrating CRISPR functional genomics and single-cell RNA-seq to explore CAR-T activation mechanisms.

## Project Structure
## Goals
1. Reproduce key scRNA-seq visualizations and cluster annotations.
2. Train machine-learning models to classify CAR-T activation states.
3. Perform pathway enrichment to identify biological mechanisms of improved potency.

## Tools
Python, Scanpy, Scikit-learn, TensorFlow, Seaborn, gseapy, JupyterLab.

## Author
**Ana Castano, M.D.**  
Translational Immunologist & AI Researcher
### Module D – PCA interpretability

Notebooks:
- `notebooks/Notebooks03_pca_analysis/03_pca_analysis.ipynb`

Core code:
- `analysis_utils/pca_utils.py`

Outputs:
- `results/pca/pca_scores.csv` – sample-level PC coordinates (+ quadrants on PC5/PC6)
- `results/pca/pca_loadings.csv` – gene-level loadings for each PC
- `results/pca/pca_explained_variance.csv` – variance explained per PC
### Quick workflow

```bash
conda activate crispr_carT_env
cartlab                # jump to project root
make modules           # recompute module scores + trajectories
gcsave "Update module pipeline results"

That turns your CRISPR CAR-T analysis from “fragile notebook magic” into a real, reproducible pipeline with:

- A smarter shell
- Git guardrails
- Data-size sanity checks
- LFS for big binary outputs
- A Makefile to standardize how you run things

That’s pretty close to a 5-star computational lab. Next upgrade tier is when we start wiring CI (GitHub Actions) to auto-run unit tests on your utils and maybe generate nightly plots of CAR-T effector vs regulatory drifts.

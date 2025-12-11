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
You are building:
THE Analysis Package
for your “CRISPR-CAR-T AI Atlas.”
Let’s organize it into modules:
 
🧩 Module A — Preprocessing & Metadata
•	counts matrix alignment
•	symbol mapping
•	gene filtering (min expression)
•	PCA matrix + variance explained
•	metadata dictionary
This becomes a reusable “stage 1” file.
 
🧩 Module B — Differential Expression
•	volcano
•	top up/down lists
•	annotated gene tables
•	pathway enrichment of DEGs
 
🧩 Module C — Hallmark Pathways
•	per-timepoint heatmaps
•	per-pathway GSEA curves
•	correlation to PCs
•	summarized pathway scores
 
🧩 Module D — PCA Interpretability
•	loadings (PC1 / PC2)
•	quadrant classification
•	quadrant gene lists
•	quadrant visualizations
•	RHOG vs SafeHarbor trajectory plot
•	biological axis interpretation (IL2/STAT5 vs IFN)
 
🧩 Module E — RHOG-specific Comparisons
•	PCA divergence
•	pathway divergence
•	gene program shifts (quadrant-wise)
•	signature synthesis

![Figure 1 – CRISPR CAR-T analysis pipeline](figures/fig1_crispr_cart_pipeline_schematic.svg)

**Figure 1.** Overview of the CRISPR CAR-T perturbation analysis pipeline, from raw counts and metadata through normalization, PCA, UMAP, differential expression, Hallmark pathway integration, and RHOG vs SafeHarbor trajectory analysis.

**CRISPR CAR-T Activation Atlas**

_A reproducible computational pipeline for PCA, UMAP, differential expression, pathway integration, and perturbation trajectory analysis in CRISPR-engineered CAR-T cells.

Overview

Overview

This repository implements a modular, manuscript-aligned analysis pipeline for dissecting transcriptional programs underlying CAR-T cell activation across a multi-day time course and genetic perturbation (RHOG knockout vs SafeHarbor control).

The pipeline integrates:
	•	transcriptomic normalization and gene symbol harmonization
	•	principal component analysis (PCA) with biological interpretation
	•	UMAP embeddings for nonlinear structure
	•	differential expression (DE) testing
	•	Hallmark pathway enrichment and module scoring
	•	perturbation-specific trajectory analysis

All intermediate and final outputs are version-controlled, reproducible, and saved with stable filenames to support figure regeneration and manuscript assembly.

⸻

Scientific Questions
	•	What transcriptional programs dominate CAR-T activation across time?
	•	How do interferon, effector, proliferative, and metabolic pathways relate to major axes of variance?
	•	Does RHOG knockout alter activation trajectories without introducing new cell states?
	•	How do pathway-level programs align with PCA-defined manifolds?

⸻

Repository Structure

project_root/
├── analysis_utils/
│   ├── config_utils.py        # Centralized paths & directory creation
│   ├── preprocessing.py       # Normalization & symbol mapping (Module A)
│   ├── de_utils.py            # Differential expression (Module B)
│   ├── pathway_utils.py       # Hallmark enrichment & module scoring (Module C)
│   ├── pca_utils.py           # PCA computation & biological interpretation (Module D)
│   └── umap_utils.py          # UMAP pipelines (Module extension)
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── expr_logcpm.parquet
│       ├── expr_logcpm_symbol.parquet
│       └── metadata_samples.csv
│
├── results/
│   ├── pca/
│   ├── de/
│   ├── pathways/
│   └── umap/
│
├── notebooks/
│   ├── A01_crispr_cart_pca_summary.ipynb
│   ├── A02_sample_umap.ipynb
│   ├── A03_gene_umap.ipynb
│   ├── A04_quadrant_projections.ipynb
│   ├── A05_hallmark_pathways.ipynb
│   └── B01_late_vs_early_DE_and_pathways.ipynb
│
├── figures/
│   ├── fig1_pipeline/
│   ├── fig2_activation_trajectories/
│   └── fig3_rhog_perturbation/
│
└── README.md
⸻

Analysis Modules

Module A — Preprocessing & Metadata

Question: How are raw CAR-T RNA-seq data normalized and harmonized?
	•	logCPM normalization
	•	ENSG → gene symbol mapping
	•	duplicate symbol collapsing
	•	canonical processed matrices

Outputs:
expr_logcpm.parquet, expr_logcpm_symbol.parquet, metadata_samples.csv

⸻

Module B — Differential Expression

Question: Which genes distinguish early vs late activation and RHOG perturbation?
	•	linear modeling of gene expression
	•	time-matched contrasts
	•	volcano plots and DE tables

Outputs:
DE tables and volcano figures under results/de/

⸻

Module C — Hallmark Pathways

Question: Which biological programs define CAR-T activation states?
	•	MSigDB Hallmark enrichment
	•	direction-aware gene sets
	•	per-sample pathway module scoring
	•	PC–pathway correlations

Outputs:
Enrichment tables, barplots, and heatmaps under results/pathways/

⸻

Module D — PCA Interpretability

Question: What biology defines the dominant axes of variance?
	•	PCA computation and explained variance
	•	biological annotation of PC axes
	•	trajectory analysis across time and perturbation

Key findings:
	•	PC1: IL-2/STAT5 & NF-κB effector activation ↔ interferon-driven activation
	•	PC2: interferon stress ↔ proliferative E2F/OxPhos programs

⸻

Module E — RHOG-specific Comparisons

Question: Does RHOG knockout bias activation trajectories?
	•	RHOG vs SafeHarbor overlays in PCA and UMAP
	•	pathway-level modulation without new state formation

⸻

Manuscript Figures

Figure 1 — Analysis Pipeline (Panels A–C)

Conceptual overview of preprocessing, dimensionality reduction, and differential expression workflows.
Source: figures/fig1_pipeline/

Figure 2 — Activation Trajectories (Panels D1–D2)
	•	D1: PCA activation trajectories (RHOG vs SafeHarbor)
	•	D2: Hallmark pathway module heatmap across time

Sources:
results/pca/, results/pathways/ → assembled in figures/fig2_activation_trajectories/

⸻

Reproducibility
	•	All paths centralized in config_utils.py
	•	Intermediate results saved to disk
	•	Figures generated directly from stored outputs
	•	No manual copy-paste steps required

⸻

Status

The pipeline is currently in the figure-locking and manuscript assembly phase.
Core analyses are complete and stabilized; remaining work focuses on figure curation, caption finalization, and narrative integration.

⸻

Authors

Ana Castano, M.D.
ChatGPT 🧠
Axolotl 🦎 (moral support & resilience)
_______________________________________________________________________________________________
⸻


## Notebook Index (Manuscript-aligned)

**A00 (implicit)** – Preprocessing & metadata checks  
**A01** – PCA summary and biological interpretation  
**A02** – Sample-level UMAP embedding  
**A03** – Gene-level UMAP  
**A04** – PCA quadrant projections  
**A05** – Hallmark pathway module scoring and heatmaps  

---

## Design Philosophy

	•	analysis_utils/ contains reusable, testable functions.
	•	notebooks/ serve as narrative, figure-producing entry points.
	•	results/ stores all intermediate and final outputs with stable filenames.
	•	Figures are regenerated directly from saved results — no manual copy-paste.

This structure ensures clarity, reproducibility, and long-term maintainability.

⸻

---

## Reproducibility Notes

	•	All paths are centralized in analysis_utils/config_utils.py
	•	Intermediate tables and figures are saved automatically
	•	Analyses can be rerun end-to-end using the notebooks in order
	•	No interactive steps are required to reproduce figures
---

## Status

---

## Manuscript Figures & Panels
figures/
├── fig1_pipeline/
├── fig2_activation_trajectories/
└── figX_*/

This analysis pipeline is organized to generate manuscript-ready figures.
Each panel corresponds to one or more notebooks and result artifacts.

### Panel A — Data & Preprocessing
**Question:** How were CRISPR CAR-T RNA-seq data normalized and harmonized?
- Raw counts normalization (logCPM)
- ENSG → gene symbol mapping and collapsing
- Canonical processed expression matrices
- Reproducible metadata alignment

**Source:** Module A (`analysis_utils/preprocessing.py`)

---

### Panel B — Dimensionality Reduction (PCA & UMAP)
**Question:** What are the dominant activation trajectories of CAR-T cells?
- PCA of samples with biologically annotated axes
- Time-ordered activation trajectories
- Sample-level UMAP embeddings

**Notebooks:**  
- `A01_crispr_cart_pca_summary.ipynb`  
- `A02_sample_umap.ipynb`

---

### Panel C — Differential Expression
**Question:** Which genes distinguish early vs late CAR-T activation?
- Linear modeling of gene expression
- Volcano plots (Late vs Early; RHOG vs SafeHarbor)
- Direction-aware gene selection

**Notebook:**  
- `B01_late_vs_early_DE_and_pathways.ipynb`

---

### Panel D — Pathways & Module Scores
**Question:** Which biological programs define CAR-T activation states?
- Hallmark pathway enrichment (MSigDB)
- Per-sample pathway module scores
- Hallmark–PC correlations
- Pathway heatmaps ordered by time and guide

**Notebook:**  
- `A05_hallmark_pathways.ipynb`

---

### Panel E — Trajectories & Perturbations (RHOG vs SafeHarbor)
**Question:** How does RHOG knockout modulate CAR-T activation trajectories?
- Overlay of RHOG vs SafeHarbor in PCA space
- Trajectory shifts without new cluster formation
- Pathway-level interpretation of perturbation effects

**Notebooks:**  
- `A01_crispr_cart_pca_summary.ipynb`  
- `A05_hallmark_pathways.ipynb`

---

### Panel F (Optional) — Reproducibility & Outputs
**Question:** How are results stored and reused?
- Versioned result tables
- Saved figures
- Modular utilities enabling reuse and extension

**Folders:**  
- `results/`
- `analysis_utils/`

Each figure folder contains:
	•	panel layouts (.pptx)
	•	final image exports (.png, .svg)
	•	caption text (figX_captions.md)

## Authors
**Ana Castano, M.D.**  
Translational Immunologist & AI Researcher

ChatGPT
Computational analysis, pipeline architecture, and scientific integration

Axolotl
Morale, curiosity, and regenerative inspiration 🦎




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

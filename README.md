![Figure 1 – CRISPR CAR-T analysis pipeline](figures/fig1_crispr_cart_pipeline_schematic.svg)

**Figure 1.** Overview of the CRISPR CAR-T perturbation analysis pipeline, from raw counts and metadata through normalization, PCA, UMAP, differential expression, Hallmark pathway integration, and RHOG vs SafeHarbor trajectory analysis.

🧬 CRISPR CAR-T Activation Atlas
A reproducible computational pipeline for PCA, UMAP, differential expression, pathway integration, and perturbation trajectory analysis
Overview
This repository implements a modular analysis pipeline for dissecting CRISPR-based perturbations in human CAR-T cell activation across a 0–168h time course.
The pipeline integrates:
transcriptomic normalization & symbol harmonization
PCA variance decomposition and biological interpretation
UMAP embeddings for nonlinear manifold structure
differential expression (DE) comparisons
Hallmark pathway enrichment & PC–pathway alignment
perturbation-specific trajectory analysis (e.g., RHOG vs SafeHarbor)
All outputs are reproducible, version-controlled, and saved under standardized directories (results/pca, results/pathways, results/umap, etc.).
This repository contains a reproducible analysis pipeline for the transcriptomic
characterization of CRISPR-perturbed CAR-T cells across activation time courses.

The pipeline integrates preprocessing, differential expression, dimensionality
reduction, pathway scoring, and trajectory analysis to interpret how genetic
perturbations (e.g. RHOG knockout) modulate CAR-T activation, interferon responses,
proliferation, and metabolic programs.

The analysis is structured to support figure generation for a manuscript-style
presentation and emphasizes clarity, reproducibility, and biological interpretability.

---

## Analysis Modules and Biological Questions

**Module A — Preprocessing & Metadata**  
*How can raw CRISPR CAR-T RNA-seq data be normalized and harmonized for reproducible downstream analysis?*  
- Normalization (logCPM)
- Gene ID harmonization (ENSG → gene symbols)
- Symbol collapsing
- Canonical processed expression matrices and metadata

**Module B — Differential Expression**  
*Which genes and pathways distinguish early vs late CAR-T activation and RHOG vs SafeHarbor perturbations?*  
- Linear modeling of gene expression
- Early vs Late activation contrasts
- RHOG vs SafeHarbor contrasts
- Volcano plots and DE result tables

**Module C — Hallmark Pathways**  
*Which biological programs drive CAR-T activation dynamics?*  
- Hallmark pathway enrichment (MSigDB)
- Direction-aware gene set construction
- Pathway module scoring
- PC–pathway correlations

**Module D — PCA Interpretability**  
*How do CAR-T samples traverse activation trajectories in low-dimensional space, and what biology defines each axis?*  
- PCA computation and explained variance
- Biological annotation of PC axes
- Time-ordered trajectories in PC space
- Integration with pathway scores

**Module E — RHOG-specific Comparisons**  
*Does RHOG knockout modulate CAR-T activation trajectories without creating new cell states?*  
- Overlay of RHOG vs SafeHarbor in PCA and UMAP
- Trajectory comparisons across time
- Pathway-level interpretation of RHOG effects

---

## Repository Structure

project_root/
├── analysis_utils/
│   ├── config_utils.py        # Project paths, directory creation
│   ├── preprocessing.py       # Normalization, symbol mapping (Module A)
│   ├── de_utils.py             # Differential expression (Module B)
│   ├── pathway_utils.py        # Enrichment + Hallmark scoring (Module C)
│   ├── pca_utils.py            # PCA computation + biological plotting (Module D)
│   └── umap_utils.py           # UMAP pipelines (Module extension)
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
│   │   ├── hallmark_enrichment_late_vs_early_UP.csv
│   │   ├── hallmark_enrichment_late_vs_early_DOWN.csv
│   │   ├── hallmark_barplot_late_vs_early_UP.png
│   │   ├── hallmark_barplot_late_vs_early_DOWN.png
│   │   ├── hallmark_module_scores_per_sample.csv
│   │   ├── hallmark_module_scores_heatmap.png
│   │   ├── hallmark_pc_correlations_PC1_PC2.csv
│   │   └── hallmark_pc_correlations_PC1_PC2_heatmap.png
│   └── umap/
│
├── notebooks/
│   ├── A01_crispr_cart_pca_summary.ipynb
│   ├── A02_sample_umap.ipynb
│   ├── A03_gene_umap.ipynb
│   ├── A04_quadrant_projections.ipynb
│   ├── A05_hallmark_pathways.ipynb
│   └── B01_late_vs_early_DE_and_pathways.ipynb
---

## Notebook Index (Manuscript-aligned)

**A00 (implicit)** – Preprocessing & metadata checks  
**A01** – PCA summary and biological interpretation  
**A02** – Sample-level UMAP embedding  
**A03** – Gene-level UMAP  
**A04** – PCA quadrant projections  
**A05** – Hallmark pathway module scoring and heatmaps  

---

## Design Philosophy

- `analysis_utils/` contains reusable, testable analysis logic.
- `notebooks/` are narrative, figure-producing entry points aligned with manuscript panels.
- `results/` contains all saved, versioned outputs used in figures and downstream analyses.

All figures in the manuscript can be regenerated by running the notebooks in order.

---

## Reproducibility Notes

- All paths are centralized in `config_utils.py`
- Intermediate and final results are saved to disk
- Figures are generated directly from stored results
- No manual copy-paste steps are required

---

## Status

---

## Manuscript Figures & Panels

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

The pipeline is currently in the figure-locking and manuscript-assembly phase.
Exploratory analyses have been consolidated into stable modules and notebooks.
    
📦 Module Summary (Publication Pipeline)
Module A — Preprocessing
Functions in preprocessing.py implement:
ENSEMBL → gene symbol mapping
logCPM normalization
duplicate-symbol collapsing
consistent sample ordering
export of processed matrices
Outputs:
expr_logcpm.parquet
expr_logcpm_symbol.parquet
metadata_samples.csv
These serve as canonical inputs for downstream modules.
Module B — Differential Expression
Implemented in de_utils.py.
Contrasts supported:
Late vs Early activation
RHOG vs SafeHarbor at selected timepoints (e.g., 0h, 48h, 72h, 168h)
Outputs:
results/de/de_late_vs_early.csv
results/de/de_rhog_vs_safe_0h.csv
Volcano plots
Top-labeled gene plots
Ranked lists for GSEA
Module C — Hallmark Pathways & PC–Biology Alignment
Implemented in pathway_utils.py.
Features:
Enrichr/GSEApy integration for Hallmark signatures
Up/down signature extraction
Module scoring on symbol-collapsed expression matrix
Correlations between Hallmark scores and PC1/PC2
This module reveals that:
PC1 aligns with IL2/STAT5, NF-κB, inflammatory activation
PC2 aligns with interferon stress vs E2F/OxPhos programs
Outputs:
hallmark_enrichment_late_vs_early_UP.csv
hallmark_enrichment_late_vs_early_DOWN.csv
hallmark_pc_correlations_PC1_PC2.csv
high-resolution pathway barplots
PC–pathway heatmap
These results provide the mechanistic interpretation of PCA axes.
Module D — PCA Interpretability
Implemented in pca_utils.py.
Features:
reproducible PCA computation (run_pca)
PC1/PC2 biological interpretation figure
centroids-by-time trajectories
RHOG vs SafeHarbor comparisons
quadrant gene identification
export of PCA tables
Key biological insights:
PC1 = Effector activation (IL2/STAT5/NFκB) ←→ Interferon-high activation
PC2 = Interferon stress ←→ Proliferative E2F/OxPhos axis
RHOG shifts activation trajectory within existing CAR-T manifolds (modulator, not a fate changer).
Outputs:
pca_scores.parquet
pca_loadings.parquet
PCA_biological_interpretation_PC1_PC2.png
PCA_summary_PC5_PC6_by_hours.png
PCA_summary_PC5_PC6_by_guide.png
summary_PCA_figure.png
Module E — UMAP Embeddings (Samples + Genes)
Implemented in umap_utils.py.
Sample-level UMAP:
HVG selection
Scaling + UMAP embedding
Coloring by time, guide, donor
Gene-level UMAP:
HVGs for gene manifold
PC1/PC2 quadrants projected onto UMAP
Top quadrant genes labeled
Outputs:
sample_umap_coordinates.csv
Sample_UMAP_timepoint.png
Sample_UMAP_guide.png
Gene_UMAP_PC_quadrants.png
These embeddings complement PCA and help distinguish donor effects from CRISPR perturbation effects.
🔄 Reproducible Workflow
To reproduce all major analyses:
conda activate crispr_carT_env
jupyter lab
Then run notebooks in order:
A01_crispr_cart_pca_summary.ipynb
A02_sample_umap.ipynb
B01_late_vs_early_DE_and_pathways.ipynb
perturbation notebooks (RHOG vs SafeHarbor)
trajectory modules
Utilities ensure that all intermediate outputs land in consistent folders.
🧭 Scientific Goal
This repository serves as a computational framework to understand:
how CRISPR perturbations shape CAR-T activation states
which signaling modules dominate variance across time
where RHOG modifies effector or interferon programs
how donor variability interacts with gene perturbation
which axes of activation represent true biology vs technical structure
This architecture is now robust enough to be extended toward:
cell-cycle regression
pseudotime analysis
latent variable models (scVI, MOFA)
integration with protein or epigenomic data
And—after the CAR-T pipeline is fully locked—the axolotl thymus regeneration project can slot into the same architecture.

🚀 Recent Progress Update — December 11, 2025
- The CAR-T perturbation analysis pipeline reached a major level of maturity today.
Several modules were consolidated into reproducible utilities, and the analytical outputs now follow a stable, publication-grade structure.

- PCA Module Stabilization
The PCA workflow was fully refactored into analysis_utils/pca_utils.py, enabling consistent execution across notebooks.
Key accomplishments:
Standardized PCA computation (run_pca) now returns scores, loadings, explained variance tables, and fitted PCA objects.
All outputs are now saved under results/pca/, ensuring reproducibility and downstream accessibility.
PCA visualizations were elevated to biological interpretation figures, integrating:
IL2/STAT5 effector activation
IFN-I / IFN-γ stress axis
E2F / OxPhos proliferative programs

-The metadata was formally integrated with PCs to produce metadata_with_pcs.csv, now the backbone for trajectory analyses.

- Hallmark Pathway Integration
- The Late vs Early activation comparison is now structurally complete:
- Differential expression tables are tracked in results/de/.
- Hallmark enrichment (UP/DOWN signatures) is performed through Enrichr/GSEApy and exported as both CSVs and high-resolution barplots.
- Pathway–PC correlations (PC1 and PC2) were computed and saved, enabling alignment of variance components with known immune programs.
- A heatmap summary provides an immediate overview of program alignment with major principal components.
- This module now serves as the mechanistic bridge between statistical variance and immunobiology.
UMAP Embedding Framework
-- To complement PCA, a dedicated UMAP pipeline was added under analysis_utils/umap_utils.py.
- This includes:
Selection of highly variable genes
Scaling and UMAP projection (sample-level)
Metadata integration (hours, guide, donor)
Color-coded plots capturing:
activation kinetics
perturbation effects
donor structure
- The resulting UMAP coordinates were saved to results/umap/sample_umap_coordinates.csv, enabling reproducible embedding overlays in future modules (e.g., RHOG-specific signatures or trajectory inference).
Processed Data Enhancements
A symbol-collapsed expression matrix (expr_logcpm_symbol.parquet) was formally added to the data processing workflow.
This dataset enables downstream:
module scoring
pathway projections
gene-symbol–based visualizations
without repeated mapping steps.
Notebook Architecture
Notebooks were reorganized into a modular structure reflecting the analysis pipeline:
A01 — PCA + biological interpretation
A02 — UMAP
B01 — Differential expression + Hallmark pathways
CRISPR perturbation modules updated for consistent inputs
Each notebook now draws from shared utilities, reducing redundancy and increasing clarity.






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

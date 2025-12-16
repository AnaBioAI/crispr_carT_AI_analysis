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

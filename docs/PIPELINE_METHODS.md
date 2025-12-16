The pipeline is currently in the figure-locking and manuscript-assembly phase.
Exploratory analyses have been consolidated into stable modules and notebooks.
    
📦 Module Summary (Publication Pipeline)

- Module A — Preprocessing
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

- Module B — Differential Expression
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

- Module C — Hallmark Pathways & PC–Biology Alignment
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

- Module D — PCA Interpretability
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

-Module E — UMAP Embeddings (Samples + Genes)
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

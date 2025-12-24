Figure 1. CRISPR CAR-T perturbation analysis pipeline

A. Data acquisition and preprocessing.
Raw CRISPR CAR-T RNA-seq counts and sample metadata (donor, guide, activation time) are processed through standardized normalization (logCPM/log1p), ENSEMBL-to-gene-symbol harmonization, and duplicate symbol collapsing to generate canonical, reusable expression matrices.

B. Dimensionality reduction.
Symbol-level normalized expression is analyzed using principal component analysis (PCA) to decompose variance and enable biological interpretation of activation trajectories, and UMAP to visualize nonlinear sample structure while preserving local relationships. PCA scores, loadings, and UMAP coordinates are saved for downstream reuse.

C. Differential expression and pathway integration.
Linear modeling identifies gene-level differences across activation time and perturbation conditions. Differentially expressed genes are organized into direction-aware gene sets and integrated with Hallmark pathway enrichment to support program-level interpretation and alignment with PCA axes.

All intermediate and final outputs are saved with stable filenames, enabling reproducible figure generation and downstream trajectory analyses.

⸻


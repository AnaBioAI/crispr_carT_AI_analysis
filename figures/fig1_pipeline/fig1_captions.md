Figure 1. CRISPR CAR-T perturbation analysis pipeline

Figure 1. Overview of the computational pipeline used to analyze CRISPR-perturbed CAR-T cell activation across a time course. The workflow integrates standardized preprocessing, dimensionality reduction, differential expression, pathway analysis, and perturbation-specific trajectory modeling to generate reproducible, manuscript-ready figures.

⸻

Panel A. Data acquisition & preprocessing

Raw gene-level RNA-seq counts and associated sample metadata (donor, guide, activation time) were processed through a standardized preprocessing workflow. Expression data were normalized using logCPM, gene identifiers were harmonized from ENSEMBL IDs to gene symbols, and duplicated symbols were collapsed by mean expression. This step produces canonical, symbol-level expression matrices and aligned metadata that serve as stable inputs for all downstream analyses.

Outputs:
	•	expr_logcpm.parquet
	•	expr_logcpm_symbol.parquet
	•	metadata_samples.csv

⸻

Panel B. Dimensionality reduction: PCA and UMAP

Processed expression matrices were subjected to principal component analysis (PCA) to identify dominant axes of transcriptional variation across CAR-T activation. PCA scores and loadings enable biological interpretation of variance components, while UMAP embeddings provide complementary nonlinear representations of sample relationships. Samples are visualized with respect to activation time, perturbation (RHOG vs SafeHarbor), and donor, allowing separation of biological signal from donor-specific effects.

Key outputs:
	•	PCA scores and loadings
	•	Sample-level UMAP coordinates
	•	Time- and guide-colored embeddings

⸻

Panel C. Differential expression and pathway abstraction

Differential expression analyses were performed to compare early versus late activation states and CRISPR perturbations (e.g., RHOG vs SafeHarbor). Gene-level contrasts were summarized using volcano plots and direction-aware gene lists. These gene-level results were subsequently abstracted into biological programs through Hallmark pathway enrichment, enabling pathway-level interpretation of activation dynamics.

Outputs:
	•	Differential expression tables
	•	Volcano plots
	•	Hallmark enrichment tables and summary plots

⸻

Reproducibility note:
All intermediate results and figures are saved to standardized directories, allowing full regeneration of this figure by rerunning the associated notebooks.

⸻

Provenance

Generated from:
	•	analysis_utils/preprocessing.py
	•	A01_crispr_cart_pca_summary.ipynb
	•	A02_sample_umap.ipynb
	•	B01_late_vs_early_DE_and_pathways.ipynb

⸻


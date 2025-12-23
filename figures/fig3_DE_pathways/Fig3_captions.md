###Figure 3. CAR-T activation is driven by coordinated, time-dependent transcriptional programs

A. Differential gene expression between late and early CAR-T activation
Volcano plot showing differential gene expression between late (≥168 h) and early (0 h) CAR-T activation states. Each point represents a gene, plotted by log2 fold change (late – early) and −log10(FDR-adjusted p-value). Vertical dashed lines indicate effect size thresholds (|log2FC| ≥ 0.5), and the horizontal dashed line indicates the significance threshold (FDR ≤ 0.2). Genes meeting both thresholds are highlighted, and the top differentially expressed genes are labeled by gene symbol. This analysis identifies coordinated transcriptional changes associated with CAR-T activation and maturation across the time course.

B. Hallmark pathway enrichment of activation-associated gene programs
Bar plots showing Hallmark pathway enrichment derived from genes upregulated (top) and downregulated (bottom) in late versus early CAR-T activation. Differentially expressed genes were stratified by direction of change prior to enrichment analysis, enabling direction-aware interpretation of pathway activity. Late activation is characterized by enrichment of IL-2/STAT5 signaling, inflammatory response, interferon signaling, and metabolic programs, whereas pathways enriched among downregulated genes reflect attenuation of early activation–associated programs.

C. Alignment of transcriptional programs with principal components
Heatmap showing correlations between Hallmark pathway module scores and the first two principal components (PC1 and PC2) derived from PCA of CAR-T transcriptomes. PC1 correlates with effector/activation programs (e.g., IL-2/STAT5 and inflammatory signaling) in opposition to interferon-biased programs. PC2 captures a proliferative/metabolic versus interferon-stress axis, reflecting E2F target and oxidative phosphorylation programs. This analysis links gene-level differential expression to low-dimensional activation trajectories.

Generated from:
	•	B01_late_vs_early_DE_and_pathways.ipynb (C1, C2)
	•	A05_hallmark_pathways.ipynb (C2, C3)

⸻

If you run the UMAP export cell and confirm the three PNGs land in figures/fig2_activation_trajectories/, we can immediately write Fig 2D3 caption and “lock” Figure 2 fully (D1–D3) with zero loose ends.
Outputs
	•	Fig3C1_volcano_late_vs_early_labeled.png
	•	Fig3C2_hallmark_barplot_UP.png
	•	Fig3C2_hallmark_barplot_DOWN.png
	•	Fig3C3_hallmark_PC_corr_heatmap.png

<!--
Generated from:
- Volcano + enrichment: notebooks/B01_late_vs_early_DE_and_pathways/*
Outputs (source-of-truth):
- results/de/volcano_late_vs_early_labeled.png
- results/pathways/hallmark_barplot_late_vs_early_UP.png
- results/pathways/hallmark_barplot_late_vs_early_DOWN.png
- results/pathways/hallmark_pc_correlations_PC1_PC2_heatmap.png
-->
## Figure 3. Differential expression and pathway programs underlying CAR-T activation

### C1. Late vs Early activation volcano plot
Volcano plot summarizing differential expression between late and early activation timepoints in CRISPR CAR-T samples. Each point is a gene (symbol-collapsed expression). The x-axis shows log2 fold-change (Late vs Early) and the y-axis shows –log10(FDR). Genes meeting the significance criteria (|log2FC| ≥ 0.5 and FDR ≤ 0.2) are highlighted (upregulated: red; downregulated: blue), while non-significant genes are shown in gray.

### C2. Hallmark enrichment of late-activation upregulated genes
Bar plot of MSigDB Hallmark pathway enrichment for genes upregulated in late vs early activation. Enrichment highlights core immune activation programs and pathway-level structure consistent with the dominant variance axes observed in PCA.

### C3. Hallmark enrichment of late-activation downregulated genes
Bar plot of MSigDB Hallmark pathway enrichment for genes downregulated in late vs early activation, capturing programs reduced over the activation time course and complementing the late-upregulated signature.

### C4. Alignment of pathway programs with principal components (optional panel)
Heatmap of correlations between per-sample Hallmark module scores and principal component scores (PC1/PC2). This panel links gene set activity to the major transcriptional axes of variation, enabling mechanistic interpretation of low-dimensional trajectories.

<!--
Generated from:
- Volcano + enrichment: notebooks/B01_late_vs_early_DE_and_pathways/*
Outputs (source-of-truth):
- results/de/volcano_late_vs_early_labeled.png
- results/pathways/hallmark_barplot_late_vs_early_UP.png
- results/pathways/hallmark_barplot_late_vs_early_DOWN.png
- results/pathways/hallmark_pc_correlations_PC1_PC2_heatmap.png
-->
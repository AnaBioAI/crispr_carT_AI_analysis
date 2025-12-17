## Figure 3. Differential expression and program-level enrichment during CAR-T activation

### C1. Gene-level differential expression (Late vs Early)
Volcano plot comparing late versus early activation states across CAR-T samples. Each point represents a gene (symbol-level logCPM). The x-axis shows log2 fold-change and the y-axis shows –log10(FDR). Labeled genes highlight the strongest program-shifting transcripts that distinguish activation stages.

### C2. Hallmark pathway enrichment (Late vs Early)
Hallmark pathway enrichment analysis (MSigDB) performed on direction-aware gene sets derived from the late vs early differential expression results. Barplots show the most significantly enriched Hallmark terms for upregulated (Late vs Early – UP) and downregulated (Late vs Early – DOWN) gene sets, reported as –log10(FDR).

### C3. Program alignment with PCA axes (optional)
Heatmap of correlations between per-sample Hallmark module scores and PCA coordinates (PC1 and PC2), linking dominant variance components to interpretable immune programs (e.g., IL-2/STAT5 / inflammatory activation versus interferon stress and proliferative E2F/OxPhos programs).

<!--
Generated from:
- Volcano + enrichment: notebooks/B01_late_vs_early_DE_and_pathways/*
Outputs (source-of-truth):
- results/de/volcano_late_vs_early_labeled.png
- results/pathways/hallmark_barplot_late_vs_early_UP.png
- results/pathways/hallmark_barplot_late_vs_early_DOWN.png
- results/pathways/hallmark_pc_correlations_PC1_PC2_heatmap.png
-->
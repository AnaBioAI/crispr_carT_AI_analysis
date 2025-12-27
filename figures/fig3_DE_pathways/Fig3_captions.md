Figure 3. CAR T cell activation is driven by coordinated, time-dependent transcriptional programs.

Differential gene expression analysis comparing late (≥168 h) versus early (0 h) CAR T cell activation reveals widespread and coordinated transcriptional remodeling over time. Genes plotted by log₂ fold change (late minus early) and −log₁₀ FDR-adjusted p value show that activation time is the dominant driver of transcriptional variation, with large numbers of genes exhibiting consistent, directionally structured regulation. Effect size (|log₂FC| ≥ 0.5) and significance (FDR ≤ 0.2) thresholds highlight coherent gene programs rather than isolated transcriptional changes, and the most strongly regulated genes illustrate the scale and coordination of activation-associated remodeling.

Pathway-level abstraction of these gene-level changes using Hallmark gene sets reveals structured, direction-dependent program dynamics. Enrichment analysis performed separately on genes upregulated and downregulated at late activation demonstrates that CAR T cell maturation is characterized by induction of IL-2/STAT5 signaling, inflammatory response, interferon-associated pathways, and metabolic programs, alongside attenuation of early activation–associated responses. This pattern indicates a progressive rebalancing of functional programs rather than uniform transcriptional amplification.

To connect gene- and pathway-level changes to global transcriptional structure, correlations between Hallmark pathway scores and principal component scores were computed. Effector and inflammatory programs align strongly with PC1, opposing interferon-biased programs, while PC2 captures a proliferative and metabolic axis enriched for E2F targets and oxidative phosphorylation in opposition to interferon-stress responses. Together, these analyses demonstrate that dominant principal components reflect biologically meaningful activation programs and that CAR T cell activation unfolds through coordinated, time-dependent transcriptional trajectories.



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
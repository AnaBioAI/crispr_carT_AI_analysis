
## Figure 2. Activation trajectories and program modulation in CAR-T cells

### D1. PCA trajectory analysis
PCA projection of CAR-T samples into PC1–PC2 space reveals shared activation states across SafeHarbor and RHOG perturbations. PC1 captures an effector IL-2/STAT5/NFκB activation axis opposing interferon-driven activation, while PC2 reflects an interferon-stress versus proliferative E2F/OxPhos program. Arrows connect time-ordered centroids for each guide (SafeHarbor, blue; RHOG, orange). Both conditions traverse identical biological quadrants, indicating conserved activation states; however, RHOG perturbation alters the shape and progression of the activation trajectory.

### D2. Hallmark pathway dynamics across activation
Heatmap showing z-scored Hallmark pathway module scores across activation time (0–240 h), ordered by time and stratified by guide (SafeHarbor, S; RHOG, R). Each time point includes six biological replicates per condition. Shared temporal activation of key programs is observed across conditions, while RHOG modulates the relative intensity and timing of IL-2/STAT5 signaling, interferon responses, apoptosis, E2F targets, and oxidative phosphorylation, consistent with the trajectory differences observed in D1.

### D3. Sample-level UMAP embeddings
UMAP projection of CAR-T samples using highly variable genes. Samples are colored by activation time (hours), perturbation (RHOG vs SafeHarbor), and donor. The embedding provides a nonlinear view of global structure, supporting that RHOG modulates progression through shared activation programs while donor effects contribute separable variation.

<!--
Generated from:
- D1: A01_crispr_cart_pca_summary.ipynb
- D2: A05_hallmark_pathways.ipynb

Outputs:
- results/pca/PCA_biological_interpretation_PC1_PC2.png
- results/pathways/hallmark_module_scores_heatmap.png
-->

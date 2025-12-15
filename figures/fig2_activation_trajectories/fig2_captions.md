
Caption (final draft):



## Figure 2. Activation trajectories and program modulation in CAR-T cells

### D1. PCA trajectory analysis
PCA projection of CAR-T samples into PC1–PC2 space reveals shared activation states across SafeHarbor and RHOG perturbations. PC1 captures an effector IL-2/STAT5/NFκB activation axis opposing interferon-driven activation, while PC2 reflects interferon-stress versus proliferative E2F/OxPhos programs. Arrows connect time-ordered centroids for each guide (SafeHarbor, blue; RHOG, orange). Both conditions traverse identical biological quadrants, indicating conserved activation states; however, RHOG perturbation alters trajectory shape and progression through this space.

### D2. Hallmark pathway dynamics across activation
Heatmap showing z-scored Hallmark pathway module scores across activation time (0–240 h), ordered by time and stratified by guide (SafeHarbor, S; RHOG, R). Each time point includes six biological replicates per condition. Shared temporal activation of key programs is observed across conditions, while RHOG modulates the relative intensity and timing of IL-2/STAT5 signaling, interferon responses, apoptosis, E2F targets, and oxidative phosphorylation, consistent with the trajectory differences observed in D1.

<!--
Generated from:
- D1: A01_crispr_cart_pca_summary.ipynb
- D2: A05_hallmark_pathways.ipynb

Outputs:
- results/pca/PCA_biological_interpretation_PC1_PC2.png
- results/pathways/hallmark_module_scores_heatmap.png
-->
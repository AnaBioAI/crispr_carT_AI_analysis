Figure 2. Conserved activation trajectories and program-level modulation in CAR T cells.
Principal component analysis (PCA) of CAR T cell transcriptomes projected into PC1–PC2 space reveals a shared activation trajectory across SafeHarbor control and RHOG-perturbed cells (A). PC1 captures a dominant effector activation axis enriched for IL-2/STAT5, NFκB, and inflammatory signaling, opposing interferon-associated activation states, while PC2 reflects an interferon-stress versus proliferative and metabolic program enriched for E2F targets and oxidative phosphorylation. Time-ordered centroids connected across activation show that both perturbations traverse identical biological regions of transcriptional space, indicating conserved activation states, while subtle differences in trajectory shape and progression are observed for RHOG-perturbed cells. Genes contributing most strongly to PC1 include IL2, IFNG, CSF2, IL1B, and inflammatory chemokines (CXCL8, CXCL10, CCL2), supporting interpretation of this axis as effector cytokine and inflammatory activation amplitude rather than lineage or memory differentiation.

Program-level dynamics across activation are shown by a heatmap of z-scored Hallmark pathway scores ordered by time and stratified by guide (B). Each activation time point includes six biological replicates per condition. Shared temporal induction of key activation programs is observed across both conditions, while RHOG perturbation modulates the relative timing and magnitude of IL-2/STAT5 signaling, interferon responses, apoptosis, E2F targets, and oxidative phosphorylation, consistent with the trajectory-level differences observed in PCA.

Nonlinear sample relationships visualized by Uniform Manifold Approximation and Projection (UMAP) further support conserved activation structure (C). Samples cluster primarily by activation time, with minimal segregation by perturbation, while donor-associated variation contributes orthogonal structure. Together, these analyses indicate that RHOG perturbation biases progression within a shared CAR T cell activation landscape rather than inducing discrete transcriptional states.
-
-Outputs:
-- results/pca/PCA_biological_interpretation_PC1_PC2.png
-- results/pathways/hallmark_module_scores_heatmap.png


-- D1: A01_crispr_cart_pca_summary.ipynb
-- D2: A05_hallmark_pathways.ipynb
-
-Outputs:
-- results/pca/PCA_biological_interpretation_PC1_PC2.png
-- results/pathways/hallmark_module_scores_heatmap.png



## Figure 4. RHOG modulates CAR-T activation trajectories without inducing new cell states

### A. RHOG and SafeHarbor follow shared activation trajectories in higher-order PCA space
(PC4/PC5 description: regulatory/stress-associated program vs lineage separation; emphasize co-traveling trajectories.)
PCA projection of CAR-T samples into PC4–PC5 space reveals orthogonal transcriptional programs underlying activation dynamics. PC5 captures a cytotoxic versus helper T cell identity axis, characterized by CD8A/B, NKG7, GZMK, and FGFBP2 loadings opposing CD4, IL7R, CCR4, and IL13 expression. PC4 reflects a regulatory and stress-associated activation program enriched for FOXP3, IL1RN, CXCR6, IL13, and metabolic stress-response genes. Across all timepoints, RHOG and SafeHarbor samples co-occupy the same temporal clouds, indicating conserved lineage and regulatory states with no guide-specific segregation.

### B. RHOG does not significantly alter memory-associated transcriptional programs
(State the negative result clearly and confidently; cite stats briefly.)
Boxplots show per-sample program scores across activation time for memory-associated programs (B1) and the balance between memory and effector programs (B2). RHOG and SafeHarbor CAR-T cells exhibit overlapping distributions at all timepoints. Statistical testing (Mann–Whitney U and OLS regression) reveals no significant guide-dependent differences, indicating that RHOG perturbation does not reprogram memory fate or effector balance.“Memory–effector balance was calculated as the difference between z-scored memory and effector program scores, where positive values indicate memory-biased states.”

### C. RHOG introduces modest program-level biases at late activation
(Highlight directionality, not magnitude; interpretation-focused.)
RHOG-associated bias in transcriptional programs at late CAR-T activation.
Donor-averaged differences in Hallmark pathway scores between RHOG-perturbed and SafeHarbor CAR-T cells at late activation (168–240 h). RHOG perturbation is associated with modest attenuation of interferon-associated programs and relative enrichment of effector, metabolic, and proliferative programs, consistent with the positioning of RHOG trajectories in higher-order PCA space. Error bars denote standard error across donors.

---

Generated from:
- Notebook05_CRISPR_perturbation
- Notebook06_module_trajectory
<!--
Generated from:
- Notebook05_CRISPR_perturbation/05_02_CRISPR_perturbation.ipynb

Outputs:
- Fig4A_PCA_PC4_PC5_lineage_trajectories.png
- Fig4B_memory_program_scores.png

**Statistical analysis.**  
Differences in memory-associated transcriptional scores between RHOG and SafeHarbor CAR-T cells were evaluated using two-sided Mann–Whitney U tests at each activation time point (0, 24, 72, 168, and 240 h). No significant differences were observed at any time point (all p > 0.1). Linear regression modeling incorporating guide and activation time as covariates similarly revealed no significant effect of RHOG perturbation on memory scores (R² = 0.004, p = 0.897), indicating that RHOG does not measurably alter memory-associated transcriptional programs under these conditions.These results suggest that RHOG modulates activation trajectories without inducing stable memory-associated transcriptional states.

Statistical comparisons were performed using Mann–Whitney U tests per time point and OLS regression across all samples.

for t in sorted(df["hours"].unique()):
    sub = df[df["hours"] == t]
    sh = sub[sub["guide"] == "SafeHarbor"]["memory_score"]
    rh = sub[sub["guide"] == "RHOG"]["memory_score"]
    if len(sh) > 2 and len(rh) > 2:
        _, p = mannwhitneyu(rh, sh, alternative="two-sided")
        print(f"{t}h: p = {p:.3g}")
        0h: p = 0.132
24h: p = 0.818
72h: p = 0.937
168h: p = 0.394
240h: p = 0.24
-->
        OLS Regression Results                            
==============================================================================
Dep. Variable:           memory_score   R-squared:                       0.004
Model:                            OLS   Adj. R-squared:                 -0.031
Method:                 Least Squares   F-statistic:                    0.1088
Date:                Thu, 18 Dec 2025   Prob (F-statistic):              0.897
Time:                        18:32:34   Log-Likelihood:                -61.689
No. Observations:                  60   AIC:                             129.4
Df Residuals:                      57   BIC:                             135.7
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
=======================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------
Intercept               0.0600      0.161      0.371      0.712      -0.263       0.383
guide[T.SafeHarbor]    -0.0354      0.179     -0.198      0.844      -0.394       0.323
hours                  -0.0004      0.001     -0.423      0.674      -0.002       0.002
==============================================================================
Omnibus:                       26.421   Durbin-Watson:                   0.221
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                6.655
Skew:                           0.492   Prob(JB):                       0.0359
Kurtosis:                       1.699   Cond. No.                         322.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
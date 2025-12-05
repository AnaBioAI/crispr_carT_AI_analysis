import os
import numpy as np
import pandas as pd


PROJECT_ROOT = "/Users/acastano/Desktop/crispr_carT_AI_analysis"

# ----------------------------------------------------------------------
# Load ENSG → SYMBOL mapping
# ----------------------------------------------------------------------
def load_gene_mapping():
    path = os.path.join(PROJECT_ROOT, "data/processed/ensg_to_symbol.csv")
    df = pd.read_csv(path)

    # Try to infer mapping columns
    id_candidates = ["ensembl_id", "ensembl_gene_id", "gene_id", "ensembl"]
    sym_candidates = ["gene_symbol", "symbol", "hgnc_symbol"]

    id_col = next((c for c in id_candidates if c in df.columns), None)
    sym_col = next((c for c in sym_candidates if c in df.columns), None)

    if id_col is None or sym_col is None:
        raise ValueError(
            f"Could not find ENSG or symbol columns in {path}. "
            f"Columns present: {df.columns.tolist()}"
        )

    df = df.dropna(subset=[sym_col]).drop_duplicates(subset=[id_col])
    mapping = df.set_index(id_col)[sym_col]
    return mapping


# ----------------------------------------------------------------------
# Map expression ENSG → SYMBOL
# ----------------------------------------------------------------------
def map_expression_to_symbols(expr_logcpm, mapping):
    expr = expr_logcpm.copy()
    expr["gene_symbol"] = expr.index.map(mapping)
    expr = (
        expr
        .dropna(subset=["gene_symbol"])
        .set_index("gene_symbol")
        .groupby(level=0).mean()
    )
    return expr


# ----------------------------------------------------------------------
# Compute effector & regulatory module scores
# ----------------------------------------------------------------------
def compute_module_scores(expr):
    effector_genes = [
        "PRF1", "GZMB", "NKG7", "CD8A", "CD8B", "IFNG", "TNF"
    ]

    reg_genes = [
        "IL1RN", "FSTL3", "ARHGEF26", "SEC22C", "TRIM34",
        "AZU1", "MST1L", "PBX3", "THOC7", "RIC3"
    ]

    eff_present = [g for g in effector_genes if g in expr.index]
    reg_present = [g for g in reg_genes if g in expr.index]

    expr_z = expr.sub(expr.mean(axis=1), axis=0).div(
        expr.std(axis=1) + 1e-6, axis=0
    )

    eff_score = expr_z.loc[eff_present].mean(axis=0)
    reg_score = expr_z.loc[reg_present].mean(axis=0)

    return eff_score, reg_score


# ----------------------------------------------------------------------
# Add module deltas, speeds, angles
# ----------------------------------------------------------------------
def add_trajectory_metrics(df):
    def compute(gr):
        gr = gr.sort_values("hours").copy()
        gr["d_eff"] = gr["effector_score"].diff()
        gr["d_reg"] = gr["reg_score"].diff()
        gr["dt"]    = gr["hours"].diff()

        gr["step_distance"] = np.sqrt(gr["d_eff"]**2 + gr["d_reg"]**2)
        gr["speed_per_hour"] = gr["step_distance"] / gr["dt"].replace(0, np.nan)
        gr["angle_rad"] = np.arctan2(gr["d_reg"], gr["d_eff"])
        return gr

    return df.groupby(["donor", "guide"], group_keys=False).apply(compute)


# ----------------------------------------------------------------------
# Quadrant classification from PC5/PC6
# ----------------------------------------------------------------------
def assign_quadrants(df):
    def quad(row):
        if row["PC5"] >= 0 and row["PC6"] >= 0:
            return "Q1: Eff+ / Reg+"
        elif row["PC5"] < 0 and row["PC6"] >= 0:
            return "Q2: Eff- / Reg+"
        elif row["PC5"] < 0 and row["PC6"] < 0:
            return "Q3: Eff- / Reg-"
        else:
            return "Q4: Eff+ / Reg-"

    df["PC_quadrant"] = df.apply(quad, axis=1)
    return df


# ----------------------------------------------------------------------
# MAIN PIPELINE FUNCTION
# ----------------------------------------------------------------------
def build_module_trajectory_table():

    # --- Load data ---
    expr_logcpm = pd.read_parquet(
        os.path.join(PROJECT_ROOT, "data/processed/expr_logcpm.parquet")
    )
    meta = pd.read_csv(
        os.path.join(PROJECT_ROOT, "data/processed/metadata_samples.csv")
    ).set_index("sample_id")

    scores_df = pd.read_csv(
        os.path.join(PROJECT_ROOT, "results/pca/pca_scores.csv"),
        index_col=0,
    )

    # --- Align samples ---
    common = scores_df.index.intersection(meta.index).intersection(expr_logcpm.columns)
    expr_logcpm = expr_logcpm[common]
    scores_df   = scores_df.loc[common]
    meta        = meta.loc[common]

    # --- Convert ENSG → symbol ---
    mapping = load_gene_mapping()
    expr = map_expression_to_symbols(expr_logcpm, mapping)

    # --- Compute module scores ---
    eff, reg = compute_module_scores(expr)

    df = scores_df.join(meta)
    df["hours"] = df["hours"].astype(float)
    df["effector_score"] = eff
    df["reg_score"]      = reg

    # --- Compute trajectories ---
    df = add_trajectory_metrics(df)

    # --- Assign quadrants ---
    df = assign_quadrants(df)

    # --- Save final table ---
    outdir = os.path.join(PROJECT_ROOT, "results/modules")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "metadata_with_modules_and_trajectories.csv")
    df.to_csv(outpath)

    print(f"Saved enriched trajectory table → {outpath}")
    return df


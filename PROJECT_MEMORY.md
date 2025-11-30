# CRISPR CAR-T AI Project Memory

## Key Commands
- startlab → activates the CRISPR CAR-T AI environment and launches JupyterLab
- openlab → opens a vanilla Jupyter instance in ~/Documents
- stoplab → deactivates and runs auto-backup
- labstatus → shows which conda env is active

## Auto-backup
- Each time you run stoplab, .zshrc is backed up to zshrc_backup_YYYY-MM-DD.txt and pushed to GitHub.

## Environment
- Conda environment: crispr_carT_env
- Notebook folder: ~/Desktop/crispr_carT_AI_analysis/notebooks

# CRISPR CAR-T AI Atlas — Project Memory

## Dataset
- GEO: GSE266618
- counts: data/raw/GSE266618_counts.csv (60675 genes × 60 samples)
- metadata columns: GSM, title, cell_type, hours, guide, donor

## Processed files
- expr_logcpm.parquet
- metadata_samples.csv

## PCA Summary
- PC1: IL2/STAT5 vs IFN axis
- PC2: stress vs proliferation axis
- Quadrants Q1–Q4 defined by sign(PC1), sign(PC2)

## UMAP Summary
- sample-level UMAP shaped by timepoint >> donor >> guide
- gene UMAP shows pathway modules (IFN, OxPhos, cytotoxicity)

## TODO / Next Steps
- Wrap DE functions into de_utils.py
- Wrap pathway enrichment into pathway_utils.py
- Build "Activation Atlas" figure collection

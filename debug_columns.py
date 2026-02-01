import pandas as pd

# Load first few rows
df = pd.read_csv('qmof.csv', nrows=5)
cols = df.columns.tolist()

print("=== DENSITY COLUMNS ===")
density_cols = [c for c in cols if 'density' in c.lower()]
print(density_cols)

print("\n=== LINKER COLUMNS ===")
linker_cols = [c for c in cols if 'linker' in c.lower()]
print(linker_cols)

print("\n=== SMILES COLUMNS ===")
smiles_cols = [c for c in cols if 'smiles' in c.lower()]
print(smiles_cols)

print("\n=== SAMPLE VALUES ===")
if 'info.density' in cols:
    print(f"info.density sample: {df['info.density'].tolist()}")

if 'info.mofid.smiles_linkers' in cols:
    print(f"smiles_linkers sample: {df['info.mofid.smiles_linkers'].tolist()}")

# Check distribution of linker values
print("\n=== FULL DATA CHECK ===")
df_full = pd.read_csv('qmof.csv', low_memory=False)
print(f"Total rows: {len(df_full)}")

if 'info.density' in df_full.columns:
    print(f"\ninfo.density stats:")
    print(f"  Non-null: {df_full['info.density'].notna().sum()}")
    print(f"  Min: {df_full['info.density'].min()}")
    print(f"  Max: {df_full['info.density'].max()}")
    print(f"  Mean: {df_full['info.density'].mean():.2f}")
    print(f"  Unique values: {df_full['info.density'].nunique()}")

if 'info.mofid.smiles_linkers' in df_full.columns:
    print(f"\ninfo.mofid.smiles_linkers stats:")
    non_null = df_full['info.mofid.smiles_linkers'].notna().sum()
    non_empty = (df_full['info.mofid.smiles_linkers'].astype(str).str.len() > 2).sum()
    print(f"  Non-null: {non_null}")
    print(f"  Non-empty (len>2): {non_empty}")
    print(f"  Sample values:")
    for i, val in enumerate(df_full['info.mofid.smiles_linkers'].dropna().head(10)):
        print(f"    {i+1}. {val[:80]}..." if len(str(val)) > 80 else f"    {i+1}. {val}")

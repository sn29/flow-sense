import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from umap import UMAP
import os

# Load features
df = pd.read_csv('features.csv')

# Ensure Dose is categorical
df['Dose'] = df['Dose'].astype(str)

# Get only marker columns (exclude metadata)
marker_cols = df.columns.difference(['Filename', 'PatientID', 'Dose', 'Time'])

# Create eda_plots folder if not exists
os.makedirs('eda_plots', exist_ok=True)

# 1. Marker distribution by Dose
for col in marker_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='Dose', y=col, data=df)
    plt.title(f'{col} by Dose')
    plt.savefig(f'eda_plots/{col}_dose_boxplot.png')
    plt.close()

# 2. Correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(df[marker_cols].corr(), annot=False, cmap='coolwarm')
plt.title('Marker Correlation Matrix')
plt.tight_layout()
plt.savefig('eda_plots/correlation_matrix.png')
plt.close()

# 3. PCA
pca = PCA(n_components=2)
pca_coords = pca.fit_transform(df[marker_cols])
df['PCA1'] = pca_coords[:, 0]
df['PCA2'] = pca_coords[:, 1]

plt.figure(figsize=(6, 5))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Dose')
plt.title('PCA of Marker Intensities')
plt.savefig('eda_plots/pca_plot.png')
plt.close()

# 4. UMAP
umap = UMAP(random_state=42)
umap_coords = umap.fit_transform(df[marker_cols])
df['UMAP1'] = umap_coords[:, 0]
df['UMAP2'] = umap_coords[:, 1]

plt.figure(figsize=(6, 5))
sns.scatterplot(data=df, x='UMAP1', y='UMAP2', hue='Dose')
plt.title('UMAP of Marker Intensities')
plt.savefig('eda_plots/umap_plot.png')
plt.close()

print("✅ EDA plots saved to eda_plots/")

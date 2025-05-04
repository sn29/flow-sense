# FlowSense

ML pipeline to predict steroid dose (VH, MP20, MP200) from flow cytometry marker expression.

🚧 **Project Status**: In progress — core pipeline complete, feature tuning and documentation ongoing,Currently mapping fluorochrome channels (e.g., Alexa Fluor 488-A) to known markers (e.g., CXCR4, CCR1) for biological interpretation.

## Dataset

Flow cytometry data from [FlowRepository: FR-FCM-ZYND](https://flowrepository.org/id/FR-FCM-ZYND)  
Makiya M. et al., NIAID/NIH, 2018

## What’s in this repo

- Data preprocessing pipeline for .fcs files
- XGBoost classifier for dose prediction
- SHAP analysis to interpret markers
- Clean EDA and dimensionality reduction (UMAP, PCA)

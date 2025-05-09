# FlowSense

I am developing an ML pipeline to predict steroid dose (VH, MP20, MP200) from flow cytometry data.

Project Status: In progress: core pipeline is complete, feature tuning and documentation is ongoing. I am currently mapping fluorochrome channels to known markers for biological interpretation.

## Dataset

Flow cytometry data from [FlowRepository: FR-FCM-ZYND](https://flowrepository.org/id/FR-FCM-ZYND)  
Makiya M. et al., NIAID/NIH, 2018

## What’s in this repo

- Data preprocessing pipeline for .fcs files
- XGBoost classifier for dose prediction
- SHAP analysis to interpret markers
- Clean EDA and dimensionality reduction (UMAP, PCA)

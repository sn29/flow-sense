import os
import pandas as pd
import numpy as np
from FlowCytometryTools import FCMeasurement
from scipy.stats import median_abs_deviation

# Load metadata
metadata = pd.read_csv('metadata.csv')

# Filter only stained samples
metadata = metadata[metadata['Condition'] == 'Stained']

features = []

for _, row in metadata.iterrows():
    file_path = os.path.join('data', row['Filename'])
    sample = FCMeasurement(ID=row['Filename'], datafile=file_path)

    # Transform: arcsinh(x / 150)
    data = np.arcsinh(sample.data / 150)

    # Compute MFI for all markers
    mfis = data.median().to_dict()

    # Add metadata
    mfis.update({
        'Filename': row['Filename'],
        'PatientID': row['PatientID'],
        'Dose': row['Dose'],
        'Time': row['Time']
    })

    features.append(mfis)

# Save to CSV
df = pd.DataFrame(features)
df.to_csv('features.csv', index=False)

print("✅ Preprocessing complete — features.csv saved.")

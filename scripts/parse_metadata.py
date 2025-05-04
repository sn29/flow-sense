import os
import pandas as pd
import re

data_folder = 'data/'

fcs_files = [f for f in os.listdir(data_folder) if f.endswith('.fcs')]

metadata = []

for filename in fcs_files:
    patient_id = None
    timepoint = None
    dose = None
    condition = 'Stained'

    if 'Unstained' in filename:
        condition = 'Unstained'
        timepoint = 'None'
        dose = 'None'

    match = re.search(r'Patient_(\d+)', filename)
    if match:
        patient_id = match.group(1)

    if 'Baseline' in filename:
        timepoint = 'Baseline'
    elif '120min' in filename:
        timepoint = '120min'

    if 'MP20' in filename:
        dose = 'MP20'
    elif 'MP200' in filename:
        dose = 'MP200'
    elif 'VH' in filename:
        dose = 'VH'
    elif 'None' in filename and 'Baseline' in filename:
        dose = 'None'

    metadata.append({
        'Filename': filename,
        'PatientID': patient_id,
        'Time': timepoint,
        'Dose': dose,
        'Condition': condition
    })

df = pd.DataFrame(metadata)
df.to_csv('metadata.csv', index=False)

print("✅ Metadata saved to metadata.csv")

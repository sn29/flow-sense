import pandas as pd

df = pd.read_csv('features.csv')

# Convert Dose column
def convert_dose(dose):
    if pd.isna(dose) or dose == 'None' or dose == 'VH':
        return 0
    elif 'MP20' in str(dose):
        return 1
    else:
        return -1  # unknown or junk

df['Dose'] = df['Dose'].apply(convert_dose)

# Drop unknown values
df = df[df['Dose'] != -1]

df.to_csv('features_clean.csv', index=False)
print("✅ Saved: features_clean.csv with cleaned Dose values")

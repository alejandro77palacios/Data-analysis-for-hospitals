import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 8)

# %% carga datos
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# %% fusión datos
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
hospitals = pd.concat([general, prenatal, sports], ignore_index=True)
hospitals.drop(columns=['Unnamed: 0'], inplace=True)

# %% limpizar datos
hospitals.dropna(how='all', inplace=True)
hospitals['gender'].replace({'man': 'm', 'male': 'm', 'woman': 'f', 'female': 'f'}, inplace=True)
hospitals['gender'].fillna('f', inplace=True)
cols_with_errors = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
for col in cols_with_errors:
    hospitals[col].fillna(0, inplace=True)

# %% análisis gráfico
hospitals.plot(kind='hist', y='age', bins=20, title='BMI')
plt.show()
hospitals.value_counts(subset='diagnosis').nlargest(3).plot(kind='pie', title='Diagnosis')
plt.show()

fig, axes = plt.subplots()
heights = []
for h in ('general', 'prenatal', 'sports'):
    heights.append(hospitals.loc[hospitals['hospital'] == h, 'height'])
fig, axes = plt.subplots()
plt.violinplot(heights)
# axes.set_xticks((3, 3))
# axes.set_xticklabels(('general', 'prenatal', 'sports'))
plt.show()
# %% respuestas
print(f'The answer to the 1st question: 15-35')
print(f'The answer to the 2nd question: pregnancy')
print(f'The answer to the 3rd question: because people that are taller are more likely to be heighter than average')
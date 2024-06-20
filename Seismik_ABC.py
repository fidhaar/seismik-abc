import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data_sefrak = pd.read_csv("data seismik.csv", sep=';')

#Mendefinisikan nilai forward dan Reverse
forward = data_sefrak['Forward']
reverse = data_sefrak['Reverse']

#Mencari Nilai TAC-TBC dengan cara mengurangkan Forward(TAC) dan reverse(TBC)
TAC_diff_TBC = forward - reverse

#Mencari nilai TAB
TAB = (data_sefrak['Forward'].max() + data_sefrak['Reverse'].max()) / 2

# Add TAC_diff_TBC and TAB as new columns to the DataFrame
data_sefrak['TAC_diff_TBC'] = TAC_diff_TBC
data_sefrak['TAB'] = [TAB] * len(data_sefrak) 

# Check the data to understand its structure
print(data_sefrak.head())

#Gelombang Langsung
dir_forward = data_sefrak.loc[:1, ['Jarak', 'Forward']]
dir_reverse = data_sefrak.loc[19:, ['Jarak', 'Reverse']]

#Gelombang Reverse
ref_forward = data_sefrak.loc[1:, ['Jarak', 'Forward']]
ref_reverse = data_sefrak.loc[0:19, ['Jarak', 'Reverse']]

# Perform linear regression for Direct Forward
m_dir_forward, c_dir_forward = np.polyfit(dir_forward['Jarak'], dir_forward['Forward'], 1)
# Perform linear regression for Refracted Forward
m_ref_forward, c_ref_forward = np.polyfit(ref_forward['Jarak'], ref_forward['Forward'], 1)
# Perform linear regression for Direct Reverse
m_dir_reverse, c_dir_reverse = np.polyfit(dir_reverse['Jarak'], dir_reverse['Reverse'], 1)
# Perform linear regression for Refracted Reverse
m_ref_reverse, c_ref_reverse = np.polyfit(ref_reverse['Jarak'], ref_reverse['Reverse'], 1)

# Plot 'Jarak and Forward'
plt.figure(figsize=(8, 6))
plt.plot(dir_forward['Jarak'], dir_forward['Forward'], label='Direct Forward',color='Blue')
plt.plot(ref_forward['Jarak'], ref_forward['Forward'], label='Refracted Forward',color='Gray')
plt.plot(dir_reverse['Jarak'], dir_reverse['Reverse'], label='Direct Reverse', color='Red')
plt.plot(ref_reverse['Jarak'], ref_reverse['Reverse'], label='Refracted Reverse',color='Orange')
plt.xlabel('Jarak (m)')
plt.ylabel('Time (ms)')
plt.title('Kurva T vs X ')
plt.legend()
# Menambahkan garis regresi linear
plt.plot(dir_forward['Jarak'], m_dir_forward * dir_forward['Jarak'] + c_dir_forward, '--', color='Blue', label=f'Direct Forward: y = {m_dir_forward:.2f}x + {c_dir_forward:.2f}')
plt.plot(ref_forward['Jarak'], m_ref_forward * ref_forward['Jarak'] + c_ref_forward, '--', color='Gray', label=f'Refracted Forward: y = {m_ref_forward:.2f}x + {c_ref_forward:.2f}')
plt.plot(dir_reverse['Jarak'], m_dir_reverse * dir_reverse['Jarak'] + c_dir_reverse, '--', color='Red', label=f'Direct Reverse: y = {m_dir_reverse:.2f}x + {c_dir_reverse:.2f}')
plt.plot(ref_reverse['Jarak'], m_ref_reverse * ref_reverse['Jarak'] + c_ref_reverse, '--', color='Orange', label=f'Refracted Reverse: y = {m_ref_reverse:.2f}x + {c_ref_reverse:.2f}')

plt.legend()

plt.show()
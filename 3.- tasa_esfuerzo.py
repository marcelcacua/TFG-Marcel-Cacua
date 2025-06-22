import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:\\Users\\marce\\Desktop\\TFG\\POR PROVINCIAS\\tasa_esfuerzo\\tabla grafico tasa esfuerzo.xls")
df.columns
df['Accesibilidad'] = df['Tasa_esfuerzo'].apply(lambda x: 'Accesible (<30%)' if x < 0.3 else 'Inaccesible (≥30%)')

colors = df['Accesibilidad'].map({'Accesible (<30%)': '#2E86C1', 'Inaccesible (≥30%)': '#C0392B'})

sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams['grid.color'] = '#D3D3D3'

plt.figure(figsize=(12, 8))
bars = plt.bar(df['Provincia '], df['Tasa_esfuerzo'], color=colors)
plt.axhline(0.3, color='black', linestyle='--', label='Límite de Accesibilidad (30%)')
plt.ylabel('Tasa de esfuerzo')
plt.title('Accesibilidad de la Vivienda en España por Provincia 2022',
         fontsize=20,   
)
plt.xticks(rotation=90)  
plt.legend()

plt.tight_layout()

plt.show()


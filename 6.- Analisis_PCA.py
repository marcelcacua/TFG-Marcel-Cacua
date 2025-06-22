from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

file_path = "C:\\Users\\marce\\Desktop\\TFG\\Copia de variables_accesibilidad_vivienda.xlsx"
df = pd.read_excel(file_path)

#Analisis PCA con tres componentes principales 

df = df.rename(columns={
    'Tasa_esfuerzo': 'Tasa_esfuerzo',
    'Renat_Media_por_hogar ': 'Renta_media',
    'PIB_per_capita_provincial': 'PIB_PP',
    'Precio_m2': 'Precio_m2',
    'Tipos_hipotecario': 'Tipo_interes',
    'Tasa_Paro': 'Tasa_paro',
    'Tasa_empleo': 'Tasa_empleo',
    'Tasa_crecimiento_población': 'Δ_población',
    'Numero_vivienda_terminadas': 'Vivienda_nueva',
    'Numero_hipotecas': 'Num_Hipotecas',
    'IPV': 'IPV',
    'Importe_medio_hipotecas': 'Importe_hipotecas'
})

variables = [
    "Renta_media",
    "PIB_PP",
    "Precio_m2",
     "IPV",
     "IPC",
    "Tasa_empleo",
    "Δ_población",
    "Vivienda_nueva",
    "Num_Hipotecas",
]

df_años = df[df["Año"].isin([2015, 2018, 2022])]

df_años = df_años.dropna(subset=variables)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_años[variables])

pca = PCA(n_components=3)
principal_components = pca.fit_transform(data_scaled)

columns = [f'PC{i+1}' for i in range(3)]
pca_df = pd.DataFrame(principal_components, columns=columns)
pca_df['Año'] = df_años['Año'].values

explained_variance = pca.explained_variance_ratio_
cumulative_variance = explained_variance.cumsum()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(pca_df['PC1'], pca_df['PC2'], pca_df['PC3'], c=pca_df['Año'], cmap='viridis', s=100)

plt.title('PCA - Primeros 3 Componentes Principales', fontsize=14)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

plt.colorbar(sc, label='Año')
plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Grafico de Varianza Acumulada

plt.figure(figsize=(10, 6))
sns.barplot(x=columns, y=explained_variance, color='#1f77b4', label='Varianza individual')
sns.lineplot(x=columns, y=cumulative_variance, marker='o', color='#ff7f0e', label='Varianza acumulada')


for i, value in enumerate(explained_variance):
    plt.text(i, value + 0.01, f'{value:.3f}', ha='center', va='bottom', fontsize=12) 

plt.grid(True, linestyle='--', alpha=0.7)

plt.xticks(rotation=45)
plt.ylabel('Varianza explicada')
plt.title('Varianza explicada por cada componente (y acumulada)', fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()

fig.write_html('grafico_interactivo.html')

varianza_total = np.sum(explained_variance)
print(f"Varianza total explicada por los primeros dos componentes: {varianza_total}")

#Grafico de codo

pca_full = PCA()
pca_full.fit(data_scaled)

explained_var = pca_full.explained_variance_ratio_
componentes = range(1, len(explained_var) + 1)

plt.figure(figsize=(8, 5))
plt.plot(componentes, explained_var, marker='o', linestyle='--', color='navy', linewidth=1.8)

for i, var in enumerate(explained_var):
    plt.text(componentes[i], var + 0.005, f"{var:.2f}", ha='center', fontsize=9, color='black')

plt.title('Gráfico del Codo (Scree Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Número de Componentes Principales', fontsize=12)
plt.ylabel('Proporción de Varianza Explicada', fontsize=12)
plt.xticks(componentes)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

#Loadings

variables = [
    "Renta_media",
    "PIB_PP",
    "Precio_m2",
     "IPV",
     "IPC",
    "Tasa_empleo",
    "Δ_población",
    "Vivienda_nueva",
    "Num_Hipotecas",
]

df_años = df[df["Año"].isin([2015, 2018, 2022])]

df_años = df_años.dropna(subset=variables)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_años[variables])

pca = PCA(n_components=3)
pca.fit(data_scaled)

loadings = pd.DataFrame(
    pca.components_.T, 
    columns=[f'PC{i+1}' for i in range(3)],  
    index=variables  
)

print("🔍 Cargas (loadings) de las variables en los 3 primeros componentes:")
print(loadings.round(3))

plt.figure(figsize=(10, 6))
sns.heatmap(loadings, annot=True, cmap='coolwarm', fmt='.3f', linewidths=0.5)
plt.title('Cargas (Loadings) de las Variables en los 3 Primeros Componentes Principales', fontsize=14)
plt.ylabel('Variables', fontsize=12)
plt.xlabel('Componentes Principales', fontsize=12)
plt.tight_layout()
plt.show()
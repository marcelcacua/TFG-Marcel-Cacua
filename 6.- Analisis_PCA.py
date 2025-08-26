from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

file_path = "C:\\Users\\marce\\Desktop\\TFG\\CORRECCIÓN FINAL\\Python_TFG\\variables_accesibilidad_vivienda.xlsx"
df = pd.read_excel(file_path)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Analisis PCA con tres componentes principales 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df = df.rename(columns={
    'Tasa_esfuerzo': 'Tasa_esfuerzo',
    'Renat_Media_por_hogar ': 'Renta_media',
    'PIB_per_capita_provincial': 'PIB_PP',
    'Precio_m2': 'Precio_m2',
    'IPV' : 'IPV',
    'IPC' : 'IPC',
    'Tasa_empleo': 'Tasa_empleo',
    'Tasa_crecimiento_población': 'Δ_población',
    'Numero_vivienda_terminadas': 'Vivienda_nueva',
    'Numero_hipotecas' : 'Num_Hipotecas',
})
variables = [
    "Tasa_esfuerzo",
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

# Filtrar por años
df_años = df[df["Año"].isin([2015, 2018, 2022])]

# Estandarización
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_años[variables])

# PCA con 3 componentes
pca = PCA(n_components=3)
principal_components = pca.fit_transform(data_scaled)

# Crear DataFrame con los componentes principales
columns = [f'PC{i+1}' for i in range(3)]
pca_df = pd.DataFrame(principal_components, columns=columns)
pca_df['Año'] = df_años['Año'].values

# Varianza explicada
explained_variance = pca.explained_variance_ratio_
cumulative_variance = explained_variance.cumsum()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gráfico de varianza explicada y acumulada
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Se procede a realizar un grafico de barras mixto, donde las barras nos muestran la varianza explicada de cada componente principal,
#Mientras que la linea naranja nos refleja la variuanza explicativa acumulada.

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=columns, y=explained_variance, color='#1f77b4', label='Varianza individual')
sns.lineplot(x=columns, y=cumulative_variance, marker='o', color='#ff7f0e', label='Varianza acumulada')

for i, value in enumerate(explained_variance):
    ax.text(i, value/2, f'{value:.3f}', ha='center', va='center', color='white', fontsize=11, fontweight='bold')
for i, value in enumerate(cumulative_variance):
    plt.text(i, value + 0.01, f'{value:.3f}', ha='center', va='bottom', fontsize=12) 

plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.ylabel('Varianza explicada')
plt.title('Varianza explicada por cada componente (y acumulada)', fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()

varianza_total = np.sum(explained_variance)
print(f"Varianza total explicada por los primeros dos componentes: {varianza_total}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gráfico de Codo
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Posteriormente se procede a realiza un grafico de codo.De esta manera conoceremos el valor de los autovalores de cada componente principal. 
#En el caso de que los mismos sean <1 nos indicara que ese componente principal explica menos que una variable misma del modelo.

pca_full = PCA()
pca_full.fit(data_scaled)

autovalores = pca_full.explained_variance_
varianza_ratio = pca_full.explained_variance_ratio_

componentes = np.arange(1, len(autovalores) + 1)

plt.figure(figsize=(8, 5))
plt.plot(componentes, autovalores, marker='o', linestyle='--', color='navy', linewidth=1.8, label='Autovalor')

for i, val in enumerate(autovalores):
    plt.text(componentes[i], val + 0.1, f"{val:.2f}", ha='center', fontsize=9, color='navy')

plt.title('Gráfico del Codo (Scree Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Número de Componentes Principales', fontsize=12)
plt.ylabel('Autovalor', fontsize=12)
plt.xticks(componentes)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gráfico de Loadings
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Se procede a realizar un mapa de calor de las cargas que representa cada componente principal, destacando de esta manera sus principales caracteristicas.

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Gráfico de dispersión 3D de los tres primeros componentes principales
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

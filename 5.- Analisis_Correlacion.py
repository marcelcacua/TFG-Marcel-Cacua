import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

#TRES MATRICES DE CORRELACIÓN 

file_path = "C:\\Users\\marce\\Desktop\\TFG\\Copia de variables_accesibilidad_vivienda.xlsx"
df = pd.read_excel(file_path)

df.columns
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

sns.set(style="white", font_scale=1.2)

fig, axes = plt.subplots(1, 3, figsize=(15, 7))
años = [2015, 2018, 2022]

for i, año in enumerate(años):
    df_año = df[df["Año"] == año]
    corr = df_año[variables].corr(method='pearson')

    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', center=0,
                square=True, cbar=False, ax=axes[i], annot_kws={"size": 10})
    axes[i].set_title(f"Matriz de correlación - {año}", fontsize=10)

    axes[i].tick_params(axis='both', which='major', labelsize=8)

plt.tight_layout()
plt.show()

#MATRIZ DE CORRELACIÓN UNICA 

df.columns
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
    'Numero_hipotecas' : 'Num_Hipotecas',
    'IPV' : 'IPV',
    'Importe_medio_hipotecas' : 'Importe_hipotecas'
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
print(variables)

sns.set(style="white", font_scale=0.9)

df_años = df[df["Año"].isin([2015, 2018, 2022])]

corr = df_años[variables].corr(method='pearson')

plt.figure(figsize=(8, 6))

sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', center=0,
            square=True, cbar=True, annot_kws={"size": 10})

plt.title("Matriz de correlación para 2015-2018-2022", fontsize=12)

plt.tight_layout()
plt.show()
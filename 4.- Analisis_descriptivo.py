import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#REALIZACIÓN DE HISTOGRAMAS DE LAS VARIABLES ESTUDIADAS

df = pd.read_excel("C:\\Users\\marce\\Desktop\\TFG\\CORRECCIÓN FINAL\\variables_accesibilidad_vivienda.xlsx")

df = df.rename(columns={
    'Tasa_esfuerzo': 'Tasa_esfuerzo',
    'Renat_Media_por_hogar ': 'Renta_media',
    'PIB_per_capita_provincial': 'PIB_PP',
    'Precio_m2': 'Precio_m2',
    'Tasa_empleo': 'Tasa_empleo',
    'Tasa_crecimiento_población': 'Δ_población',
    'Numero_vivienda_terminadas': 'Vivienda_nueva',
    'Numero_hipotecas' : 'Num_Hipotecas',
    'IPV' : 'IPV',
})

vars_num = [col for col in df.columns if col != 'Año']

for col in vars_num:
    g = sns.FacetGrid(df, col="Año", col_wrap=3, height=4, sharex=False, sharey=False)
    g.map(sns.histplot, col, bins=30, kde=True, color='skyblue')
    g.set_titles(col_template="{col_name}")
    g.set_axis_labels(col, "Frecuencia")


    g.fig.suptitle(f"Histograma de {col} por Año", fontsize=14, y=1.05)

    
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)  
    plt.show()
#--------------------------------------------------------------------------------------------------------------------

#RESULTADOS DEL ANALISIS DESCRIPTIVO

variables = [
    'Tasa_esfuerzo',
    'Renta_media',
    'PIB_PP',
    'Precio_m2',
    'Tasa_empleo',
    'Δ_población',
    'Vivienda_nueva',
    'Num_Hipotecas',
    'IPV',
    'IPC'
]

def iqr(x):
    return x.quantile(0.75) - x.quantile(0.25)

stats = (
    df.groupby('Año')[variables]
      .agg(['mean', 'median', iqr, 'std', 'min', 'max'])
)

stats.columns = ['_'.join(col).strip() for col in stats.columns.values]
stats = stats.reset_index()

print(stats)
stats.columns

pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

pd.set_option('display.width', None)

print(stats)

stats.to_excel("C:\\Users\\marce\\Desktop\\TFG\\CORRECCIÓN FINAL\\Analisis_Descriptivo_Resultados_2.xlsx", index=False)
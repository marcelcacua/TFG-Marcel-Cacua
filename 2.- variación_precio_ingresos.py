#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VARIACIÓN DEL PRECIO DE LA VIVIENDA CON RESPECTO A LA RENTA NETA MEDIA DE LOS HOGARES
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("C:\\Users\\marce\\Desktop\\TFG\\POR PROVINCIAS\\Variación precio y ingresos\\Libro2.xls")
df.columns

x = np.arange(len(df))
width = 0.4

fig, ax = plt.subplots(figsize=(18, 8))
bars1 = ax.bar(x - width/2, df['Variacion de los precios vivienda'], width, label='Variación del Precio de la Vivienda(m2)', color='#1f77b4', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, df['Variación de la renta media'], width, label='Variación de los Ingresos Medios por Hogar', color='#2ca02c', edgecolor='black', linewidth=0.5)

ax.set_ylabel('Variación (%)')
ax.set_title('Comparación de la Tasa de Variación del Precio de la Vivienda e Ingresos Medios (2015-2022)')
ax.set_xticks(x)
ax.set_xticklabels(df['Provincia '], rotation=90)
ax.legend()

ax.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

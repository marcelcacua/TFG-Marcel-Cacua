#----------------------------------------------------------------------------------------------------------------------------------------------------------
#EVOLUCIÓN DE LOS PRECIOS DE LA VIVIENDA
#----------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:\\Users\\marce\\Desktop\\TFG\\POR PROVINCIAS\\Precio_m2\\PRECIOS 2022-2018-2015.xls")
df.columns
print(df.columns.tolist())

sns.set(style="whitegrid", font_scale=1.1)
plt.rcParams["font.family"] = "DejaVu Sans"

df.columns = df.columns.str.strip()
df.columns = [int(col) if str(col).isdigit() else col for col in df.columns]

df['Crecimiento'] = df[2022] - df[2015]

top_crecimiento = df.sort_values(by='Crecimiento', ascending=False).head(10)['Provincias'].tolist()

df_melted = df.melt(id_vars=['Provincias', 'Crecimiento'],
                    value_vars=[2015, 2018, 2022],
                    var_name='Año', value_name='Precio')
df_melted['Año'] = df_melted['Año'].astype(str)

plt.figure(figsize=(14, 7))

colores = sns.color_palette("tab10", n_colors=10)
color_map = {prov: colores[i] for i, prov in enumerate(top_crecimiento)}

for provincia in df['Provincias']:
    datos_prov = df_melted[df_melted['Provincias'] == provincia]
    if provincia in top_crecimiento:
        color = color_map[provincia]
        plt.plot(datos_prov['Año'], datos_prov['Precio'], label=provincia,
                 linewidth=2.5, color=color, marker='o')
    else:
        plt.plot(datos_prov['Año'], datos_prov['Precio'], color='lightgrey', alpha=0.3, linewidth=1)

plt.title('Evolución del precio de la vivienda (€/m²) por provincia entre 2015 y 2022', fontsize=16)
plt.xlabel('Año')
plt.ylabel('Precio (€/m²)')
plt.xticks(['2015', '2018', '2022'])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.legend(
    title='Top 10 provincias con mayor crecimiento',
    loc='upper left',
    fontsize=6,          
    title_fontsize=8     
)
plt.show()

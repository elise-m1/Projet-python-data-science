import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# --- 1. Préparation des données d'implantations ---
file_name = "fr-esr-implantations_etablissements_d_enseignement_superieur_publics (2).csv"
df = pd.read_csv(file_name)


# Nettoyage et conversion des coordonnées
df_geo = df.dropna(subset=['Géolocalisation']).copy()
df_geo[['latitude', 'longitude']] = df_geo['Géolocalisation'].str.split(', ', expand=True)
df_geo['latitude'] = pd.to_numeric(df_geo['latitude'], errors='coerce')
df_geo['longitude'] = pd.to_numeric(df_geo['longitude'], errors='coerce')
df_geo.dropna(subset=['latitude', 'longitude'], inplace=True)

geometry = [Point(xy) for xy in zip(df_geo['longitude'], df_geo['latitude'])]
gdf = gpd.GeoDataFrame(df_geo, geometry=geometry, crs="EPSG:4326")

# Filtrage pour la visualisation (Top 10 Régions)
top_regions = gdf['Région'].value_counts().head(10).index.tolist()
gdf_plot = gdf[gdf['Région'].isin(top_regions)].copy()
gdf_plot['Région'] = gdf_plot['Région'].astype('category')

# --- 2. Génération de la carte ---
fig, ax = plt.subplots(1, 1, figsize=(15, 15))

# TRACÉ DE LA FRONTIÈRE FRANÇAISE (utilise le jeu de données GeoPandas 'naturalearth_lowres')
try:
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    france_border = world[world['name'] == 'France']
    
    # Tracé de la frontière en fond
    france_border.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.7, alpha=0.5)
except Exception as e:
    # Ce bloc sera exécuté ici en raison de l'erreur fiona
    print(f"La frontière n'a pas pu être tracée dans cet environnement. Erreur: {e}")


# TRACÉ DES POINTS (IMPLANTATIONS COLORÉES)
gdf_plot.plot(column='Région', ax=ax, legend=True,
              markersize=5, cmap='tab20', alpha=0.8,
              legend_kwds={'loc': 'lower left', 'title': 'Région (Top 10)', 'fontsize': 10})

# 3. Définir les limites et les titres
ax.set_xlim(-5.5, 9.5)
ax.set_ylim(41, 51)
ax.set_title("Implantations des Établissements d'Enseignement Supérieur Publics par Région (avec Frontière)", fontsize=16)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Sauvegarder la figure
plt.savefig("france_esr_map_final.png")
plt.show() # Pour afficher le résultat
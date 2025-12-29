import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# 1. Chargement du fichier CSV
file_path = 'fr-esr-implantations_etablissements_d_enseignement_superieur_publics.csv'
df = pd.read_csv(file_path, sep=';')

# 2. Préparation des données
# On supprime les lignes sans coordonnées
df = df.dropna(subset=['Géolocalisation'])
# On sépare la colonne 'Géolocalisation' (ex: "48.85, 2.35") en deux colonnes numériques
df[['lat', 'lon']] = df['Géolocalisation'].str.split(',', expand=True).astype(float)

# 3. Création du GeoDataFrame
# Le format GeoJSON/GeoPandas utilise l'ordre (Longitude, Latitude)
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# 4. Filtrage pour la France métropolitaine (pour une meilleure visibilité)
# On limite aux longitudes entre -5 et 10 et latitudes entre 41 et 52
gdf_metropole = gdf[(gdf['lon'] > -5) & (gdf['lon'] < 10) & (gdf['lat'] > 41) & (gdf['lat'] < 52)]

# 5. Génération de la carte
fig, ax = plt.subplots(figsize=(12, 12))

# Affichage des points
# La couleur et la transparence (alpha) permettent de voir les zones de forte densité (ex: Paris, Lyon)
gdf_metropole.plot(ax=ax, 
                   markersize=12, 
                   color='#0055A4', # Bleu institutionnel
                   alpha=0.5, 
                   edgecolor='white', 
                   linewidth=0.3,
                   label='Établissements ESR')

# Habillage de la carte
plt.title("Carte des implantations de l'enseignement supérieur public", fontsize=16, fontweight='bold')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.3)

# Sauvegarde de l'image
plt.savefig('carte_esr_geopandas.png', dpi=300, bbox_inches='tight')
plt.show()

print("La carte a été générée : carte_esr_geopandas.png")

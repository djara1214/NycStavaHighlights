import pandas as pd 
import polyline
from shapely.geometry import LineString
import geopandas as gpd



def decode_polyline_to_list(df, column_name):
    def decode_polyline_coords(encoded_polyline):
        coords = polyline.decode(encoded_polyline)
        reordered_coords = [[lon, lat] for lat, lon in coords]  # Reorder (lat, lon) to (lon, lat)
        return reordered_coords

    df['coordinates'] = df[column_name].apply(decode_polyline_coords)

    return df


df=pd.read_csv('Seg_with_poly.csv')
df = df.drop('Unnamed: 0', axis=1)  #Cleanup

 #Decode column of Polypoints - Outputs correct form for Geojson
df=decode_polyline_to_list(df, 'polyPoints')

df = df.drop('polyPoints', axis=1)  #Cleanup

# Creates GeoJson
geometry = [LineString(coords) for coords in df['coordinates']]
gdf = gpd.GeoDataFrame(df, geometry=geometry)
geojson_str = gdf.to_json(indent=2)

#Save File
with open('coord_json.geojson', 'w') as file:
    file.write(geojson_str)


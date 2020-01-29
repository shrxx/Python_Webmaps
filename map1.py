import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])


map = folium.Map(
    location=[38.58, -99.09],
    tiles='CartoDB Positron',
    zoom_start=6
)

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="Hi, I'm Volcano",
            icon=folium.Icon(color='green')
        )
    )

map.add_child(fg)

map.save("Map1.html")

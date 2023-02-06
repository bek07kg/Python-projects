import folium

map = folium.map(
    location = [-19.932452, -43.937944],
    titles = "Stamen Terrain",
    zoom_start = 16
)

folium.Marker(
	[-19.932452, -43.937944],
	popup = '<i>Praca da Liberdade</i>'
	tooltip = 'Clique aqui'
).add.to(map)

map.save('D:/Download/map.html')
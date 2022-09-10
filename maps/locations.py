import folium
import json
import datetime

# loads jsonfile


def load_json(file):
    with open(file) as data:
        return json.load(data)


# store json file
apple_locations = load_json('locations.json')



time = datetime.datetime.now()
current_hour = time.hour


def location_color(location, open_color, closed_color):
    if current_hour > location['open hours'][0] and current_hour < location['open hours'][1]:
        return open_color
    else:
        return closed_color


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, titles='Stamen Terrain')

fga = folium.FeatureGroup(name='Apple Stores')

for apple_location in apple_locations:
    fga.add_child(folium.CircleMarker(location=apple_location['coordinators'], radius = 12, popup=apple_location['name'], 
    fill_color=location_color(apple_location, 'green', 'red'), color = 'blue', fill = True,fill_opacity = 0.7))








fgb = folium.FeatureGroup(name='Population')


fgb.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 30000000
else 'yellow' if 30000000 <= x['properties']['POP2005'] < 60000000
else 'DarkOrange' if 60000000 <= x['properties']['POP2005'] < 100000000 else 'red'}))


map.add_child(fga)

map.add_child(fgb)
map.add_child(folium.LayerControl())

map.save('Map1.html')

print(current_hour)

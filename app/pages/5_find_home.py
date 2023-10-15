import folium
import streamlit_folium as st_folium
import googlemaps
import numpy as np
import streamlit as st
import dotenv
import os

dotenv.load_dotenv()

gmaps = googlemaps.Client(key=os.getenv("GOOGLE_API_KEY"))

st.title("Find my Home")

start = "1868 Floribunda Avenue, Hillsborough, CA"
end = "Ayrshire Farm Lane, Stanford, CA"

directions_result = gmaps.directions(start, end)

# Geocode start and end locations
start_loc = gmaps.geocode(start)[0]['geometry']['location']
end_loc = gmaps.geocode(end)[0]['geometry']['location']

directions_result = gmaps.directions(start, end, mode="walking")

duration_value_s = directions_result[0]['legs'][0]['duration']['value']
duration_text = directions_result[0]['legs'][0]['duration']['text']
distance_value_m = directions_result[0]['legs'][0]['distance']['value']
distance_text = directions_result[0]['legs'][0]['distance']['text']

coordinates = np.zeros((int(len(directions_result[0]['legs'][0]['steps'])), 2))
i = 0
for step in directions_result[0]['legs'][0]['steps']:

    coordinates[i, 0] = step['start_location']['lat']
    coordinates[i, 1] = step['start_location']['lng']
    i += 1
    #coordinates[1, i] = step['end_location']

st.write('Duration: ', duration_text)
st.write('Distance: ', distance_text)

if duration_value_s/60 > 15:
    st.write('Do you have a ride home or should I book a ride for you?')

mid_loc_lat = (start_loc['lat'] + end_loc['lat'])/2
mid_loc_lng = (start_loc['lng'] + end_loc['lng'])/2


# Create map and add markers
m = folium.Map(location=[mid_loc_lat, mid_loc_lng], zoom_start=10)
folium.Marker(location=[start_loc['lat'], start_loc['lng']], popup='Start').add_to(m)
my_PolyLine=folium.PolyLine(locations=coordinates,weight=5)
m.add_child(my_PolyLine)
folium.Marker(location=[end_loc['lat'], end_loc['lng']], popup='End').add_to(m)

# Display Map
st_data = st_folium.folium_static(m)

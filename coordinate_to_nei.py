from pygeocoder import Geocoder

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(query, from_sensor=False):
    query = query.encode('utf-8')
    results = Geocoder.geocode(query).coordinates
    print(results)

get_coordinates("122 Westway, Greenbelt, MD 20742, USA", False)
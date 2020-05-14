import json
import sys

import config
import googlemaps

gmaps = googlemaps.Client(key=config.api_key)


def get_ids(location):
    with open('public/locations.json') as f:
        data = json.load(f)
        current_location = data[location]
        stores = gmaps.places_nearby(
            keyword=current_location['search'],
            type=current_location['type'],
            location=current_location['location'],
            radius=current_location['radius']
        )
        return stores['results']


print(get_ids(sys.argv[1]))

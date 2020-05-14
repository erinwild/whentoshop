import json

import config
import populartimes

all_locations = []
location_number = 0
locations_file = 'public/locations.json'
all_results_file = 'public/data/allresults.json'


def scrape_data(coords):
    popular_results = []

    for key in coords['ids']:
        result = populartimes.get_id(config.api_key, key)
        if 'populartimes' in result:
            popular_results.append(result)
            all_locations.append(result)

    filename = 'public/data/' + coords['name'] + '.json'
    with open(filename, 'w') as outfile:
        json.dump(popular_results, outfile)


with open(locations_file) as f:
    data = json.load(f)
    for key in data:
        location = data[key]
        scrape_data(location)
        location_number = location_number + 1
        locations_length = len(data)
        if location_number is locations_length:
            with open(all_results_file, 'w') as outfile:
                json.dump(all_locations, outfile)

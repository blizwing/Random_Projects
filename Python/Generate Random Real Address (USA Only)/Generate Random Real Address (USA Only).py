import requests
import random

# Constants
STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
    "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
    "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]
LOCATION_TYPES = ["hospital", "school", "restaurant", "services"]
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


# Function to get a random state
def get_random_state():
    return random.choice(STATES)


# Function to fetch cities in a state
def fetch_cities(state):
    url = f"https://nominatim.openstreetmap.org/search?state={state}&country=USA&city&format=json"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to fetch cities. Retrying...")
        return fetch_cities(get_random_state())

    cities = response.json()
    if cities:
        selected_city = random.choice(cities)
        bounding_box = selected_city['boundingbox']
        fetch_locations(bounding_box)
    else:
        print("No cities found. Retrying...")
        fetch_cities(get_random_state())


# Function to fetch locations within a city
def fetch_locations(bounding_box):
    location_type = random.choice(LOCATION_TYPES)
    north, south, east, west = bounding_box
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location_type}&bounded=1&viewbox={west},{north},{east},{south}&addressdetails=1"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to fetch locations. Retrying...")
        return fetch_cities(get_random_state())

    locations = response.json()
    if locations:
        selected_location = None
        for location in locations:
            if 'postcode' in location['address']:
                selected_location = location
                break

        if selected_location and 'postcode' in selected_location['address']:
            latitude = selected_location['lat']
            longitude = selected_location['lon']
            complete_address = selected_location['display_name']
            city = selected_location['address'].get('city') or selected_location['address'].get('town') or \
                   selected_location['address'].get('village')
            state = selected_location['address'].get('state')
            country = selected_location['address'].get('country')
            postcode = selected_location['address'].get('postcode')

            print(f"Complete Address: {complete_address}")
            print(f"Postcode: {postcode}, City: {city}, State: {state}, Country: {country}")
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("No valid postcode found. Retrying...")
            fetch_cities(get_random_state())
    else:
        print("No specific locations found. Retrying...")
        fetch_cities(get_random_state())


# Start the process
fetch_cities(get_random_state())

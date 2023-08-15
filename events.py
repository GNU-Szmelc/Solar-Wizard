from datetime import datetime, timedelta
from skyfield.api import Topos, load
from pprint import pprint

# Ask user for latitude and longitude
latitude = float(input("Enter your latitude (in decimal degrees): "))
longitude = float(input("Enter your longitude (in decimal degrees): "))

# Load astronomical data
ts = load.timescale()
planets = load('de421.bsp')  # You can download this file from the Skyfield website

# Create a location using user's coordinates
user_location = Topos(latitude_degrees=latitude, longitude_degrees=longitude)

# Calculate the start and end dates for the next week
today = datetime.now()
next_week = today + timedelta(days=7)

# Load the TLE data for celestial objects
tle_url = 'http://www.celestrak.com/NORAD/elements/stations.txt'  # Example TLE URL
satellites = load.tle_file(tle_url)

# Find visible satellites during the next week
visible_satellites = []

for sat in satellites:
    difference = sat - user_location
    topocentric = difference.at(ts.utc(next_week.year, next_week.month, next_week.day))
    alt, az, d = topocentric.altaz()
    
    if alt.degrees > 10:  # Adjust this threshold as needed
        visible_satellites.append(sat)

# Print upcoming celestial events
print("\nUpcoming Celestial Events for the Next Week:\n")

# Example of meteor shower data (you can replace this with actual meteor shower data)
meteor_showers = [
    {"name": "Perseids Meteor Shower", "start_date": next_week.strftime('%Y-%m-%d'), "end_date": (next_week + timedelta(days=2)).strftime('%Y-%m-%d')},
]

pprint(meteor_showers)

# Print visible satellites
print("\nVisible Satellites for the Next Week:\n")
for sat in visible_satellites:
    print(sat.name)

# You can add more logic here to fetch and display other celestial events like eclipses.

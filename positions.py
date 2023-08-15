import ephem
import datetime
from skyfield.api import Topos, load

def identify_celestial_objects(latitude, longitude, date_time=None):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    
    if date_time is None:
        observer.date = datetime.datetime.utcnow()
    else:
        observer.date = date_time

    sun = ephem.Sun(observer)
    moon = ephem.Moon(observer)
    planets = {
        "Mercury": ephem.Mercury(observer),
        "Venus": ephem.Venus(observer),
        "Mars": ephem.Mars(observer),
        "Jupiter": ephem.Jupiter(observer),
        "Saturn": ephem.Saturn(observer),
        "Uranus": ephem.Uranus(observer),
        "Neptune": ephem.Neptune(observer)
    }

    # Create a list of celestial objects including the Sun, Moon, and planets
    celestial_objects = [(sun, "Sun"), (moon, "Moon")]
    for planet_name, planet in planets.items():
        celestial_objects.append((planet, planet_name))

    # Sort the celestial objects based on their altitude (angle above the horizon)
    celestial_objects.sort(reverse=True, key=lambda x: x[0].alt)

    # Display the sorted celestial objects
    for obj, name in celestial_objects:
        print(f"{name}: Altitude = {obj.alt}, Azimuth = {obj.az}")

if __name__ == "__main__":
    user_latitude = float(input("Enter your latitude (degrees): "))
    user_longitude = float(input("Enter your longitude (degrees): "))
    user_date_time = input("Enter date and time (YYYY/MM/DD HH:MM:SS) or press Enter for current time: ")

    if user_date_time:
        user_date_time = ephem.Date(user_date_time)
    else:
        user_date_time = None

    identify_celestial_objects(user_latitude, user_longitude, user_date_time)

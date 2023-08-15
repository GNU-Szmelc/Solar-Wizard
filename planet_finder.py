import ephem
from datetime import datetime, timedelta

def get_upcoming_events(observer, start_date, end_date, selected_planet):
    planets = {
        'Mercury': ephem.Mercury(),
        'Venus': ephem.Venus(),
        'Mars': ephem.Mars(),
        'Jupiter': ephem.Jupiter(),
        'Saturn': ephem.Saturn(),
        'Uranus': ephem.Uranus(),
        'Neptune': ephem.Neptune(),
    }

    t = ephem.Date(start_date)
    end_t = ephem.Date(end_date)

    events = []

    while t < end_t:
        planet = planets[selected_planet]
        planet.compute(observer)
        alt_deg = planet.alt * 180.0 / ephem.pi
        if alt_deg > 0 and alt_deg < 30:
            event = {
                'date': ephem.localtime(t).isoformat(),
                'planet': selected_planet,
                'altitude': alt_deg,
            }
            events.append(event)

        t += ephem.hour  # Increment by one hour using ephem.Date

    return events

if __name__ == '__main__':
    latitude = input("Enter your latitude (degrees): ")
    longitude = input("Enter your longitude (degrees): ")

    observer = ephem.Observer()
    observer.lat = latitude
    observer.lon = longitude

    today = datetime.utcnow().date()
    start_date = datetime(today.year, today.month, today.day)
    end_date = start_date + timedelta(days=1)

    selected_planet = input("Enter the planet you want to check (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ").capitalize()

    upcoming_events = get_upcoming_events(observer, start_date, end_date, selected_planet)

    print(f'Upcoming Celestial Events for {selected_planet} Today:')
    for event in upcoming_events:
        print(f"Date: {event['date']}")
        print(f"Planet: {event['planet']}")
        print(f"Altitude: {event['altitude']} degrees")
        print('-' * 40)

    # Save log to file
    log_filename = f"{selected_planet}_{today}.txt"
    with open(log_filename, 'w') as log_file:
        log_file.write(f'Upcoming Celestial Events for {selected_planet} Today:\n')
        for event in upcoming_events:
            log_file.write(f"Date: {event['date']}\n")
            log_file.write(f"Planet: {event['planet']}\n")
            log_file.write(f"Altitude: {event['altitude']} degrees\n")
            log_file.write('-' * 40 + '\n')

    print(f"Log saved to {log_filename}")

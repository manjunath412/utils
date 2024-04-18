import pandas as pd
import pgeocode
from timezonefinder import TimezoneFinder

def map_timezone_to_region(timezone):
    # Mapping of detailed timezones to general regions (most popular)
    # in US and PR
    mapping = {
        'America/New_York': 'Eastern',
        'America/Detroit': 'Eastern',
        'America/Kentucky/Louisville': 'Eastern',
        'America/Kentucky/Monticello': 'Eastern',
        'America/Indiana/Indianapolis': 'Eastern',
        'America/Indiana/Vincennes': 'Eastern',
        'America/Indiana/Winamac': 'Eastern',
        'America/Indiana/Marengo': 'Eastern',
        'America/Indiana/Petersburg': 'Eastern',
        'America/Indiana/Vevay': 'Eastern',
        'America/Chicago': 'Central',
        'America/Indiana/Tell_City': 'Central',
        'America/Indiana/Knox': 'Central',
        'America/Menominee': 'Central',
        'America/North_Dakota/Center': 'Central',
        'America/North_Dakota/New_Salem': 'Central',
        'America/North_Dakota/Beulah': 'Central',
        'America/Denver': 'Mountain',
        'America/Boise': 'Mountain',
        'America/Phoenix': 'Mountain',
        'America/Los_Angeles': 'Pacific',
        'America/Anchorage': 'Alaska',
        'Pacific/Honolulu': 'Hawaii',
        'America/Puerto_Rico': 'Atlantic'
    }
    return mapping.get(timezone, 'Unknown')  

def get_timezone_by_zip(zip_code, country='US'): #default US country code else pass code
    nomi = pgeocode.Nominatim(country)
    location = nomi.query_postal_code(zip_code)
    if location is not None and not pd.isna(location.latitude):
        latitude, longitude = location.latitude, location.longitude
        # print(f"Latitude and Longitude for ZIP code {zip_code} are: {latitude}, {longitude}")
        tf = TimezoneFinder()
        detailed_timezone = tf.timezone_at(lat=latitude, lng=longitude)
        if detailed_timezone:
            general_region = map_timezone_to_region(detailed_timezone)
            return general_region
        else:
            return "No timezone found"
    else:
        return "Location not found"

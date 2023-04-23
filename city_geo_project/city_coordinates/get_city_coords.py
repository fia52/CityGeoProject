from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim

from city_geo_project.settings import USER_AGENT


def get_city_coords(city_name="Moscow"):
    geolocator = Nominatim(user_agent=USER_AGENT)
    res = geolocator.geocode(city_name)
    location = Point(x=res.latitude, y=res.longitude)
    return location

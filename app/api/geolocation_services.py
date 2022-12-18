import geopy.geocoders
from geopy.geocoders import Nominatim
from ssl import create_default_context, SSLContext
from certifi import where


def _create_ssl_context() -> SSLContext:
    return create_default_context(cafile=where())


def get_geolocation(latitude: str | float | int, longitude: str | float | int) -> str:
    geopy.geocoders.options.default_ssl_context = _create_ssl_context()
    geolocator = Nominatim(user_agent="photo_manager")
    location = geolocator.reverse(f"{latitude}, {longitude}", language="ru")
    return location.address
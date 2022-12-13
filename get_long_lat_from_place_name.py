from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


def get_long_lat_from_place_name(place_name):
    """
    Give place name in this format
    place_name = 'mumbai,maharashtra,india' (OR)
    place_name = 'mumbai, maharashtra, india' and combinations...

    and get output as
    { longitude: longitude_value, latitude: latitude_value }
    """

    place_name.replace(",", ",+")
    place_name.replace(" ", "+")
    BASE_MAPS_URL = "https://www.google.com/maps/place/"
    longitude, latitude = -1, -1

    try:
        req = Request(url=BASE_MAPS_URL + place_name)
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, "html.parser")
        for script in soup.find_all("script"):
            if "window.APP_INITIALIZATION_STATE=" in script.get_text():
                split_part = script.get_text().split("window.APP_INITIALIZATION_STATE=")
                _, longitude, latitude = (
                    split_part[1].split("],[")[0].strip("[[[").split(",")
                )
                break
    except Exception as e:
        print(place_name, "::", e)
    return {longitude: longitude, latitude: latitude}


print(get_long_lat_from_place_name("pandharpur,solapur, maharashtra"))

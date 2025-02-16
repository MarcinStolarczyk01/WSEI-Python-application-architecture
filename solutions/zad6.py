"""
Na podstawie danych z IMGW w formacie XML, dostępnych pod adresem
https://danepubliczne.imgw.pl/api/data/meteo/format/xml, napisz program, który
odczytuje dane, przetwarza informacje o prędkości wiatru z wybranych stacji i
wyświetla średnią prędkość wiatru na wykresie słupkowym.
"""

STATION_OF_INTEREST = ["siedlce", "tomaszów lubelski", "głodowo", "nowy sącz"]
STATION_WIND_SPEED_MAP = {}

import requests
import xml.etree.ElementTree as et

if __name__ == "__main__":

    url = "https://danepubliczne.imgw.pl/api/data/meteo/format/xml"
    response = requests.get(url).text
    element = et.fromstring(response)
    for station in element:
        if (
            station_name := station.find("nazwa_stacji").text.lower()
        ) in STATION_OF_INTEREST:
            wind_speed = station.find("wiatr_srednia_predkosc").text
            if wind_speed is None:
                wind_speed = "No data"
            STATION_WIND_SPEED_MAP[station_name] = wind_speed

    print(STATION_WIND_SPEED_MAP)

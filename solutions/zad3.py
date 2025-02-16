"""
Za pomocą API zwracającego informacje dot. uniwersytetów w danym państwie:
http://universities.hipolabs.com/search?country=<nazwa_kraju_eng> wyświetl
nazwy uniwersytetów z 20 wybranych krajów w postaci: {<nazwa_kraju>:
[<nazwa_uniwersytet1>, <nazwa_uniwersytet2>,...], …}. W celu przyspieszenia
pobierania danych, wykorzystaj moduł threading do realizacji wielowątkowego
pobierania informacji.
"""

from concurrent.futures.thread import ThreadPoolExecutor
import requests

url_base = "http://universities.hipolabs.com/search"


def get_uni_for_country(country_name: str, universities: dict):
    url = url_base + f"?country={country_name}"
    response = requests.get(url).json()
    names = [u.get("name", "unknown") for u in response]

    universities[country_name] = names


if __name__ == "__main__":
    countries = [
        "Turkey",
        "Poland",
        "Netherlands",
        "Germany",
        "Brazil",
        "France",
        "Italy",
        "Spain",
        "Portugal",
        "Croatia",
        "Mexico",
        "Canada",
        "Chile",
        "Israel",
        "China",
        "Japan",
        "Australia",
        "Austria",
        "Slovenia",
        "Hungary",
    ]
    universities_map = {}
    with ThreadPoolExecutor(max_workers=20) as executor:
        for country in countries:
            executor.submit(get_uni_for_country, country, universities_map)

    for country, unis in universities_map.items():
        print(f"{country}: {unis}")

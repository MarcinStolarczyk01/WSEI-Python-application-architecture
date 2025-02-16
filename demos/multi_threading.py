import requests
from bs4 import BeautifulSoup
import time
import logging
from concurrent.futures import ThreadPoolExecutor
import threading
from queue import Queue

logging.basicConfig(level="INFO")
titles = []


def download_site(url, session):
    global titles

    with session.get(url) as response:
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        event_titles = soup.find_all(
            "h3", class_="tribe-events-calendar-list__event-title"
        )

        for title_raw in event_titles:
            title = title_raw.text.strip()
            logging.info(f"Pobrano tytul: {title}")

            with threading.Lock():
                titles.append(title)


def download_all_sites(sites):
    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=100) as executor:
            args = [(url, session) for url in sites]
            for arg in args:
                executor.submit(download_site, *arg)


def demo():
    sites = [
        f"https://wsei.edu.pl/wydarzenia/lista/strona/{i}/?eventDisplay=past"
        for i in range(1, 11)
    ]
    start = time.time()
    download_all_sites(sites)
    logging.info(f"Pobrano {len(titles)} tytulow in {time.time() - start} seconds")


def get_cat_fact():
    url = "https://catfact.ninja/fact"
    return requests.get(url).json()


def task1(facts_num):
    with ThreadPoolExecutor(20) as executor:
        cat_facts = list(executor.map(lambda _: get_cat_fact(), range(facts_num)))
    return print(cat_facts)


def task2():
    q = Queue(2)
    products_counter = 0

    def producent():
        pass

    def consument():
        pass


if __name__ == "__main__":
    # demo()
    task1(20)

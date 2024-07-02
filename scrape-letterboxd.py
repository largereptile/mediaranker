from bs4 import BeautifulSoup
import requests
import time
import sys

def get_first_page(user):
    r = requests.get(f"https://letterboxd.com/{user}/films/")
    soup = BeautifulSoup(r.text, "html.parser")
    pages = soup.find_all("li", class_="paginate-page")
    if not pages:
        return soup, 1

    pages = int(pages[-1].find_all("a")[0].text)
    return soup, pages


def get_all_films(user):
    first_page, pages = get_first_page(user)
    page_html = [first_page]
    if pages > 1:
        for x in range(2, pages+1):
            r = requests.get(f"https://letterboxd.com/{user}/films/page/{x}/")
            page_html.append(BeautifulSoup(r.text, "html.parser"))
            time.sleep(0.5)

    films = []
    for soup in page_html:
        film_li = soup.find_all("li", class_="poster-container")
        for film in film_li:
            film_poster = film.find("div", class_="poster")
            film_id = film_poster.get("data-film-slug")
            rev = film.find("p", class_="poster-viewingdata")
            if rev is not None:
                rev = rev.find("span")
                if rev is not None:
                    rev = rev.text
                else:
                    rev = "None"
            else:
                rev = "None"
            films.append((film_id, rev))

    return films

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape-letterboxd.py <username>")
    
    target_user = sys.argv[1]

    with open(f"{target_user}_films.txt", "w", encoding="utf8") as f:
        for f_id, rev in get_all_films(target_user):
            f.write(f"{f_id} - {rev}\n")
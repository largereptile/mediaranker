# Letterboxd Film Ranker

This is a small project used to create a gaussian/bell curve for letterboxd rankings by using comparisons.
It uses both a scraper on the letterboxd website, and a profile username

## Requirements

- Python 3.x
- 'BeautifulSoup' package for web scraping
- 'requests' package

You can install these using

```sh
pip install beautifulsoup4 requests
```

## Usage

`main.py` is used to run the program with the Letterboxd username as a mandatory argument. You can also use the `--force` flag if you want to forcably rescan your account if you have rated new films since the last run.

```sh
python main.py <username> [--force]
```

- `<username>`: your Letterboxd username
- `--force`: Optional flag to force rescan
from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'


# helper function to scrape posts from hackernews
def scrape_posts():
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table2 = soup.select('table')[0]

    rows = [
        {
            'href': a.get('href'), 'text': a.string
        }
        for a in (table2.select('td.title a.storylink'))
    ]

    return rows

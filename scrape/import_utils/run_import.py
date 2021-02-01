import scrape.scrape_utils.hackernews as hackernews
import scrape.models as models


# function that imports posts from hackernews into our database
def run_import(session):
    # 1. scrape posts
    posts = hackernews.scrape_posts()

    # 2. put posts in our database
    for scraped_post in posts:
        models.save_post(session, scraped_post['href'], scraped_post['text'])

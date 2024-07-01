import random
import sys
import getopt
import argparse
import webbrowser
from random import choice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def search_stories(query, date_range, sort):
    driver = webdriver.Firefox()
    random_page = random.randint(0, 33)
    base_url = f'https://hn.algolia.com/?dateRange={date_range}&page={random_page}&prefix=false&query={query}&sort={sort}&type=story'
    driver.get(base_url)
    wait = WebDriverWait(driver, 5)
    assert "All | Search powered by Algolia" in driver.title
    links = wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.Story_title > a')))
    if not links:
        print("No stories found with given search criteria.")
        return
    link = choice(links)
    webbrowser.open(link.get_attribute('href'))
    driver.quit()


def main():
    help_message = """
    Usage python main.py [options]
    
    Options:
        -h, --help  Show this help message
        -q, --query=QUERY  Optional query for stories 
        -d, --date=DATE  Date range for stories: all, last24h, pastWeek, pastMonth, pastYear. Defaults to all
        -s, --sort=SORT  Sort stories: byDate, byPopularity. Defaults to byPopularity
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", help="Display this help message", action='store_true')
    parser.add_argument("-q", "--query", help="Optional query for stories")
    parser.add_argument("-d", "--date", help="Date range for stories: all, last24h, pastWeek, pastMonth, pastYear. Defaults to all")
    parser.add_argument("-s", "--sort", help="Sort stories: byDate, byPopularity. Defaults to byPopularity")
    args = parser.parse_args()
    query = None
    date_range = 'all'
    sort = 'byPopularity'
    if args.query:
        query = args.query
    elif args.date:
        date_range = args.date
    elif args.sort:
        sort = args.sort
    elif args.help:
        print(help_message)
        sys.exit(2)

    if query and date_range and sort:
        search_stories(query, date_range, sort)
    else:
        search_stories(query, date_range, sort)


if __name__ == "__main__":
    main()

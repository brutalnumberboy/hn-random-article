import random
import sys
import getopt
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
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hq:d:s:", ["--help", "--query=", "--date_range=", "--sort="])
    except getopt.GetoptError as err:
        print(err)
        print(help_message)
        sys.exit(2)
    query = None
    date_range = 'all'
    sort = 'byPopularity'
    for o, a in opts:
        if o in ("-h", "--help"):
            print(help_message)
            sys.exit(0)
        elif o in ("-q", "--query"):
            query = a
        elif o in ("-d", "--date_range"):
            date_range = a
        elif o in ("-s", "--sort"):
            sort = a
        else:
            assert False, "unhandled option"

    if query and date_range and sort:
        search_stories(query, date_range, sort)
    else:
        search_stories(query, date_range, sort)


if __name__ == "__main__":
    main()

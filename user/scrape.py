import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

from .models import *

# terms = ['lettuce','spinach','cucumber']
def get_source(url):
    """Return the source code for the provided URL.
    Args:
        url (string): URL of the page to scrape.
    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

# https://pubmed.ncbi.nlm.nih.gov/?term=lettuce

def scrape(term):
    try:
        message = "Starting scraping..."
        term = urllib.parse.quote_plus(term)
        response = get_source("https://pubmed.ncbi.nlm.nih.gov/?term=" + term)

        links = response.html.absolute_links

        plants = {'name': term, 'links': links}

        return save_function(plants)
    except Exception as e:
        message = "The scraping job failed"
        err = e



    return links

def save_function(plants):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            Scrape.objects.create(
                name = article['name'],
                link = article['links']
            )
            new_count += 1
        except Exception as e:
            print('failed')
            print(e)
            break
    return print('finished')
# for term in terms:
#
#     print(scrape('lettuce'))
# print(scrape('lettuce'))

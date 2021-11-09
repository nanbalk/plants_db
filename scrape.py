import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
terms = ['lettuce','spinach','cucumber']
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

    term = urllib.parse.quote_plus(term)
    response = get_source("https://pubmed.ncbi.nlm.nih.gov/?term=" + term)

    links = response.html.absolute_links
    # google_domains = ('https://www.google.',
    #                   'https://google.',
    #                   'https://webcache.googleusercontent.',
    #                   'http://webcache.googleusercontent.',
    #                   'https://policies.google.',
    #                   'https://support.google.',
    #                   'https://maps.google.')
    #
    # for url in links[:]:
    #     if url.startswith(google_domains):
    #         links.remove(url)

    return links
# for term in terms:
#
#     print(scrape('lettuce'))
print(scrape('lettuce'))

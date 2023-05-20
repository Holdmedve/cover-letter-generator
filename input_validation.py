import requests
from requests.exceptions import MissingSchema, ConnectionError


def is_form_incomplete(file, url):
    if file is None:
        return True
    if url is None or url == '':
        return True
    return False

def is_url_invalid(url):
    try:
        requests.get(url)
        return False
    except (MissingSchema, ConnectionError):
        return True

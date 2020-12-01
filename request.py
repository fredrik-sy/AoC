import requests

session = requests.Session()

with open('session', 'r') as session_cookie:
    session.cookies.set('session', session_cookie.read())


def get(url):
    response = session.get(url)
    response.raise_for_status()
    return response.text

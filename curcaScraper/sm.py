
from lxml import html
import requests

page = requests.get('http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/scrape/')
print(page.text)

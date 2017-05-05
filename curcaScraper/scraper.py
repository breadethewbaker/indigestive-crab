from lxml import html
import requests

page = requests.get('http://curca.buffalo.edu/students/research-opps.php')
tree = html.fromstring(page.content)

links = tree.xpath('//ul[@class="rops"]/li/a/attribute::href')
names = tree.xpath('//ul[@class="rops"]/li/a/text()')


for n in range(len(links)):
	page = requests.get("http://curca.buffalo.edu"+links[n])
	if "coding" in page.text or "programming" in page.text or "linux" in page.text:
		print(names[n])

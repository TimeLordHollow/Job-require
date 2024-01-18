from bs4 import BeautifulSoup #web scarper package
import requests
import pprint


url = "https://www.linkedin.com/jobs/no-experience-graphic-design-jobs-greater-houston?position=1&pageNum=0"

#request to get the html from the url
html= requests.get(url)

#get the html and covert it into text
soup = BeautifulSoup(html.text, 'html.parser')

#prints html
pprint.pprint(soup)

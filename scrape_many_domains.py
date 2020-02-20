import pandas 
import os
import time
from urllib.request import urlopen, Request
from tld import get_tld, get_fld

if not os.path.exists("domain_html"):
	os.mkdir("domain_html")

df = pandas.read_csv("domains.csv")


for link in df['domain_name']:
	f = open('domain_html/' +link, "wb")

	try: 
		print("Downloading (1st): ", link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		fld_link = get_fld('http://' + link)
		request_link = "http://www." + fld_link
		print(request_link)
		req = Request(url = request_link, headers = headers)
		response = urlopen(req)
		html = response.read()
		f.write(html)

	except:
		print("Downloading (2nd): ", link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		fld_link = get_fld('http://' + link)
		request_link = "http://" + fld_link
		req = Request(url = request_link, headers = headers)
		response = urlopen(req)
		html = response.read()
		f.write(html)

	f.close()
	time.sleep(2)



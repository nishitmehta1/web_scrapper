from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

filename = "nike_cr7.csv"
f = open(filename, "w")

for i in range(1,6):
	url = 'https://www.amazon.com/s/ref=sr_pg_'+ str(i) +'?rh=i%3Aaps%2Ck%3Anike+cr7&page=3&keywords=nike+cr7&ie=UTF8&qid=1535481489'

	client = uReq(url)
	webpage_html = client.read()
	client.close()

	html_page = soup(webpage_html, "html.parser")
	headers = "Name, Price\n"

	f.write(headers)

	div_containers = html_page.findAll("div", {"class" : "a-fixed-left-grid-inner"})

	for div_container in div_containers:
		name_temp = div_container.findAll("div", {"class:", "a-col-right"})[0]
		name = name_temp.div.div.a["title"]
		print(name)
		price = name_temp.find("span", {"class:", "a-offscreen"})
		if price != None:
			print(price.get_text())
			f.write(str(name).replace(",", "|") + "," + str(price.get_text()) + "\n")

f.close()
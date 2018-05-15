#Nama		: Nella Zabrina Pramata
#NIM		: 13516025

"""
-------------------------------------
IMPORT LIB
-------------------------------------
urllib2 : modul untuk menghandle url request
BeatifulSoup : modul untuk memparsing HTML/XML
json : data scrap disimpan dalam file json
time : untuk sleep saat scraping per tempat kos
"""
import py_compile
from bs4 import BeautifulSoup
import urllib.request
import json
import time

print("START SCRAPING HEHEHE")
"""
-------------------------------------
SCRAP THE HTML
-------------------------------------
"""
#request URL yang dimana urlnya adalah https://www.cari-kos.com/, dan simpan pada variabel 'main_page'
#some HTTP servers only allow requests coming from common browsers as opposed to scripts -- shg pakai Chrome/66.0.3359.139
#req = urllib.request.Request('http://mamikos.com/',
req_main_page = urllib.request.Request('https://www.cari-kos.com/', 
	headers = {'user-agent' : 'Chrome/66.0.3359.139 (Ubuntu 18 amd64) 13516025@std.stei.itb.ac.id'})
main_page = urllib.request.urlopen(req_main_page)
#membaca keseluruhan string dari 'page' dan simpan pada variabel 'main_HTMLcode'
main_HTMLcode = main_page.read().decode('utf-8') 


"""
-------------------------------------
SCRAP
-------------------------------------
"""
#scraping home
base_main = "https://www.cari-kos.com/"
HTMLmain = BeautifulSoup(main_HTMLcode, "html.parser")

for link in HTMLmain.find_all(attrs={"class": "col-lg-4 col-md-4 col-sm-6 col-xs-6"}):
	try:
		link_city = link.find("a")
		url_city = link_city["href"]
	except:
		continue
	#give name file for each daerah
	name_file = url_city.split("/")
	name_file = name_file[len(name_file)-1].split("?")[0]
	name_file = name_file.replace("-", " ")

	print("scraping " + name_file)

	#start scrapping from daerah
	data = {}
	data['kost'] = []

	req_city_page = urllib.request.Request(url_city, 
		headers = {'user-agent' : 'Chrome/66.0.3359.139 (Ubuntu 18 amd64) 13516025@std.stei.itb.ac.id'})
	city_page = urllib.request.urlopen(req_city_page)
	city_HTMLcode = city_page.read().decode('utf-8')
	HTMLcity = BeautifulSoup(city_HTMLcode, "html.parser")
	i = 1

	#just scraping 10 data from each daerah
	while (i <= 10):
		link_page = HTMLcity.find(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-xs-12"})
		try:
			link_kos = link_page.find("a")
			url_kos = link_kos["href"]
			i += 1
		except:
			continue

		#start scrapping from each kos
		time.sleep(1)
		req_kos_page = urllib.request.Request(url_kos, 
			headers = {'user-agent' : 'Chrome/66.0.3359.139 (Ubuntu 18 amd64) 13516025@std.stei.itb.ac.id'})
		kos_page = urllib.request.urlopen(req_kos_page)
		kos_HTMLcode = kos_page.read().decode('utf-8')
		HTMLkos = BeautifulSoup(kos_HTMLcode, "html.parser")
		title = HTMLkos.title.text

		price = HTMLkos.find(attrs={"class": "wrapper-priceDetailTop"})
		price = price.text

		#json file isi nya nama kos + harga
		data['kost'].append({title: price})

		kos_page.close()

	#save json from each city
	with open(name_file + '.json', 'w') as outfile:  
		json.dump(data, outfile)

	city_page.close()

main_page.close()
input("Press Enter to Exit.")

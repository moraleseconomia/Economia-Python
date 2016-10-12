# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:53:20 2016

@author: Deybi.Morales
"""
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(r)
response.xpath('//span/text()').extract()

from bs4 import BeautifulSoup
url="'https://www.procredit.com.ni/Pages/BancaPersonas/ServiciosFinancieros/MesaCambio.aspx'"
soup = BeautifulSoup(url, 'html.parser')
print(soup.prettify())


#from bs4 import BeautifulSoup
#import urllib
#r = urllib.urlopen('https://www.procredit.com.ni/Pages/BancaPersonas/ServiciosFinancieros/MesaCambio.aspx').read()
#soup = BeautifulSoup(r)
#print type(soup)
#print soup.prettify()[0:1000]

#rank = soup.find("div", {"class": "rank-box"}).h6.contents

#soup.find("table", {"class": "tblTasaCambio"})
#cambio=soup.find("table", {"class": "tblTasaCambio"})

#name = cambio.span.contents
#cambio.td.span.contents

#tabla = soup.find('table')
#trs = tabla.findAll('tr')

#for tr in trs:
#    tds = tr.findAll('td')
#    print tds

#tds.find("table", {"class":"ctl00_ctl33_g_14955031_6ad3_4d14_9ee1_6db74d84e354_lblCompra"})

#soup.find("span", {"ctl00_ctl33_g_14955031_6ad3_4d14_9ee1_6db74d84e354_lblCompra"})



#from bs4 import BeautifulSoup
#import requests
#url = raw_input("https://www.procredit.com.ni/Pages/BancaPersonas/ServiciosFinancieros/MesaCambio.aspx")

#r  = requests.get("https://www.procredit.com.ni/Pages/BancaPersonas/ServiciosFinancieros/MesaCambio.aspx" +url)
#data = r.text
#print ""

#soup = BeautifulSoup(data, 'lxml')
#soup.table.text


#for link in soup.find_all('tr'):
#    print(link.get('span'))


from lxml import html
import requests
page = requests.get('https://www.procredit.com.ni/Pages/BancaPersonas/ServiciosFinancieros/MesaCambio.aspx')
tree = html.fromstring(page.text)
tree.xpath('//span/text()')
tree.xpath('//span/text()')
row = tree.xpath('//span/text()')

row[8]
row[10]
row[12]




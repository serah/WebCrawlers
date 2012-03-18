#! /usr/bin/env 2.7

import urllib2
import re
from BeautifulSoup import BeautifulSoup


class ninecircuits:
	
	def initialize(self):
		# access the required page
		page = urllib2.urlopen("http://9circuits.com/store/products/?items_per_page=all")
		self.soup = BeautifulSoup(page)
		self.product_price()
		
	def product_price(self): # get all the product prices and save in a list
		productprices=[]
		# search for all occurrences of 'pricedisplay' in the html tags
		productprice = self.soup.findAll(attrs="pricedisplay")
		for p in productprice:
			# add the prices of products in the pricelist
			productprices.append(p.string)
		return productprices
		self.product_name()
					
	def product_name(self): # get all product names and save in 'productnames'
		productnames=[]
		productname = self.soup.findAll("strong")
		for pName in productname:
			#add the names of products in the product list
			productnames.append(pName.string)
		return productnames

class explorelabs:

	def initialize(self):
		page = urllib2.urlopen("http://store.explorelabs.com/index.php?main_page=products_all")
		self.soup = BeautifulSoup(page)
		self.product_names()
		
	def product_names(self):
		productName = self.soup.findAll(colspan = '2')
		productnames = []
		for pName in productName:
			productnames.append(pName.contents[1].next.next)
		return productnames
		self.product_prices()
		
	def product_prices(self):
		productPrice = self.soup.findAll(colspan = '2')		
		productprices = []
		for p in productPrice:
			productprices.append(p.contents[5])
		return productprices

class mgSuperStore: # get product names and their prices from all pages
	
	def get_data(self):
		productprices = []
		productnames = []
		
		for u in ("http://mgsuperlabs.co.in/store/index.php/cPath/1","http://mgsuperlabs.co.in/store/index.php/cPath/2","http://mgsuperlabs.co.in/store/index.php/cPath/2_7","http://mgsuperlabs.co.in/store/index.php/cPath/2_6","http://mgsuperlabs.co.in/store/index.php/cPath/2_8","http://mgsuperlabs.co.in/store/index.php/cPath/5","http://mgsuperlabs.co.in/store/index.php/cPath/9"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			productName = soup.findAll("td",align = None)
			for p in productName:
				if p.next.next.string != 'Product Name+':
					productnames.append(p.next.next.string)
						
			productPrice = soup.findAll('td',align = 'right')		
			for p in productPrice:
				try:
					productprices.append(p.contents[2].string) #product price in case of no sale
				except:
					if p.contents[0].string !='Price':
						productprices.append(p.contents[0].string) # price of product on sale
			page.close()
		
		return productnames,productprices	
		
class simplelabs:
			
	def get_data(self):
		productprices = []
		productnames = []
		
		for u in ('http://www.simplelabs.co.in/catalog/arduino-boards','http://www.simplelabs.co.in/catalog/arduino-shields','http://www.simplelabs.co.in/catalog/starter-kits','http://www.simplelabs.co.in/catalog/other-boards','http://www.simplelabs.co.in/catalog/pressure-force-flow','http://www.simplelabs.co.in/catalog/distance-measurement','http://www.simplelabs.co.in/catalog/accelerometers-gyros','http://www.simplelabs.co.in/catalog/temperature-light','http://www.simplelabs.co.in/catalog/other-sensors','http://www.simplelabs.co.in/catalog/robotics-kits','http://www.simplelabs.co.in/catalog/ics','http://www.simplelabs.co.in/catalog/motors','http://www.simplelabs.co.in/catalog/wireless','http://www.simplelabs.co.in/catalog/discrete-components','http://www.simplelabs.co.in/catalog/displays'):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			productName = soup.findAll("td", attrs = {'class'  : 'catalogueItem'})
			for p in productName:
				productnames.append(p.h2.next.next)
			productPrice = soup.findAll(attrs = 'uc-price')		
			for p in productPrice:
				productprices.append(p.contents[0])
			page.close()						
		
		return productnames,productprices
				
class rhydolabz:
			
	def get_data(self):
		productprices = []
		productnames = []
		
		for u in ("http://www.rhydolabz.com/index.php?main_page=index&cPath=152_123","http://www.rhydolabz.com/index.php?main_page=index&cPath=152_151","http://www.rhydolabz.com/index.php?main_page=index&cPath=152_169","http://www.rhydolabz.com/index.php?main_page=index&cPath=88","http://www.rhydolabz.com/index.php?main_page=index&cPath=67","http://www.rhydolabz.com/index.php?main_page=index&cPath=99","http://www.rhydolabz.com/index.php?main_page=index&cPath=155_161","http://www.rhydolabz.com/index.php?main_page=index&cPath=155_156","http://www.rhydolabz.com/index.php?main_page=index&cPath=155_157",'http://www.rhydolabz.com/index.php?main_page=index&cPath=155_160','http://www.rhydolabz.com/index.php?main_page=index&cPath=155_162',"http://www.rhydolabz.com/index.php?main_page=index&cPath=155_163","http://www.rhydolabz.com/index.php?main_page=index&cPath=155_164","http://www.rhydolabz.com/index.php?main_page=index&cPath=155_167","http://www.rhydolabz.com/index.php?main_page=index&cPath=87","http://www.rhydolabz.com/index.php?main_page=index&cPath=80","http://www.rhydolabz.com/index.php?main_page=index&cPath=130_131","http://www.rhydolabz.com/index.php?main_page=index&cPath=130_132","http://www.rhydolabz.com/index.php?main_page=index&cPath=130_133","http://www.rhydolabz.com/index.php?main_page=index&cPath=130_134","http://www.rhydolabz.com/index.php?main_page=index&cPath=130_136","http://www.rhydolabz.com/index.php?main_page=index&cPath=130_135","http://www.rhydolabz.com/index.php?main_page=index&cPath=98","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_138","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_139","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_144","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_145","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_140","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_141","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_142","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_143","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_150","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_146","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_149","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_147","http://www.rhydolabz.com/index.php?main_page=index&cPath=137_148","http://www.rhydolabz.com/index.php?main_page=index&cPath=97_111","http://www.rhydolabz.com/index.php?main_page=index&cPath=97_112","http://www.rhydolabz.com/index.php?main_page=index&cPath=72","http://www.rhydolabz.com/index.php?main_page=index&cPath=82","http://www.rhydolabz.com/index.php?main_page=index&cPath=124","http://www.rhydolabz.com/index.php?main_page=index&cPath=126","http://www.rhydolabz.com/index.php?main_page=index&cPath=166","http://www.rhydolabz.com/index.php?main_page=index&cPath=165"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			productName = soup.findAll(attrs = 'itemTitle')
			for p in productName:
				productnames.append(p.contents[0].next)
			productPrice = soup.findAll('td',attrs = {'class':"productListing-data", 'align':"right"})		
			for p in productPrice:
				try:
					productprices.append(p.find(attrs = 'productSpecialPrice').string)	# price of product on sale					
				except:
					productprices.append(p.next.next) # price of product without discount
			page.close()						
		
		return productnames,productprices


class catSystems:
	
	def get_data(self):
		productprices = []
		productnames = []
		
		for u in ("http://www.catsystems.in/products.aspx?qscatid=103","http://www.catsystems.in/products.aspx?qscatid=163","http://www.catsystems.in/products.aspx?qscatid=157","http://www.catsystems.in/products.aspx?qscatid=82","http://www.catsystems.in/products.aspx?qscatid=102","http://www.catsystems.in/products.aspx?qscatid=139","http://www.catsystems.in/products.aspx?qscatid=143","http://www.catsystems.in/products.aspx?qscatid=146","http://www.catsystems.in/products.aspx?qscatid=152","http://www.catsystems.in/products.aspx?qscatid=160","http://www.catsystems.in/products.aspx?qscatid=186","http://www.catsystems.in/products.aspx?qscatid=202","http://www.catsystems.in/products.aspx?qscatid=28","http://www.catsystems.in/products.aspx?qscatid=71","http://www.catsystems.in/products.aspx?qscatid=140","http://www.catsystems.in/products.aspx?qscatid=147","http://www.catsystems.in/products.aspx?qscatid=148","http://www.catsystems.in/products.aspx?qscatid=159"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			productName = soup.findAll(attrs = {"style":"margin-bottom:5px"})
			pr = iter(productName)
			for p in pr:
				if p.contents[1].string != None:
					productnames.append(p.contents[1].string)
					pr.next() # skip product id
			
			productPrice = soup.findAll(attrs = {'alt':'Rs.'})		
			for p in productPrice:
				productprices.append(p.next.next.string)						

					
		page.close()
		
		return productnames,productprices	

class tenet:
	
	def get_data(self):
		productprices = []
		productnames = []
		
		for u in ("http://tenettech.com/category.php?n=50&id_category=28","http://tenettech.com/category.php?id_category=68","http://tenettech.com/category.php?id_category=87","http://tenettech.com/category.php?id_category=75","http://tenettech.com/category.php?id_category=78","http://tenettech.com/category.php?id_category=72","http://tenettech.com/category.php?id_category=82","http://tenettech.com/category.php?id_category=83","http://tenettech.com/category.php?id_category=85","http://tenettech.com/category.php?id_category=88","http://tenettech.com/category.php?id_category=91"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			productName = soup.findAll('h3')
			for p in productName:
				if p.next.next!='New' and p.next!= 'Subcategories':
					productnames.append(p.next.next)
			productPrice = soup.findAll(attrs = {'class':'price'})		
			for p in productPrice:
				productprices.append(p.next)						
		page.close()
		
		return productnames,productprices	


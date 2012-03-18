#! /usr/bin/env 2.7

#import all classes from ninecircuits
from nineCircuits import ninecircuits, explorelabs,mgSuperStore,simplelabs,rhydolabz,catSystems,tenet
import HTML
import re

class table():

	def ninecircuits(self): #list of all 9circuits products and their prices
		nine = ninecircuits()
		run = nine.initialize()
		self.productlist = nine.product_name()
		self.pricelist = nine.product_price()
		self.explorelabs()
		
	def explorelabs(self): # search for common products in explorelabs and get their prices
		explore = explorelabs()
		run = explore.initialize()
		explorenames = explore.product_names()
		exploreprices = explore.product_prices()
		
		self.elmatch = []
		for product in self.productlist:
			self.pLower = []
			for p in str(product).split(): #split the product name and convert to lowercase
				self.pLower.append(p.lower()) 	
			for i in explorenames:
				elSplit = re.split('\W',i)
				elLower = []
				for j in elSplit:
					elLower.append(j.lower())
				if set(self.pLower).issubset(set(elLower)): # check for any match in product names
					m = explorenames.index(i) # get index of the matched product 
					# using index number of matched product get its price
					self.elmatch.insert(self.productlist.index(product),exploreprices[m]) 
				else:
					# incase of no match add 'N/A'
					self.elmatch.append('N/A')
		self.mgSuperStore()
	
	def mgSuperStore(self):
		mg = mgSuperStore()
		mgproducts,mgprices = mg.get_data()
	
		self.mgmatch = []
		for product in self.productlist:
			pLower = []
			for p in str(product).split():
				pLower.append(p.lower()) 	
			for i in mgproducts:
				mgSplit = re.split('\W',i)
				mgLower = []
				for j in mgSplit:
					mgLower.append(j.lower())
				if set(pLower).issubset(set(mgLower)):
					m = mgproducts.index(i)
					self.mgmatch.insert(self.productlist.index(product),mgprices[m])
				else:
					self.mgmatch.append('N/A')
		self.simplelabs()

	def simplelabs(self):
		sl = simplelabs()
		slproducts,slprices = sl.get_data()
	
		self.slmatch = []
		for product in self.productlist:
			pLower = []
			for p in str(product).split():
				pLower.append(p.lower()) 	
			for i in slproducts:
				slSplit = re.split('\W',i)
				slLower = []
				for j in slSplit:
					slLower.append(j.lower())
				if set(pLower).issubset(set(slLower)):
					m = slproducts.index(i)
					self.slmatch.insert(self.productlist.index(product),slprices[m])
				else:
					self.slmatch.append('N/A')
		self.rhydolabz()
	
	def rhydolabz(self):
		rl = rhydolabz()
		rlproducts,rlprices = rl.get_data()
	
		self.rlmatch = []
		for product in self.productlist:
			pLower = []
			for p in str(product).split():
				pLower.append(p.lower()) 	
			for i in rlproducts:
				rlSplit = re.split('\W',i)
				rlLower = []
				for j in rlSplit:
					rlLower.append(j.lower())
				if set(pLower).issubset(set(rlLower)):
					m = rlproducts.index(i)
					self.rlmatch.insert(self.productlist.index(product),rlprices[m])
				else:
					self.rlmatch.append('N/A')
		self.catSystems()

	def catSystems(self):
		cs = catSystems()
		csproducts,csprices = cs.get_data()
	
		self.csmatch = []
		for product in self.productlist:
			pLower = []
			for p in str(product).split():
				pLower.append(p.lower()) 	
			for i in csproducts:
				csSplit = re.split('\W',i)
				csLower = []
				for j in csSplit:
					csLower.append(j.lower())
				if set(pLower).issubset(set(csLower)):
					m = csproducts.index(i)
					self.csmatch.insert(self.productlist.index(product),csprices[m])
				else:
					self.csmatch.append('N/A')
		self.tenet()

	def tenet(self):
		tt = tenet()
		ttproducts,ttprices = tt.get_data()
	
		self.ttmatch = []
		for product in self.productlist:
			pLower = []
			for p in str(product).split():
				pLower.append(p.lower()) 	
			for i in ttproducts:
				ttSplit = re.split('\W',i)
				ttLower = []
				for j in ttSplit:
					ttLower.append(j.lower())
				if set(pLower).issubset(set(ttLower)):
					m = ttproducts.index(i)
					self.ttmatch.insert(self.productlist.index(product),ttprices[m])
				else:
					self.ttmatch.append('N/A')
		self.get_code()

		
	def code(self): # get table contents
		for x in range(len(self.pricelist)):
			yield[self.productlist[x],self.pricelist[x],self.elmatch[x],self.mgmatch[x],self.slmatch[x],self.rlmatch[x],self.csmatch[x],self.ttmatch[x]]
	
	def get_code(self): # write table headers in a file
		html =  HTML.table(self.code(),header_row = ['Products','9circuits','Explore Labs','MG super Labs','Simple Labs','Rhydo Labz','CAT Systems','Tenet Technotronics'])
		file1 = open('sourcecode.html','w')
		file1.write(html)
		file1.close()
		

s = table()
start = s.ninecircuits()

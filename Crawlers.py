#! /usr/bin/env 2.7

import urllib2
import re
from BeautifulSoup import BeautifulSoup


class site1:
	
	def initialize(self):
		# access the required page
		page = urllib2.urlopen("site url")
		self.soup = BeautifulSoup(page)
		self.info1()
		
	def info1(self): # get all relevant and save in a list
		infoList1=[]
		# search for all occurrences of 'required data' in the html tags
		info1 = self.soup.findAll(attrs="attribute")
		for p in info1:
			# add the data in the list
			infoList1.append(p.string)
		return infoList1
		self.info2()
					
	def info2(self): # get all required info and save in second  list
		infoList2=[]
		productname = self.soup.findAll("strong")
		for pName in productname:
			#add the 'relevant data' list
			infoList2.append(pName.string)
		return infoList2

class site2:

	def initialize(self):
		page = urllib2.urlopen("site url")
		self.soup = BeautifulSoup(page)
		self.info2()
		
	def info2s(self):
		getInfo = self.soup.findAll(colspan = '2')
		infoList2 = []
		for pName in getInfo:
			infoList2.append(pName.contents[1].next.next)
		return infoList2
		self.info1s()
		
	def info1(self):
		getInfo1 = self.soup.findAll(colspan = '2')		
		infoList1 = []
		for p in getInfo1:
			infoList1.append(p.contents[5])
		return infoList1

class site3: # get relevant information
	
	def get_data(self):
		infoList1 = []
		infoList2 = []
		
		for u in ("web page"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			getInfo = soup.findAll("td",align = None)
			for p in getInfo:
				if p.next.next.string != 'info to be skipped':
					infoList2.append(p.next.next.string)
						
			getInfo1 = soup.findAll('td',align = 'right')		
			for p in getInfo1: #taking care of exceptions in tags
				try:
					infoList1.append(p.contents[2].string) 
				except:
					if p.contents[0].string !='the data to be skipped':
						infoList1.append(p.contents[0].string) 
			page.close()
		
		return infoList2,infoList1	
		
class site4:
			
	def get_data(self):
		infoList1 = []
		infoList2 = []
		
		for u in ('relevant web pages'):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			getInfo = soup.findAll("td", attrs = {'class'  : 'class'})
			for p in getInfo:
				infoList2.append(p.h2.next.next)
			getInfo1 = soup.findAll(attrs = 'attribute')		
			for p in getInfo1:
				infoList1.append(p.contents[0])
			page.close()						
		
		return infoList2,infoList1
				
class site5:
			
	def get_data(self):
		infoList1 = []
		infoList2 = []
		
		for u in ("all pages to be crawled"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			getInfo = soup.findAll(attrs = 'itemTitle')
			for p in getInfo:
				infoList2.append(p.contents[0].next)
			getInfo1 = soup.findAll('td',attrs = {'class':"class", 'align':"allignment"})		
			for p in getInfo1:
				try:
					infoList1.append(p.find(attrs = 'attribute').string)						
				except:
					infoList1.append(p.next.next) 
			page.close()						
		
		return infoList2,infoList1


class site6:
	
	def get_data(self):
		infoList1 = []
		infoList2 = []
		
		for u in ("relelvant pages"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			getInfo = soup.findAll(attrs = {"style":"margin-bottom:5px"})
			pr = iter(getInfo)
			for p in pr:
				if p.contents[1].string != None:
					infoList2.append(p.contents[1].string)
					pr.next() # skip product id
			
			getInfo1 = soup.findAll(attrs = {'alt':'Rs.'})		
			for p in getInfo1:
				infoList1.append(p.next.next.string)						

					
		page.close()
		
		return infoList2,infoList1	

class site7:
	
	def get_data(self):
		infoList1 = []
		infoList2 = []
		
		for u in ("pages to be crawled"):
			page=urllib2.urlopen(u)
			soup = BeautifulSoup(page)
					
			getInfo = soup.findAll('h3')
			for p in getInfo:
				if p.next.next!='New' and p.next!= 'Subcategories':
					infoList2.append(p.next.next)
			getInfo1 = soup.findAll(attrs = {'class':'the class needed'})		
			for p in getInfo1:
				infoList1.append(p.next)						
		page.close()
		
		return infoList2,infoList1	


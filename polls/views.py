from django.shortcuts import render
from django.http import HttpResponse
import selenium
import time
from selenium import webdriver
from time import sleep
import sqlite3
import sys
import MySQLdb
import _mysql
import bs4
from bs4 import BeautifulSoup
import io

# Create your views here.
def hom(request):
	i=0
	return render(request, "polls/home.html",{"i":i})
def search(request,name):
	"""
	query=str(name)
	url="http://www.amazon.in"
	print(str(sys.argv[1]))
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.get(url)
	print("\nOpening Amazon....")
	time.sleep(1)
	sbox=driver.find_element_by_id('twotabsearchtextbox')
	sbox.send_keys(query)
	print("\nEntering Queries....")
	go=driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
	time.sleep(2)
	image=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[2]/div[1]/div[1]/a[1]/img')
	tex=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[3]/div[1]/a[1]/h2')
	link=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[3]/div[1]/a')
		
	ai=0
	a=["","","","",""];
	b=["","","","",""];
	c=["","","","",""];
		
	for lin in link:
		a[ai]=str(lin.get_attribute('href'))
		b[ai]=str(image[ai].get_attribute('src'))
		c[ai]=str(tex[ai].text)	
		ai=ai+1
		if ai==4:
			break
	"""
	print("\nOpening WebDriver....")
	#print(str(sys.argv[1]))
	url="http://www.google.com"
	query=str(name)
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	print("\nOpening search engines....")
	driver.set_window_size(1024, 600)
	driver.set_window_position(-10000,0)
	
	driver.get(url)
	print("\nSearching web for "+query)
	time.sleep(1)
	gs=driver.find_element_by_xpath('//*[@id="lst-ib"]')
	gs.clear()
	gs.click()
	gs.send_keys(query+" site://mysmartprice.com")
	time.sleep(1)
	gb=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
	time.sleep(2)
	gr=driver.find_element_by_xpath('//*[@class="r"]/a').click()
	time.sleep(3)#more time for the images on the page to load
	#Code for mysmartprice landing page
	driver.execute_script("window.scrollTo(0, 200)")
	mspimg=driver.find_element_by_xpath('//*[@class="prdct-dtl__img"]')
	src=mspimg.get_attribute('src')
	mspsites=driver.find_elements_by_xpath('//*[@class="prc-tbl__row-wrpr"]/div/div/img')
	mspprice=driver.find_elements_by_xpath('//*[@class="prc-tbl__prc"]')
	count=0
	bestb=mspsites[0].get_attribute('src')
	besta=""
	if bestb=="https://assets.mspcdn.net/q_auto/logos/partners/flipkart_store.png":
		besta="site://www.flipkart.com"
	elif bestb=="https://assets.mspcdn.net/q_auto/logos/partners/tatacliq_store.png":
		besta="site://www.tatacliq.com"
	elif bestb=="https://assets.mspcdn.net/q_auto/logos/partners/amazon_store.png":
		besta="site://amazon.in"
	elif bestb=="https://assets.mspcdn.net/q_auto/logos/partners/mi_store.png":
		besta="site://mi.com"		
	for site in mspsites:
		count=count+1	
	s_site=[]
	s_price=[]	
	for i in range(0,count):
		s_sit=mspsites[i].get_attribute('src')
		s_pric=mspprice[i].text
		s_site.append(s_sit)
		s_price.append(s_pric)
		print(str(s_site[i])+":"+str(s_price[i])+"\n")
	#Specs retriever
	specboo=0
	try:
		mspgd=driver.find_elements_by_xpath('//*[@class="exprt-rvw__col"][1]/li[@class="exprt-rvw__item"]')
		mspbd=driver.find_elements_by_xpath('//*[@class="exprt-rvw__col"][2]/li[@class="exprt-rvw__item"]')
		gd=[]
		bd=[]
		for i1 in mspgd:
			gd.append(i1.text)
		for i2 in mspbd:
			bd.append(i2.text)
		print(gd)
		print("\n")
		print(bd)
		if len(gd)==0:
			specboo=0
		else:
			specboo=1
	except:
			specboo=0
			print("Cannot find pros and cons")	

	descboo=0
	try:
		desc=driver.find_element_by_xpath('//*[@class="prdct-dtl__spfctn-wrpr"]').text
		descboo=1
	except:
		descboo=0
		print("Cannot find DESCRIPTION")
	time.sleep(2)
	driver.quit()

	#for best buy links
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.set_window_size(1024, 600)
	driver.set_window_position(-10000,0)
	url="http://www.google.com"
	driver.get(url)
	print("\nfinding best price for "+query)
	time.sleep(2)
	gs=driver.find_element_by_xpath('//*[@id="lst-ib"]')
	gs.clear()
	gs.click()
	gs.send_keys(query+" "+besta)
	time.sleep(2)
	#gb=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
	#driver.find_element_by_xpath('//*[@name="btnK"]')
	driver.find_element_by_xpath('//*[@id="gbwa"]/div[1]/a').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@name="btnK"]').click()
	driver.execute_script("window.scrollTo(0, 200)")
	time.sleep(2)
	bestlink=driver.find_element_by_xpath('//*[@class="r"]/a').get_attribute('href')
	time.sleep(1)
	driver.quit()

	url="http://www.amazon.in"
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.set_window_size(1024, 600)
	driver.set_window_position(-10000,0)
	driver.get(url)
	print("\nOpening AMAZON....")
	time.sleep(1)
	sbox=driver.find_element_by_id('twotabsearchtextbox')
	sbox.send_keys(query)
	print("\nEntering Queries....")
	go=driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
	time.sleep(2)
	#link=driver.find_elements_by_xpath('//*[@id="result_0"]/div[1]/div[3]/div[1]/a')
	try:
		link=driver.find_element_by_xpath('//*[@class="s-result-list s-col-3 s-result-list-hgrid s-height-equalized s-grid-view s-text-condensed"]/li[1]/div/div[3]/div/a')
		print('First link is selected')
	except:
		try:
			link=driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a')
			print('Second link is selected')
		except:
			try:
				link=driver.find_element_by_xpath('//*[@id="result_1"]/div/div/div/div[2]/div[1]/div[1]/a')
				print('third link is selected')
			except:
				try:
					link=driver.find_element_by_xpath('//*[@id="result_2"]/div/div/div/div[2]/div[1]/div[1]/a')
					print('third link is selected')
				except:
					link=driver.find_element_by_xpath('//*[@id="result_3"]/div/div/div/div[2]/div[1]/div[1]/a')
					print('E:404')
	url1=link.get_attribute('href')
	driver.quit()

	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.set_window_size(1024, 600)
	driver.set_window_position(-10000,0)
	driver.get(url1)
	time.sleep(2)
	url2=driver.find_element_by_xpath('//*[@id="acrCustomerReviewLink"]').get_attribute('href')
	driver.quit()
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.set_window_size(1024, 600)
	driver.set_window_position(-10000,0)
	driver.get(url2)
	nodes=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/span[contains(@class,'a-size-base review-text')]")
	#div[contains(@class,'row')]
	star=driver.find_elements_by_xpath('//*[@id="cm_cr-review_list"]/div/div[@class="a-section celwidget"]/div[1]/a[1]')
	title=driver.find_elements_by_xpath('//*[@id="cm_cr-review_list"]/div/div[@class="a-section celwidget"]/div[1]/a[2]')
	time.sleep(2)
	print(str(len(nodes)))
	i=0
	c="a"
	aas="a"
	cas="c"
	rev=[]
	str1=[]
	tit=[]
	bas="b"
	for head in nodes:
		aas=head.text
		bas=title[i].text
		cas=star[i].get_attribute("title")
		rev.append(aas)
		tit.append(bas)
		str1.append(cas)
		i=i+1
	driver.quit()	
	#url1 not needed anymore
	#return render(request, "polls/spec.html", {"src1" : b[0],"src2" : b[1],"src3" : b[2],"src4" : b[3],"src5" : b[4],"hh1" : c[0],"hh2" : c[1],"hh3" : c[2],"hh4" : c[3],"hh5" : c[4],"a1" : a[0],"a2" : a[1],"a3" : a[2],"a4" : a[3],"a5" : a[4]})
	return render(request, "polls/spec.html", {"bestbuy":bestlink,"rev":zip(str1,tit,rev),"url1":url1,"desc":desc,"gd":gd,"bd":bd,"q1":query,"plist":s_price,"slist":s_site,"imgsrc":src,"specboo":specboo,"descboo":descboo})

def search1(request,name):
	print("\nOpening WebDriver....")
	#print(str(sys.argv[1]))
	url="http://www.flipkart.com"
	query=str(name)
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.set_window_size(1024, 600)
	#driver.maximize_window()
	
	driver.set_window_position(-10000,0)
	driver.get(url)

	"""
	print("\nOpening Amazon....")
	time.sleep(1)
	sbox=driver.find_element_by_id('twotabsearchtextbox')
	sbox.send_keys(query)
	print("\nEntering Queries....")
	go=driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
	time.sleep(2)
	image=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[2]/div[1]/div[1]/a[1]/img')
	tex=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[3]/div[1]/a[1]/h2')
	link=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[3]/div[1]/a')
	price=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[5]/div[1]/a/span[1]')
	ai=0
	a=["","","","","","","",""];
	b=["","","","","","","",""];
	c=["","","","","","","",""];
	d=["","","","","","","",""];
		
	for lin in link:
		a[ai]="http://127.0.0.1:8000/search2/"+str(tex[ai].text)
		b[ai]=str(image[ai].get_attribute('src'))
		c[ai]=str(tex[ai].text)	
		d[ai]=str(price[ai].text)
		ai=ai+1
		if ai==7:
			break
	"""
	print("\nOpening E-commerce websites....")
	time.sleep(1)
	try:
		driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
		print("login cancelled")
	except:
		print("No login found!")
	sbox=driver.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input')
	sbox.send_keys(query)
	print("\nEntering Queries....")
	go=driver.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div/div/div/div[1]/form/div/div[2]/button').click()
	time.sleep(4)
	driver.execute_script("window.scrollTo(0, 200)")
	driver.execute_script("window.scrollTo(200, 400)")	
	driver.execute_script("window.scrollTo(400, 600)")

	driver.execute_script("window.scrollTo(600, 800)")

	driver.execute_script("window.scrollTo(800, 1000)")
	driver.execute_script("window.scrollTo(1000, 1200)")
	driver.execute_script("window.scrollTo(1200, 1400)")
	driver.execute_script("window.scrollTo(1400, 1600)")
	
	time.sleep(2)
	image=driver.find_elements_by_xpath('//div[contains(@class,"col _2-gKeQ")]/div[1]/a[1]/div[contains(@class,"_3SQWE6")]/div[1]/div[1]/div[1]/img[1]')
	tex=driver.find_elements_by_xpath('//div[contains(@class,"col _2-gKeQ")]/div[1]/a[1]/div[contains(@class,"_1-2Iqu row")]/div[1]/div[1]')
	link=driver.find_elements_by_xpath('//div[contains(@class,"col _2-gKeQ")]/div[1]/a[1]')
	price=driver.find_elements_by_xpath('//div[contains(@class,"col _2-gKeQ")]/div[1]/a[1]/div[contains(@class,"_1-2Iqu row")]/div[2]/div[1]/div[1]/div[1]')
	chec=0
	if len(image)==0:
		image=driver.find_elements_by_xpath('//*[@class="_3liAhj"]/a[1]/div/div[1]/div[1]/img')
		tex=driver.find_elements_by_xpath('//*[@class="_3liAhj"]/a[2]')
		link=driver.find_elements_by_xpath('//*[@class="_3liAhj"]/a[2]')
		price=driver.find_elements_by_xpath('//*[@class="_3liAhj"]/a[3]/div[@class="_1uv9Cb"]/div[1]')
	ai=0
	a=["","","","","","","",""];
	b=["","","","","","","",""];
	c=["","","","","","","",""];
	d=["","","","","","","",""];
		
	for lin in link:
		a[ai]="http://127.0.0.1:8000/search2/"+str(tex[ai].text)
		b[ai]=str(image[ai].get_attribute('src'))
		c[ai]=str(tex[ai].text)	
		d[ai]=str(price[ai].text)
		ai=ai+1
		print(ai)
		if ai==8:
			break
	
			
	
	driver.quit()	
	#return render(request, "polls/spec.html", {"src1" : b[0],"src2" : b[1],"src3" : b[2],"src4" : b[3],"src5" : b[4],"hh1" : c[0],"hh2" : c[1],"hh3" : c[2],"hh4" : c[3],"hh5" : c[4],"a1" : a[0],"a2" : a[1],"a3" : a[2],"a4" : a[3],"a5" : a[4]})
	return render(request, "polls/res.html", {"tilte":query,"prod":zip(c,b,d,a)})

def search2(request,name):
	print("\nOpening WebDriver....")
	#print(str(sys.argv[1]))
	url="http://www.google.com"
	query=str(name)

	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.set_window_size(1024, 600)
	driver.set_window_position(-10000,0)
	driver.get(url)
	print("\nSearching web for "+query)
	time.sleep(1)
	gs=driver.find_element_by_xpath('//*[@id="lst-ib"]')
	gs.clear()
	gs.click()
	gs.send_keys(query+" site://flipkart.com")
	time.sleep(1)
	gb=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
	time.sleep(2)
	gr=driver.find_element_by_xpath('//*[@class="r"]/a')
	furl=gr.get_attribute("href")
	gr.click()
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, 200)")
	driver.execute_script("window.scrollTo(200, 400)")	
	driver.execute_script("window.scrollTo(400, 600)")

	driver.execute_script("window.scrollTo(600, 800)")

	driver.execute_script("window.scrollTo(800, 1000)")
	driver.execute_script("window.scrollTo(1000, 1200)")
	driver.execute_script("window.scrollTo(1200, 1400)")
	driver.execute_script("window.scrollTo(1400, 1600)")

	time.sleep(2)
	#waiting for image to load
	image=driver.find_element_by_xpath('//*[@class="sfescn"]')
	ima=image.get_attribute('src')
	print(ima)
	price=driver.find_element_by_xpath('//*[@class="_1vC4OE _37U4_g"]')
	name=driver.find_element_by_xpath('//*[@class="_3eAQiD"]')
	try:
		driver.find_element_by_xpath('//*[@class="_2AkmmA _2V7q8b"]').click()
		print('details opened')
	except:
		print('details not found')
	driver.execute_script("window.scrollTo(1600, 2000)")
	driver.execute_script("window.scrollTo(2000, 2500)")

	driver.execute_script("window.scrollTo(2500, 3000)")

	time.sleep(2)
	spech=driver.find_elements_by_xpath('//*[@class="_2ixwsm"]/div[2]/div[1]/div[1]/div[@class="_2Kp3n6"]/div[1]')
	#specs=driver.find_elements_by_xpath('//*[@class="_2ixwsm"]/div[2]/div[1]/div[1]/div[@class="_2Kp3n6"]/ul[1]')
	cspec=0
	c1=0
	print("Product Name: ")
	print(name.text)
	na=name.text
	print("\n")
	print("Product Price: ")
	print(price.text)
	pa=price.text
	print("\n")
	print("Product Specification:- ")
	sh1=[]
	ca=[]
	for sp in spech:
		sh1.append(sp.text)
		ca.append("x")
		#print(sp.text)
		cspec=cspec+1;
	print("\n\n\n")
	d=[]
	for c in range(1,cspec):
		c1=0
		specs1=driver.find_elements_by_xpath('//*[@class="_2ixwsm"]/div[2]/div[1]/div[1]/div[@class="_2Kp3n6"]['+str(c)+']/ul[1]/li/div')
		specs2=driver.find_elements_by_xpath('//*[@class="_2ixwsm"]/div[2]/div[1]/div[1]/div[@class="_2Kp3n6"]['+str(c)+']/ul[1]/li/ul')
		#print(str(len(specs1))+" :  "+str(len(specs2)))
		d2=[]
		d3=[]
		for s1 in specs1:
			d2.append(s1.text)
			#print(s1.text)
			#print(" : ")
			d3.append(specs2[c1].text)
			#print(specs2[c1].text)
			c1=c1+1
		d.append(zip(d2,d3))
	print(d)		
	driver.quit()	
	return render(request, "polls/spec1.html", {"name":na,"price":pa,"imgsrc":ima,"c":cspec,"sh":sh1,"spec":d,"ur":furl,"c1":ca})
	
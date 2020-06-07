import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

def url():
	urls = 'http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=39436183727126211'
	url1 = 'http://www.tsetmc.com/Loader.aspx?ParTree=15131F'
	return url1


def process_driver(url):
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(options=options)
	driver.implicitly_wait(10)
	driver.get(url)
	return driver

def sec_process(driver):
	#Getting first selector
	s_1 = '#id1'
	s_1_prime = '#InsMenu'
	element = driver.find_elements_by_css_selector(s_1)
	element[0].click()
	driver.switch_to.window(driver.window_handles[0])


	#After selecting Faraboors and Bazarpaie!
	s_2 = '#ModalWindowInner1 > div.box3 > div:nth-child(33)'
	element = driver.find_elements_by_css_selector('#ModalWindowInner1 > div.box3 > div:nth-child(33)')
	element[0].click()
	driver.refresh()

	list_of_selectors = []
	for i in range(34,41):
		css_selector_link = '#ModalWindowInner1 > div.box3 > div:nth-child({})'.format(i)
		list_of_selectors.append(css_selector_link)
	s_1 = '#id1'
	for i in range(len(list_of_selectors)):
		element = driver.find_elements_by_css_selector(s_1)
		element[0].click()
		driver.switch_to.window(driver.window_handles[0])
		print(i)
		driver.implicitly_wait(5)
		element = driver.find_elements_by_css_selector(list_of_selectors[i])
		print(len(element))
		element[0].click()
		driver.refresh()
	time.sleep(3)
	page = driver.page_source
	driver.quit()
	soup = BeautifulSoup(page, 'html.parser')
	container_list = []
	for container in soup.find_all('a', attrs={'class': 'inst'}):
		container_list.append(container)
	print(container_list[0])
	return container_list
	# return driver

import re
def Code_getter(code_list):
	names, id = [], []
	i = 0
	for m in code_list:
		if i % 2 == 0:
			y = re.findall(r'i=([0-9]*)', str(m))
			x = re.findall(r'>(.*)</a>', str(m))
			names.append(x[0])
			id.append(y[0])
		i += 1
	return names,id

import csv
def import_to_csv(names,ids):
	with open('tsestocknames.csv', 'w', encoding="utf-8", newline='') as f:
		writer = csv.writer(f)
		writer.writerows(zip(names, ids))

url = url()
g_driver = process_driver(url)
g2_driver = sec_process(g_driver)
stock_names , ids = Code_getter(g2_driver)
import_to_csv(stock_names,ids)
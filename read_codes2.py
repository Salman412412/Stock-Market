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
	driver = webdriver.Chrome()
	driver.implicitly_wait(100)
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


	# print(s_3)
	# elem = driver.find_elements_by_css_selector(s_3)
	# print(elem)
	# if elem:
	# 	elem[0].click()
	# 	driver.switch_to.window(driver.window_handles[0])
	# else:
	# 	print('hi')



	# def find(driver):
	# 	e = driver.find_element_by_id('#ModalWindowInner1 > div.box3 > div:nth-child(11)')
	# 	return e
	#
	# elem = WebDriverWait(driver, 10).until(find)
	# elem[0].click()



	# mamad = driver.page_source
	# print(driver)
	#
	#
	#
	# elem = driver.find_elements_by_css_selector('#ModalWindowInner1 > div > div.content > div > ul > li:nth-child(1) > a')
	# if elem:
	# 	for el in elem:
	# 		print(el.text)
	# else:
	# 	print('hi')
	# close_click = driver.find_elements_by_css_selector('#ModalWindowOuter1 > div.popup_close')[0].click()



	list_of_selectors = ['#ModalWindowInner1 > div.box3 > div:nth-child(34)',
	                     '#ModalWindowInner1 > div.box3 > div:nth-child(35)',
	                     '#ModalWindowInner1 > div.box3 > div:nth-child(36)',
	                     '#ModalWindowInner1 > div.box3 > div:nth-child(37)',
	                     '#ModalWindowInner1 > div.box3 > div:nth-child(38)',
	                     '#ModalWindowInner1 > div.box3 > div:nth-child(39)',
	                     '#ModalWindowInner1 > div.box3 > div:nth-child(40)']
	s_1 = '#id1'
	for i in range(len(list_of_selectors)-4):
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
	print(page)
	input('Hey you ! Fuck you ...')
	driver.quit()
	soup = BeautifulSoup(page, 'html.parser')
	for container in soup.find_all('a', attrs={'class': 'inst'}):
		print(container)
	#
	return 1
	# return driver

def last_process(driver):
	page = driver.page_source
	print(page)
	driver.quit()
	soup = BeautifulSoup(page, 'html.parser')
	for container in soup.find_all('a', attrs={'class': 'inst'}):
		print(container)



url = url()
g_driver = process_driver(url)
g2_driver = sec_process(g_driver)
#last_process(g2_driver)
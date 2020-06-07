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

	# list_of_selectors = ['#ModalWindowInner1 > div.box3 > div:nth-child(34)',
	#                      '#ModalWindowInner1 > div.box3 > div:nth-child(35)',
	#                      '#ModalWindowInner1 > div.box3 > div:nth-child(36)',
	#                      '#ModalWindowInner1 > div.box3 > div:nth-child(37)',
	#                      '#ModalWindowInner1 > div.box3 > div:nth-child(38)',
	#                      '#ModalWindowInner1 > div.box3 > div:nth-child(39)',
	#                      '#ModalWindowInner1 > div.box3 > div:nth-child(40)']
	list_of_selectors = []
	for i in range(34,41):
		css_selector_link = '#ModalWindowInner1 > div.box3 > div:nth-child({})'.format(i)
        list_of_selectors.append(css_selector_link)

	s_1 = '#id1'
	for i in range(len(list_of_selectors)-2):
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
	#
	return container_list
	# return driver

def Code_getter(code_list):
	pass



url = url()
g_driver = process_driver(url)
g2_driver = sec_process(g_driver)
#last_process(g2_driver)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException    

import time
import csv

def check_exists_by_class_name(browser, class_name):
	try:
		browser.find_element_by_class_name(class_name)
	except NoSuchElementException:
		return False
	return True

def check_exists_by_id(browser, id_param):
	try:
		browser.find_element_by_id(id_param)
	except NoSuchElementException:
		return False
	return True

school = 'Emory'
year = '2016'
term = 'Fall'

l_urls = []
filename = school + '_' + term + '_' + year + '_' + 'courselinks.csv' 
with open(filename, 'r') as myfile:
    read = csv.reader(myfile)
    for row in read:
    	l_urls.append(row[0]) #every row is a list

#for testing data
test_urls = l_urls[:2]

browser = webdriver.Firefox()
for url in l_urls:
	section = {}
	#section['url'] = url

	#Class title 
	browser.get(url)
	#time.sleep(1)
	selection = browser.find_element_by_id('class-section')
	name = selection.text.split('\n', 1)[0]
	#print(name)
	section['name'] = name

	#Class topic
	if check_exists_by_class_name(browser, 'topic'):
		topic = browser.find_element_by_class_name('topic')
		course_topic = topic.text
	else:
		course_topic = 'No Topic'
	#print(course_topic)
	section['topic'] = course_topic.replace('Topic: ', '')

	#find tabs
	#tabs are 1-5 eg tabs-2
	#	1 - Schedule
	#	2 - Descriptions
	#	3 - Textbooks, Articles, and Resources
	#	4 - Grading
	#	5 - Related Courses 
	tabnames = []
	tabs_name = selection.find_elements_by_class_name('ui-tabs-anchor')
	for tab_name in tabs_name:
		tabnames.append(tab_name.text)
	#print(tabnames)
	section['tabnames'] = tabnames
	number_of_tabs = len(tabnames)
	#print(number_of_tabs)

	tabs = selection.find_elements_by_class_name('ui-tabs-panel')
	if check_exists_by_id(browser, 'tabs-1'):
		tab1 = selection.find_element_by_id('tabs-1')
		tab1_body = tab1.find_element_by_tag_name('tbody')

		ger = tab1_body.find_element_by_class_name('ger')
		credit = tab1_body.find_element_by_class_name('credit')
		opus_number = tab1_body.find_element_by_class_name('opus-number')
		
		#print(ger.text)
		#print(credit.text)
		#print(opus_number.text)
		section['ger'] = ger.text
		section['credit'] = credit.text
		section['opus_number'] = opus_number.text


		schedules = tab1_body.find_element_by_class_name('schedule')
		#There are identical schedule elements, this is the child
		schedules2 = schedules.find_elements_by_class_name('schedule')
		schlist = []
		count_sch = 0
		for schedule in schedules2:
			slot = {}
			days = schedule.find_element_by_class_name('days')
			time_schedule = schedule.find_element_by_class_name('time')
			instructor = schedule.find_element_by_class_name('instructor')
			
			slot['days'] = days.text
			slot['time'] = time_schedule.text 
			slot['instructor'] = instructor.text
			schlist.append(slot)

			#count_sch = count_sch + 1

		#print(schlist)
		section['schedule'] = schlist

		notes = tab1.find_element_by_class_name('notes')
		section['notes'] = notes.text

	#need to iterate over each tab, xpath seems like the move
	#start with two because the first one is already there by default
	for i in range(2, number_of_tabs + 1):
		tab_num = selection.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/ul/li[' + str(i) + ']')
		tab_num.click()
		#print(tabnames[i-1])
		tab = selection.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/div[' + str(i) + ']')
		#print(tab.text)
		section[str(tabnames[i-1])] = tab.text

	print(section)
	

	
	

browser.quit()
print('done')
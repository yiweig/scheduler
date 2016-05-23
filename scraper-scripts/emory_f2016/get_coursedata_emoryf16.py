from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException    

import time
import csv
import json

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
#test_urls = l_urls[:2]
end = []
browser = webdriver.Firefox()
for url in l_urls:
	section = {}

	#Class title 
	browser.get(url)
	selection = browser.find_element_by_id('class-section')
	#this grabs all the text and just takes the first line, easiest
	name = selection.text.split('\n', 1)[0]
	section['name'] = name


	#Class topic
	if check_exists_by_class_name(browser, 'topic'):
		topic = browser.find_element_by_class_name('topic')
		course_topic = topic.text
	else:
		course_topic = 'none'
	section['topic'] = course_topic.replace('Topic: ', '')


	#find tabs
	#tabs are 1-5 eg tabs-2
	#	1 - Schedule
	#	2 - Descriptions
	#	3 - Textbooks, Articles, and Resources
	#	4 - Grading
	#	5 - Related Courses 
	ref_tabnames = ['Schedule','Descriptions' ,'Textbooks, Articles, and Resources' ,'Grading' ,'Related Courses']
	tabnames = []
	tabs_name = selection.find_elements_by_class_name('ui-tabs-anchor')
	for tab_name in tabs_name:
		tabnames.append(tab_name.text)
	#section['tabnames'] = tabnames
	number_of_tabs = len(tabnames)
	for item in ref_tabnames:
		if item not in tabnames:
			section[str(item)] = 'none'


	#Tab 1, has the schedule and most of the important stuff
	tabs = selection.find_elements_by_class_name('ui-tabs-panel')
	if check_exists_by_id(browser, 'tabs-1'):
		tab1 = selection.find_element_by_id('tabs-1')
		tab1_body = tab1.find_element_by_tag_name('tbody')

		ger = tab1_body.find_element_by_class_name('ger')
		credit = tab1_body.find_element_by_class_name('credit')
		opus_number = tab1_body.find_element_by_class_name('opus-number')
		
		section['ger'] = ger.text
		section['credit'] = credit.text
		section['opus_number'] = opus_number.text


		#Can be multiple meeting places, times per day, etc.
		#There are identical schedule elements, annoying
		schedules = tab1_body.find_element_by_class_name('schedule')
		schedules2 = schedules.find_elements_by_class_name('schedule') #child

		schlist = []
		for schedule in schedules2:
			slot = {}
			days = schedule.find_element_by_class_name('days')
			time_schedule = schedule.find_element_by_class_name('time')
			instructor = schedule.find_element_by_class_name('instructor')
			
			slot['days'] = days.text
			slot['time'] = time_schedule.text 
			slot['instructor'] = instructor.text
			schlist.append(slot)
		
		section['schedule'] = schlist


		#also grab the notes at the bottom
		if check_exists_by_class_name(browser, 'notes'):
			notes = tab1.find_element_by_class_name('notes')
			section['notes'] = notes.text
		else:
			section['notes'] = 'none'



	#need to iterate over the rest of the tabs
	for i in range(2, number_of_tabs + 1):
		tab_num = selection.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/ul/li[' + str(i) + ']')
		tab_num.click()

		tab = selection.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/div[' + str(i) + ']')
		
		#Justs grabs all of the text in other tabs, not structured consistently 
		section[str(tabnames[i-1])] = tab.text

	#print(section)
	#add section to a list
	end.append(section)

browser.quit()



with open('result_coursedata.json', 'w') as fp:
    json.dump(end, fp)



print('done')
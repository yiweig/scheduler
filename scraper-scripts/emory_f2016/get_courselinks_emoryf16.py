from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

school = 'Emory'
year = '2016'
term = 'Fall'

browser = webdriver.Firefox()

browser.get('http://atlas.college.emory.edu/schedules/index.php?t=5169')
assert 'Course Atlas' in browser.title
assert year in browser.title
assert term in browser.title

#waiting for page to load
time.sleep(1)

#---------------------------------------------------------------
#--Gets names of courses and their abbreviations for later use
#---------------------------------------------------------------
l_abbrev = []
l_full = []
subjects = browser.find_element_by_id('list')
for subject_links in subjects.find_elements_by_tag_name('li'):
	text = subject_links.text
	abbreviation, full_name, *rest = text.split(' - ')
	
	l_abbrev.append(abbreviation)
	l_full.append(full_name)

#--------------------------------------------------------------
#--abbreviations can be used to access classes by subject like:
#--http://atlas.college.emory.edu/schedules/index.php?select=AAS
#--where select=(ABBREV)
#===============================================================

#---------------------------------------------------------------
#--Visits subject and grabs links to detailed class page
#---------------------------------------------------------------
l_courses = []
for abbreviation in l_abbrev:
	#to subject via abbreviation
	browser.get('http://atlas.college.emory.edu/schedules/index.php?select='+ abbreviation)
	time.sleep(5) #wait to load
	
	courses = browser.find_element_by_xpath('/html/body/div[2]/div[5]/div/div')
	for course in courses.find_elements_by_class_name('course'):
		for sections in course.find_elements_by_tag_name('a'):
			s_class_link = sections.get_attribute('href')
			l_courses.append(s_class_link)
			
			
	#back to main atlas
	browser.execute_script("window.history.go(-1)")
	time.sleep(2) #need a better page_is_loaded()

#---------------------------------------------------------------
#--Every class link is now in a list
#===============================================================



browser.quit()
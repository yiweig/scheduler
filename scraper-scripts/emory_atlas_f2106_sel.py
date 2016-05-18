from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

year = '2016'
term = 'Fall'

browser = webdriver.Firefox()

browser.get('http://atlas.college.emory.edu/schedules/index.php?t=5169')
assert 'Course Atlas' in browser.title
assert year in browser.title
assert term in browser.title

time.sleep(1)

l_abbrev = []
l_full = []
subjects = browser.find_element_by_id('list')
for subject_links in subjects.find_elements_by_tag_name('li'):
	text = subject_links.text
	abbreviation, full_name, *rest = text.split(' - ')
	
	l_abbrev.append(abbreviation)
	l_full.append(full_name)

#print(l_abbrev)
#print(l_full)

#print(len(l_abbrev))
#print(len(l_full))

#abbreviations can be used to access classes by subject
#eg http://atlas.college.emory.edu/schedules/index.php?select=AAS
#where select=(ABBREV)
l_courses = []
for abbreviation in l_abbrev:
	#to subject via abbreviation
	browser.get('http://atlas.college.emory.edu/schedules/index.php?select='+ abbreviation)
	time.sleep(5)
	
	#back to main atlas
	browser.execute_script("window.history.go(-1)")
	time.sleep(2) #need a better page_is_loaded()

	"""
	courses = browser.find_element_by_xpath('//div[@id="schedule-landing-page"]/div')
	i = 1
	for course in courses:
		name = course.find_element_by_xpath('//div['+ i +']')
		i = i + 1
		print(name)
	"""

	#print(course_names)
	"""
	courses_raw = browser.find_elements_by_class_name('course')
	for course in courses_raw:
		text_course = course.text
		print(text_course)
		l_courses.append[text_course.strip()]

	print(l_courses)
	break
	"""

browser.quit()



#http://atlas.college.emory.edu/schedules/index.php?t=5169
#http://atlas.college.emory.edu/schedules/index.php?select=AAS
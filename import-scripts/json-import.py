import json
import os
import sys

import django

sys.path.insert(0, '../scheduler/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler.settings')
django.setup()

from scraper.models import EmoryAtlasCourse

current_path = os.path.dirname(__file__)
relative_path = '../scraper-scripts/emory_f2016/result_coursedata.json'
json_path = os.path.join(current_path, relative_path)

with open(json_path) as json_file:
    json_data = json.load(json_file)
    for datum in json_data:
        # print(datum.keys())
        emory_course = EmoryAtlasCourse(
            related_courses=datum['Related Courses'],
            grading=datum['Grading'],
            opus_number=datum['opus_number'],
            name=datum['name'],
            credit=datum['credit'],
            notes=datum['notes'],
            ger=datum['ger'],
            resources=datum['Textbooks, Articles, and Resources'],
            description=datum['Descriptions'],
            topic=datum['topic'],
            schedule=datum['schedule']
        )
        print(emory_course)
    print('finished making objects')

'''
    related_courses = models.CharField(max_length=128)
    grading = models.CharField(max_length=32)
    opus_number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    credit = models.IntegerField
    notes = models.CharField(max_length=128)
    ger = models.CharField(max_length=32)
    resources = models.TextField
    description = models.TextField
    topic = models.CharField(max_length=128)
    schedule = models.CharField(max_length=512)


dict_keys(['Related Courses',
           'Grading',
           'opus_number',
           'name',
           'credit',
           'notes',
           'ger',
           'Textbooks, Articles, and Resources',
           'Descriptions',
           'topic',
           'schedule'])

           '''

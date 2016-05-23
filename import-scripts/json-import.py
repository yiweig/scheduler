import json
import sys
import os

current_path = os.path.dirname(__file__)
relative_path = '../scraper-scripts/emory_f2016/result_coursedata.json'
json_path = os.path.join(current_path, relative_path)

with open(json_path) as json_file:
    print('hello!')

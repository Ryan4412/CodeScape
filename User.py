import json
import os
from Stats import Stats

class User(object):
    def __init__(self):
        path: str = os.getcwd()
        # stats: str = f'{path}\\stats.json'
        json_file = open('stats.json')
        stats = json.load(json_file)
        print(stats['totalTime'])

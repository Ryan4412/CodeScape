import json
from Stats import Stats

class Session(object):

    def __init__(self, language_list):
        self.json_file = open('stats.json')
        self.data = json.load(self.json_file)
        self.language_list: list = language_list
        self.stats: Stats = Stats(self.data['totalTime'], self.data['totalExp'], self.data['totalLevel'], self.data['languages'], self.data['highestLevelLanguage'], language_list)
        print(self.stats.exp)

    def run(self):
        self.data['totalTime'] = self.stats.updateTime()
        self.data['totalExp'] = self.stats.updateExp()
        print(self.stats.exp)
        with open('stats.json', 'w') as update:
            json.dump(self.data, update, indent=2)



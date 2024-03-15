import json
from Stats import Stats
import filecmp

class Session(object):

    def __init__(self, language_list, path):
        self.json_file = open('stats.json')
        self.data = json.load(self.json_file)
        self.language_list: list = language_list
        self.stats: Stats = Stats(self.data['totalTime'], self.data['totalExp'], self.data['totalLevel'], self.data['languages'], self.data['highestLevelLanguage'], language_list)
        print(self.stats.exp)
        self.path = path
        # self.editing_files = editing_files # [c/user/project_dir/main.py]
        self.acceptable_languages = self.data['languages'] # a list of dictionaries ex: [{'extention': 'py', 'name': 'Python', 'time': 0, 'exp': 0, 'level': 0}]
        print(self.acceptable_languages)

    def run(self):
        self.data['totalTime'] = self.stats.updateTime()
        self.data['totalExp'] = self.stats.updateExp()
        print(self.stats.exp)
        for language in self.acceptable_languages:
            for extention in self.language_list:
                if(language.get('extention') == extention):
                    self.data['languages'] = self.stats.updateLang(extention)
        with open('stats.json', 'w') as update:
            json.dump(self.data, update, indent=2)



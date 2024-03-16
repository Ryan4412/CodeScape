import json
from JsonObject import JsonObject
from LevelSystem import LevelSystem

class DataSaver(object):

    def __init__(self, language_list, path):
        self.language_list: list = language_list # stores the list of languges being edited
        self.path = path # stores the path to the directory that we are listening to events from
        self.json_file = open('stats.json') # opens json file that stores all of our stats for the user
        self.data = json.load(self.json_file) # saves the json stats file to a python object

        self.jsonObject: JsonObject = JsonObject(self.data['totalTime'], self.data['totalExp'], 
        self.data['totalLevel'], self.data['languages'], self.data['highestLevelLanguage'], language_list) # parses the individual json fields into python objects

        self.level_system: LevelSystem = LevelSystem()

        print(self.jsonObject.exp)
        # self.editing_files = editing_files # [c/user/project_dir/main.py]
        self.languages = self.data['languages'] # a list of dictionaries ex: [{'extention': 'py', 'name': 'Python', 'time': 0, 'exp': 0, 'level': 0}]
        # print(self.languages)

    # def run(self):
    #     self.data['totalTime'] = self.statsUpdateHelper.updateTime()
    #     self.data['totalExp'] = self.statsUpdateHelper.updateExp()
    #     print(self.statsUpdateHelper.exp)
    #     for language in self.languages:
    #         for extention in self.language_list:
    #             if(language.get('extention') == extention):
    #                 self.data['languages'] = self.statsUpdateHelper.updateLang(extention)
    #     with open('stats.json', 'w') as update:
    #         json.dump(self.data, update, indent=2)

    def addXpToLanguageForGameTick(self, extention: str):
        language_to_update: dict = self.jsonObject.getLang(extention) # gets a copy of the current langs dictionary
        language_to_update['exp'] = self.level_system.calcXpForGameLoopTick(language_to_update['exp']) # updates the copy with the new xp value
        self.jsonObject.updateLang(language_to_update) # updates the lang list in the json object with the new data
        self.data['languages'] = self.jsonObject.langs
        with open('stats.json', 'w') as update:
            json.dump(self.data, update, indent=2)



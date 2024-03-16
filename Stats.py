class Stats():
    def __init__(self, time, exp, level, langs, higestLevelLang, languagesThisSession):
        self.time: int = time
        self.exp: int  = exp
        self.level: int = level
        self.langs: list = langs
        self.highestLevelLang: str = higestLevelLang
        self.languagesThisSession = languagesThisSession
    
    def updateTime(self):
        self.time += 5
        return self.time

    def updateExp(self):
        self.exp += 5
        return self.exp

    def updateLevel(self):
        self.level += 1
    
    def updateLang(self, extention):
        for lang in self.langs:
            if lang.get('extention') == extention:
                lang['time'] = lang.get('time') + 5
                lang['exp'] = lang.get('exp') + 5
                return self.langs
                # lang['level'] = lang.get('level') + 1 # need to handle level system
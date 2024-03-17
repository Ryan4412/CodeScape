

class LevelSystem(object):

    def __init__(self):
        self.exp_required_for_levelup: dict = {
            # 120 (10 minutes) total = 1.3 hours
            1: 0, 2: 120, 3: 240, 4: 360, 5: 480, 6: 600, 7: 720, 8: 840, 9: 960,
            #180 (15 minutes) total = 2.5 hours
            10: 1140, 11: 1320, 12: 1500, 13: 1680, 14: 1860, 15: 2040, 16: 2220, 17: 2400, 18: 2580, 19: 2760,
            #360 (30 minutes) total = 5 hours
            20: 3120, 21: 3480, 22: 3840, 23: 4200, 24: 4560, 25: 4920, 26: 5280, 27: 5640, 28: 6000, 29: 6360,
            #540 (45 minutes) total = 7.5
            30: 6900, 31: 6900, 32: 7440, 33: 7980, 34: 8520, 35: 9060, 36: 9600, 37: 10140, 38: 10680, 39: 11220,
            #600 (1 hour) total = 10 hours
            40: 11820, 41: 12420, 42: 13020, 43: 13620, 44: 14220, 45: 14820, 46: 15420, 47: 16020, 48: 16620, 49: 17220,
            #1200 (2 hours) total = 20 hours
            50: 18420, 51: 19620, 52: 20820, 53: 22020, 54: 23220, 55: 24420, 56: 25620, 57: 26820, 58: 28020, 59: 29220,
            #2400 (4 hours) total = 40 hours
            60: 31620, 61: 34020, 62: 36420, 63: 38820, 64: 41220, 65: 43620, 66: 46020, 67: 48420, 68: 50820, 69: 53220,
            #4800 (8 hours) total = 80 hours
            70: 58020, 71: 62820, 72: 67620, 73: 72420, 74: 77220, 75: 82020, 76: 86820, 77: 91620, 78: 96420, 79: 101220,
            #9600 (16 hours) total = 160 hours
            80: 110820, 81: 120420, 82: 130020, 83: 139620, 84: 149220, 85: 158820, 86: 168420, 87: 178020, 88: 187620, 89: 197220,
            # 19200 (32 hours) total = 360 hours
            90: 216420, 91: 235620, 92: 254820, 93: 274020, 94: 293220, 95: 312420, 96: 331620, 97: 350820, 98: 370020, 99: 389220
            # total time = 686.3 hours to hit level 99 in any language just based on game ticks
        }
    
    def calcXpForLineChange(self, lines_edited: int, current_exp: int) -> int:
        if lines_edited <= 0:
            return current_exp + 1
        
        if lines_edited >= 100:
            return current_exp + 100
        
        return current_exp + lines_edited

    def calcXpForGameLoopTick(self, current_exp: int) -> int:
        return current_exp + 5
    
    def calcXPForMakingNewFile(self, current_exp: int) -> int:
        return current_exp + 50
    
    def canLevelUp(self, language_level: int, current_xp: int) -> bool:
        return self.exp_required_for_levelup[language_level] <= current_xp
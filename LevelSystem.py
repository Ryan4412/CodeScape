

class LevelSystem(object):

    def __init__(self):
        self.exp_required_for_levelup: dict = {
            1: 0, 2: 720, 3: 2160, 4: 4320, 5: 7200, 6: 10800, 7: 15120, 8: 20160, 9: 25920,
            10: 32400, 11: 39600, 12: 47520, 13: 56160, 14: 65520, 15: 75600, 16: 86400, 17: 97920, 18: 110160, 19: 123120,
            20: 136800, 21: 151200, 22: 166320, 23: 182160, 24: 198720, 25: 216000, 26: 234000, 27: 252720, 28: 272160, 29: 292320, 30: 313200,
            31: 334800, 32: 357120, 33: 380160, 34: 403920, 35: 428400, 36: 453600, 37: 479520, 38: 506160, 39: 533520,
            40: 561600, 41: 590400, 42: 619920, 43: 650160, 44: 681120, 45: 712800, 46: 745200, 47: 778320, 48: 812160, 49: 846720,
            50: 882000, 51: 918000, 52: 954720, 53: 992160, 54: 1030320, 55: 1069200, 56: 1108800, 57: 1149120, 58: 1190160, 59: 1231920,
            60: 1274400, 61: 1317600, 62: 1361520, 63: 1406160, 64: 1451520, 65: 1497600, 66: 1544400, 67: 1591920, 68: 1640160, 69: 1689120,
            70: 1738800, 71: 1789200, 72: 1840320, 73: 1892160, 74: 1944720, 75: 1998000, 76: 2052000, 77: 2106720, 78: 2162160, 79: 2218320,
            80: 2275200, 81: 2332800, 82: 2391120, 83: 2450160, 84: 2509920, 85: 2570400, 86: 2631600, 87: 2693520, 88: 2756160, 89: 2819520,
            90: 2883600, 91: 2948400, 92: 3013920, 93: 3080160, 94: 3147120, 95: 3214800, 96: 3283200, 97: 3352320, 98: 3422160, 99: 3492720,
            # each level takes 1 more hour than before to move to the next
            # level 1 takes 1 hour, level 2 takes 2 hours, ... level 99 takes 99 hours
            # the cumulative time takes 4950 hours to go from level 1 - 99 for any language
        }
    
    def calcXpForLineChange(self, lines_edited: int) -> int:
        if lines_edited <= 0:
            return 1
        
        if lines_edited >= 100:
            return 100
        
        return lines_edited

    def calcXpForGameLoopTick(self, current_exp: int) -> int:
        return current_exp + 5
    
    def calcXPForMakingNewFile(self) -> int:
        return 50
    
    def canLevelUp(self, language_level: int, current_xp: int) -> bool:
        return self.exp_required_for_levelup[language_level + 1] <= current_xp
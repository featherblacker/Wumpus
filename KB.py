from logic import *
from Attributions import *
import math

manstate = ManState()
wumpus_kb = PropKB()

class KB1:
    def __init__(self):
        self.state = manstate.state

    # Method to deal with breeze
    def breeze(self, action):
        CP = action
        State = (np.array(self.state)).reshape(4, 4)
        x = int(CP / 4) + 1
        y = CP % 4 + 1
        # Add condtions
        wumpus_kb.tell(~expr("P" + str(int(x)) + str(y)))
        if "breeze" in State[x - 1][y - 1]:
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)))
        else:
            wumpus_kb.tell(~expr("B" + str(int(x)) + str(y)))

        # Logic of judge
        if (4 > x > 1)&(4 >= y >= 1):
            if y == 1:
                wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P" + str(int(x+1)) + str(y)) | expr("P" + str(int(x)) + str(y+1)) | expr("P" + str(int(x-1)) + str(y)))))
            elif y == 4:
                wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | (expr("P" + str(int(x+1)) + str(y))) | (expr("P" + str(int(x)) + str(y-1))) | (expr("P" + str(int(x-1)) + str(y))))
            else:
                wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P" + str(int(x)) + str(y-1))) | (expr("P" + str(int(x+1)) + str(y))) | (expr("P" + str(int(x)) + str(y+1))) | (expr("P" + str(int(x-1)) + str(y)))))
        elif (x == 1) & (4 > y > 1):
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P" + str(int(x+1)) + str(y))) | (expr("P" + str(int(x)) + str(y+1))) | (expr("P" + str(int(x)) + str(y-1)))))
        elif (x == 4) & (4 > y > 1):
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | (expr("P" + str(int(x-1)) + str(y)) | (expr("P" + str(int(x)) + str(y+1))) | (expr("P" + str(int(x)) + str(y-1)))))
        elif CP == 0:
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P21"))) | ((expr("P12"))))
        elif CP == 3:
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P13"))) | ((expr("P24"))))
        elif CP == 12:
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P31"))) | ((expr("P42"))))
        elif CP == 15:
            wumpus_kb.tell(expr("B" + str(int(x)) + str(y)) | '<=>' | ((expr("P43"))) | ((expr("P34"))))

        # Method to deal with stench
    def stench(self, action):
        CP = action
        State = (np.array(self.state)).reshape(4, 4)
        x = int(CP / 4) + 1
        y = CP % 4 + 1

        wumpus_kb.tell(~expr("W" + str(int(x)) + str(y)))
        if "stench" in State[x - 1][y - 1]:
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)))
        else:
            wumpus_kb.tell(~expr("S" + str(int(x)) + str(y)))

        if (4 > x > 1)&(4 >= y >= 1):
            if y == 1:
                wumpus_kb.tell(expr("S" + str(x) + str(y)) | '<=>' | ((expr("W" + str(x+1) + str(y)) | expr("W" + str(x) + str(y+1)) | expr("W" + str(x-1) + str(y)))))
            elif y == 4:
                wumpus_kb.tell(expr("S" + str(x) + str(y)) | '<=>' | (expr("W" + str(x+1) + str(y))) | (expr("W" + str(x) + str(y-1))) | (expr("W" + str(x-1) + str(y))))
            else:
                wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | ((expr("W" + str(int(x)) + str(y-1))) | (expr("W" + str(int(x+1)) + str(y))) | (expr("W" + str(x) + str(y+1))) | (expr("W" + str(x-1) + str(y)))))
        elif (x == 1) & (4 > y > 1):
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | ((expr("W" + str(int(x+1)) + str(y))) | (expr("W" + str(int(x)) + str(y+1))) | (expr("W" + str(x) + str(y-1)))))
        elif (x == 4) & (4 > y > 1):
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | (expr("W" + str(x-1) + str(y)) | (expr("W" + str(x) + str(y+1))) | (expr("W" + str(x) + str(y-1)))))
        elif CP == 0:
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | ((expr("W21"))) | ((expr("W12"))))
        elif CP == 3:
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | ((expr("W13"))) | ((expr("W24"))))
        elif CP == 12:
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | ((expr("W31"))) | ((expr("W42"))))
        elif CP == 15:
            wumpus_kb.tell(expr("S" + str(int(x)) + str(y)) | '<=>' | ((expr("W43"))) | ((expr("W34"))))

    # Unsure list
    def Unsure(self, PA):
        pa = PA
        for i in range (0, 16):
            if "up" in pa[i]:
                pa[i].remove("up")
                pa[i].append(i + 4)
                pa[i] = list(pa[i])
            if "down" in pa[i]:
                pa[i].remove("down")
                pa[i].append(i - 4)
                pa[i] = list(pa[i])
            if "left" in pa[i]:
                pa[i].remove("left")
                pa[i].append(i - 1)
                pa[i] = list(pa[i])
            if "right" in pa[i]:
                pa[i].remove("right")
                pa[i].append(i + 1)
                pa[i] = list(pa[i])
        return pa

    # Consider where to go
    def filter(self, PA, action):
        list = PA
        Action = action
        unsafe_list = []
        actionlist = list[Action]
        lenth = len(actionlist)
        # for Action in range(0, 15):
        if len(actionlist) != 0:
            self.safe_list = []
            for i in range(0, lenth):
                if wumpus_kb.ask_if_true(expr("P" + str(int(actionlist[i]/4) + 1) + str(actionlist[i] % 4 + 1))):
                    wumpus_kb.tell(expr("P" + str(int(actionlist[i] / 4) + 1) + str(actionlist[i] % 4 + 1)))
                    unsafe_list.append(actionlist[i])
                if wumpus_kb.ask_if_true(expr("W" + str(int(actionlist[i]/4) + 1) + str(actionlist[i] % 4 + 1))):
                    wumpus_kb.tell(expr("W" + str(int(actionlist[i] / 4) + 1) + str(actionlist[i] % 4 + 1)))
                    unsafe_list.append(actionlist[i])
                if wumpus_kb.ask_if_true((~expr("P" + str(int(actionlist[i] / 4) + 1) + str(actionlist[i] % 4 + 1)))
                                                 &(wumpus_kb.ask_if_true(~expr("W" + str(int(actionlist[i] / 4) + 1) + str(actionlist[i] % 4 + 1))))):
                    wumpus_kb.tell(~expr("P" + str(int(actionlist[i] / 4) + 1) + str(actionlist[i] % 4 + 1)))
                    wumpus_kb.tell(~expr("W" + str(int(actionlist[i] / 4) + 1) + str(actionlist[i] % 4 + 1)))
                    self.safe_list.append(actionlist[i])
            if Action == 0:
                self.safe_list = actionlist
        return self.safe_list

    # Heuristic
    def heuristic(self, action):
        for i in range(0,16):
            if "glitter" in manstate.state[i]:
                self.gold = i
        x1 = int(action / 4) + 1
        y1 = action % 4 + 1
        x2 = int(self.gold / 4) + 1
        y2 = self.gold % 4 + 1
        g = abs(x1 + y1 - x2 - y2)
        h = math.sqrt(abs(x1 - x2)) + math.sqrt(abs(y1 - y2))
        return g + h

    # Absolutely safe place
    def Safelist(self, safe_list, i):
        self.safe_list = safe_list
        self.i = i
        if len(self.safe_list) != 0:
            # f = []
            # ilist = []
            # for m in range(0, len(self.safe_list)):
            #     f.append(self.heuristic(self.safe_list[m]))
            #     if m > 0:
            #         if f[m] >= f[m - 1]:
            #             ilist.append(self.safe_list[m])
            #         else:
            #             ilist.append(self.safe_list[m - 1])
            self.i = choice(self.safe_list)
        else:
            self.i = -1
        return self.i
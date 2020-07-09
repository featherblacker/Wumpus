from Maps import *
from logic import *

map = Maps()

# Important attributions
class ManState:

    def __init__(self, payoff=0):
        self.state = map.randommaps()
        self.face = []
        self.payoff = payoff
        self.record = []
        self.bag = ["arrow"]
        self.possibleactions = []

        # Possible actions for every square
    def PossibleActions(self, action):
        self.action = action
        self.possibleactions = []
        if self.action < 12:
            self.possibleactions.append("up")
        if self.action > 3:
            self.possibleactions.append("down")
        if self.action not in (3, 7, 11, 15):
            self.possibleactions.append("right")
        if self.action not in (0, 4, 8, 12):
            self.possibleactions.append("left")
        return self.possibleactions

    # Record the trace
    def Record(self, action):
        self.record.append(action)

    # The orientation of person
    def Orientation(self, record):
        if len(record) > 2:
            if record[-2] == record[-1] + 4:
                self.face = "up"
            if record[-2] == record[-1] - 4:
                self.face = "down"
            if record[-2] == record[-1] - 1:
                self.face = "left"
            if record[-2] == record[-1] + 1:
                self.face = "right"

    # The condtions of arrow
    def Arrow(self, action):
        person = action
        if "arrow" in self.bag:
            graph = (np.array(self.state)).reshape(4, 4)
            i = int(person / 4)
            row = person % 4
            for m in range(0, 4):
                if "wumpus" in graph[m][row]:
                    graph[m][row].remove("wumpus")
                    self.payoff -= 10
                    wumpus_kb.tell(~expr("S" + str(i + 1) + str(row + 1)))
                    self.bag.remove("arrow")
                    print('Scream!')
            for n in range(0, 4):
                if "wumpus" in graph[i][n]:
                    graph[i][n].remove("wumpus")
                    self.bag.remove("arrow")
                    self.payoff -= 10
                    wumpus_kb.tell(~expr("S" + str(i + 1) + str(row + 1)))
                    print('Scream!')
        for a in range(0, 16):
            if "wumpus" not in self.state[a]:
                for b in range(0, 16):
                    if "stench" in self.state[b]:
                        self.state[b].remove("stench")

    # If there is gold in the square, pick it
    def pick(self, action):
        Action = action
        if "glitter" in self.state[Action]:
            self.bag.append("gold")
            self.state[Action].remove("glitter")
            self.payoff += 1000
            x = int(Action / 4) + 1
            y = Action % 4 + 1
            print("(", x, ",", y, ")")
            print("Get gold!")

    # The conditions of loss
    def Lose(self, action):
        Action = action
        if "pit" in self.state[Action]:
            self.payoff -= 1000
            x = int(Action / 4) + 1
            y = Action % 4 + 1
            print("(", x, ",", y, ")")
            print("Fall into pit")
        if "wumpus" in self.state[Action]:
            self.payoff -= 1000
            x = int(Action / 4) + 1
            y = Action % 4 + 1
            print("(", x, ",", y, ")")
            print("Catch by Wumpus")


# author: Liyuan Cao (300042723) & Qiguang Chu (300042722)

import numpy as np
from random import choice
import random

space = list(range(1, 16))

class Maps:
    # Establish squares
    def __init__(self):
        self.state = [['start!'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    # Simulaition 0
    def map0(self):
        self.state0 = [['start!'], ['breeze'], ['pit'], ['breeze'],
                       ['stench'], [], ['breeze'], [],
                       ['wumpus'], ['breeze', 'stench', 'glitter'], ['pit'], ['breeze'],
                       ['stench'], [], ['breeze'], ['pit']]
        return self.state0

    # Establish random maps
    def randommaps(self):

        # Choose gold location fisrt
        self.goldLocation = choice(space)
        self.state[self.goldLocation].append('glitter')
        space.remove(self.goldLocation)

        # Then choose Wumpus location
        self.wumpusLocation = choice(space)
        space.remove(self.wumpusLocation)
        self.state[self.wumpusLocation].append("wumpus")

        # There are stench around Wumpus
        if self.wumpusLocation < 12:
            self.state[self.wumpusLocation + 4].append("stench")
        if self.wumpusLocation > 3:
            self.state[self.wumpusLocation - 4].append("stench")
        if self.wumpusLocation not in (3, 7, 11, 15):
            self.state[self.wumpusLocation + 1].append("stench")
        if self.wumpusLocation not in (0, 4, 8, 12):
            self.state[self.wumpusLocation - 1].append("stench")

        # Then choose pits location
        self.pitLocation=[]
        pitState = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        for i in space:
            pitSpace = range(1, 6)
            pitState[i] = random.sample(pitSpace, 1)
            if pitState[i] == [1]:
                self.pitLocation.append(i)
                self.state[i].append('pit')
        # There are breeze around pits
        for a in range(0, len(self.pitLocation)):
            if self.pitLocation[a] < 12:
                self.state[self.pitLocation[a] + 4].append("breeze")
            if self.pitLocation[a] > 3:
                self.state[self.pitLocation[a] - 4].append("breeze")
            if self.pitLocation[a] not in (3, 7, 11, 15):
                self.state[self.pitLocation[a] + 1].append("breeze")
            if self.pitLocation[a] not in (0, 4, 8, 12):
                self.state[self.pitLocation[a] - 1].append("breeze")

        for i in range(0, 16):
            self.state[i] = list(set(self.state[i]))

        return self.state


#####################  show  ############################
    # Show squares
    def show(self, state):
        showstate = (np.array(state)).reshape(4, 4)
        showstate[[0, 3], :] = showstate[[3, 0], :]
        showstate[[1, 2], :] = showstate[[2, 1], :]
        for i in range(4):
            for j in range(4):
                print(showstate[i][j], end="")
            print("\n")

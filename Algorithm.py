from KB import *
import profile

f = 0
kb = KB1()
state = manstate.state
map.show(state)
Record = manstate.record
Action = 0
PA = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(0, 16):
    if i < 12:
        PA[i].append("up")
    if i > 3:
        PA[i].append("down")
    if i not in (3, 7, 11, 15):
        PA[i].append("right")
    if i not in (0, 4, 8, 12):
        PA[i].append("left")
# Try to find the gold
while "gold" not in manstate.bag:
    manstate.Record(Action)
    record = manstate.record
    manstate.Orientation(record)
    x = int(Action / 4) + 1
    y = Action % 4 + 1
    print("(", x, ",", y, ")")
    if "stench" in manstate.state[Action]:
        manstate.Arrow(Action)
    kb.breeze(Action)
    kb.stench(Action)
    possibleactions = manstate.PossibleActions(Action)
    unsure_list = kb.Unsure(PA)
    safe = kb.filter(PA, Action)
    Action = kb.Safelist(safe, Action)
    if "stench" in manstate.state[Action]:
        manstate.Arrow(Action)
    if len(manstate.record) > 1:
        if manstate.record[-1] in PA[manstate.record[-2]]:
            PA[manstate.record[-2]].remove(manstate.record[-1])
            if len(manstate.state[Action]) == 0:
                PA[manstate.record[-1]].append(manstate.record[-2])
        else:
            print("No way to go")
            break
    if Action == -1:
        print("No way to go")
        break
    manstate.pick(Action)
    manstate.Lose(Action)
    manstate.payoff -= 1
    if manstate.payoff < -1000:
        print('Game over!')
        break

print(manstate.payoff)

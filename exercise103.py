def record(nplayer, ngoals):
    return f"Player {nplayer.upper()} make {ngoals} goals."


name = str(input("Name: \n"))
if len(name) == 0:
    name = "<undefined>"

goals = str(input("Goals: \n"))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

print(record(name, goals))

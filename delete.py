import classes.enemyClass as enemyClass


list = []
for i in range(3):
    n = i
    randomEncounter = enemyClass.Wolf(name = "Wolf {}".format(i))
    list.append(randomEncounter)

print(list)

for wolf in list:
    print(wolf.name)

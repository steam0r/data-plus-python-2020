import random

def randomName(male):
    maleNames = ["stephan", "daniel", "alexander", "philipp"]
    femaleName = ["silke", "daniela", "maria", "bianca"]
    if(male):
        name = random.choice(maleNames)
    else:
        name = random.choice(femaleName)
    print(name)

print(name)
print(maleNames)

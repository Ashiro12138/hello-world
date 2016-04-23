#Init
points = int(300)
attack = int(0)
defence = int(0)
speed = int(0)
count = int(1)
area = ""
aream = int(0)

#Getting information
name = input("Name: ")
age = input("Age: ")

#Masteries System
print("There are 300 points avalible, you have 3 areas to put in, 150 max for each section.")
n = input("")
print("Points avaliable:",points)
print("Attack:",attack)
print("Defence:",defence)
print("Speed:",speed)
n = input("")
print("(add (area) amount) to add amount of point to an area")
print("(take (area) amount) to take amount of points from an area")
pointchange = input("Would you like to add or take?(add/take) ").lower()
while(True):
    if pointchange == "add":
        area = input("Which area? ").lower()
        if area == "attack":
            aream = int(input("How much? "))
            if attack + aream < 151:
                attack += aream
                points -= aream
        elif area == "defence":
            aream = int(input("How much? "))
            if defence + aream < 151:
                defence += aream
                points -= aream
        elif area == "speed":
            aream = int(input("How much? "))
            if speed + aream < 151:
                speed += aream
                points -= aream
    if pointchange == "take":
        area = input("Which area? ").lower()
        if area == "attack":
            aream = int(input("How much? "))
            if attack - aream > -1:
                attack -= aream
                points += aream
        elif area == "defence":
            aream = int(input("How much? "))
            if defence - aream > -1:
                defence -= aream
                points += aream
        elif area == "speed":
            aream = int(input("How much? "))
            if speed - aream > -1:
                speed -= aream
                points += aream
    if points == 0:
        break
    print("Points avaliable:",points)
    print("Attack:",attack)
    print("Defence:",defence)
    print("Speed:",speed)
    pointchange = input("Would you like to add or take?(add/take) ").lower()
print("Here are your stats:")
print("Attack:",attack)
print("Defence:",defence)
print("Speed:",speed)
n = input("")

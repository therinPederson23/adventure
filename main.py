import random
points = 250

print("Hello and welcome stranger! It's time for you to go on a great adventure!")
print("You will now allocate your skill points into your skills.")

strength = int(input("How many points do you want to put into strength? (from 0-100)\n>"))
if strength > 100 or strength < 0 or strength > points:
    print("You can't do that! You suck get rekt, no more game for you!")
    exit()

points = points - strength

print("Cool your strength is now at " + str(strength))
print("Now you have " + str(points) + " points remaining.")

dex = int(input("Now choose the amount of points you would like to put into dexterity? (from 0-100)\n>"))
if dex > 100 or dex < 0 or dex > points:
    print("Don't be a bot and break the rules! No more game for you!")
    exit()

points = points - dex

print("You have set your dexterity to " + str(dex))
print("You now have " + str(points) + " left over.")

combatability = int(input("How much points would you like to put into comabt ability? (from 0-100)\n>"))
if combatability > 100 or combatability < 0 or combatability > points:
    print("Don't put in to many points, that's illegal! No more game for you!")
    exit()

points = points - combatability

print("Your combat ability is now at " + str(combatability))
print("Your remaining points total up to " + str(points) + ".")
print("Now onto stealth.")

stealth = int(input("How stealthy would you like to be? (from 0-100)\n>"))
if stealth > 100 or stealth < 0 or stealth > points:
    print("Don't break the rules! Bye!")
    exit()

points = points - stealth

print("Your stealth is at " + str(stealth) + ".")
print("You have " + str(points) + " points remaining.")
print("Now for your final skill, magic!")

magic = int(input("What would you like your magic skill to be set at? (from 0-100)\n>"))
if magic > 100 or magic < 0 or magic > points:
    print("So sad that you broke the rules at the last skill. No more game for you!")
    exit()

print("Now that you have finished allocating your points it's time for the real adventure to begin!")
print("As your adventure begins you are walking down a path through the forest on a quest for some treasure.")
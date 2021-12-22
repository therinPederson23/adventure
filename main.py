import random
points = 250

print("Hello and welcome stranger! It's time for you to go on a great adventure!")
print("You will now allocate your skill points into your skills. You have 250 skill points to use on 5 skills.")

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
print("As you are walking down the path you come across a ravine. There is an old worn down bridge that is too dangerous to cross, however there is a tree that fell across the ravine that could suffice as a bridge.")
print("How will you cross the ravine?")
print("1. use the fallen tree to cross.")
print("2. use magic and levitate over the ravine.")
print("3. use your amazing leg strength and leap over the ravine.")
choice = input(">")

if choice = 1:
    roll = random.randrange(0, dex)
    if roll >= 20
        print("You carefully step onto the fallen tree, you take one step at a time until finally you reach the other side.")
    else:
        print("You out one foot onto the leg but then you slip, landing on the log and then tumbling down the ravine to your death.")
        print("Try not to be so clumsy next time.")
        exit()
elif choice = 2:
    roll = random.randrange(0, magic)
    if roll >= 20
        print("You use your magic to cast a levitation spell on your self and you gracefully glide to the other side of the ravine.")
    else:
        print("You cast a levitation spell on yourself except it failed, no worries though because you tried it again and it worked this time. However as you are almost to the other side of the ravine, your levitation spell fails and you fall to your death.")
        print("Maybe you should've put more points into magic.")
        exit()
elif choice = 3:
   roll = random.randrange(0, strength)
   if roll >= 20
        print("You step back and get a running start. You get to the edge of the ravine and take a glorius leap of faith. You landed safely on the other side of the ravine.")
   else:
        print("You run up to the ravine and jump, but you get a bad jump and smack right into the side of the ravine wall. You then fall down into the ravine, where you die.")
        print("This is why you don't skip leg day.")
        exit()
else:
    print("That is not allowed, the game will now end.")
    exit()

print("After successfully crossing the ravine you continue on your journey for treasure.")
print("During your walk down the path you see something in the distance. As you get closer you can see that it's bandits who have set up a roadblack, probably in hopes to catch any merchants passing by.")
print("How will you deal with these bandits?")
print("1. Try and sneak past them.")
print("2. Try to fight them off with your godly strength.")
print("3. Try to figth them with magic.")

if choice = 1:
    roll = random.randrange(0, stealth)
    if roll >= 30
        print("You step off of the main path and use the cover of the trees and foiliage to sneak past the bandits. For a moment you swear one saw but after a few seconds he looked away and you ended up sneaking past them.")
    else:
        print("you start sneaking to the side of the main path, hidden by the trees and various brushes, until you step on a twig. All of a sudden all of the bandits look at you and fire all of their crossbows towards you at once. There was no chance for survival as you were hit by every crossbow bolt fired.")
        print("Pro tip: Look where you're walking next time.")
        exit()
elif choice = 2:
    roll = random.randrange(0, strength)
    roll2 = random.randrange(0, combatability)
    if roll + roll2 >= 50
        print("You walk up to the bandits menacingly. They see you and fire their crossbow bolts at you, but you dodge them all with ease. You then rush in towards all of them beating them to pulps. After the battle you take all of their loot with you.")
    else:
        print("You confront the bandits and tell them thiw will be their end. They fire their crossbows at you and you take two hits, one to the knee and the other in your chest, rendering you helpless as they rush in and beat you to death.")
        print("Hint: Dodging helps.")
        exit()
elif choice = 3:
   roll = random.randrange(0, magic)
   roll2 = random.randrange(0, combatability)
   if roll + roll2 >= 55
        print("You decide to keep your distance from the bandits. You throw a fe fireballs in their direction, taking out 3 of them. They retaliate by shooting at you with crossbows, but you put up a magic shield and the bolts bounce off the shield harmlessly. You then summon a lighting cloud above the bandits striking down the rest of them. you try to take their loot but it is too charred to be worth anything.")
   else:
        print("You fight the bandits at a distance by thwoing ice shards at them. You ended up being very inaccurate and didn't hit any of the bandits. You were then too late to react as they show you with their crossbows.")
        print("Git Gud.")
        exit()
else:
    print("You're not supposed to break the rules!")
    exit()

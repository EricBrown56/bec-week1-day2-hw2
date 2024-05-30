# Identify errors in the following code:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        action == "cross a river"
        print("You found a boat!")
else: 
    place == "cave"
    print("You find a hidden treasure!")
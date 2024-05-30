# Create an adventure game using python

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You see a spike trap! Narrowly escaping death! Upon further inspection, you find a hidden treasure!")
        action = input("Do you want to take the treasure or leave it?")
        if action == "take the treasure":
            print("You took the treasure! Suddenly, the cave starts to fill with water! You must find a way out, but your torch has been extinguished!")
            action = input("Do you want to want to try to find a way out or do you put back the treasure?")
            if action == "find a way out":
                print("You found a secret passage! You made it out alive with the treasure! Risking your life was worth it! YOU WIN!")
            elif action == "put back the treasure":
                print("You left the treasure behind! However, the cave still fills with water and you drown! GAME OVER!")
            else:
                pass
        elif action == "leave it":
            print("You left the treasure behind even though it would make you rich! Proceeding further in the cave, you find a secret passage! In the passage, you see a corpse. There is something glistening in their hand.")
            action = input("Do you want to take the item or leave it?")
            if action == "take the item":
                print("You took the item! Just as you do, the corpse comes to life! It was a zombie! Before you can do anything, the zombie bites you! You become a zombie and live out the rest of your days in the cave! GAME OVER!")
            elif action == "leave it":
                print("You left the item behind! Proceeding further in the cave, you find a secret passage! You made it out alive! Even though you have no treasure, you are at least alive to tell the tale! Remembering your adventures, you decide to write a book about your time in the cave, which quickly becomes a best seller and you live off of the proceeds for the rest of your life! YOU WIN!")
            else:
                pass
    elif action == "proceed in the dark":
        print("Proceeding in the dark, you trip over a rock and fall into a pit! You are impaled on spikes! GAME OVER!")
    else:
        pass
else:
    pass
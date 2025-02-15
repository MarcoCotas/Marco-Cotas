name = input("Hey, type your name: ")
print(f"Hello {name}. Welcome to my game!")

shoud_we_play = input("Do you want to play? (Yes/No) ").lower().strip()
weapons = input("Choose your weapon: sword,or bow? ").lower().strip()
# Corrigido: Verifique cada condição separadamente
if shoud_we_play == "yes" or shoud_we_play == "y":
    print("Let's play!")
    direction = (
        input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
        .lower()
        .strip()
    )
    if direction == "left":
        action = (
            input("You encounter a monster. What will you do? Type 'run' or 'attack'")
            .lower()
            .strip()
        )
        if action == "run":
            print("You escaped the monster!")
        elif action == "attack" and weapons == "sword":
            print("You defeated the monster!")
            action = (
                input("Do you want to eat the monster or start a fire? ")
                .lower()
                .strip()
            )
            if action == "eat":
                print("You ate the monster and got sick!")
                print("You are dead!")
            elif action == "fire":
                print("You started a fire and some villagers saw the smoke")
        elif action == "attack" and weapons == "bow":
            print("You took out your bow and shot the monster in the eye!")
            print("The monster blinked and start laughting at you")
            print("You are dead!")
    elif direction == "right":
        treasure = input("You found a treasure chest!").lower().strip()
    else:
        print("You're lost. Game over!")
else:
    print(f"Ok {name}, see you next time!")

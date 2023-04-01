import os
from datetime import datetime
import player
import enemy
import dungeon

class Menu:
    def __init__(self):
        print("This will be an introduction message")
        print("\n\nMAIN MENU\n\n> NEW GAME\n> LOAD GAME\n> EXIT\n\n")
        choice = input("> ")
        if choice.lower() == "new game":
            NewGame()
        elif choice.lower() == "load game":
            LoadGame()
        elif choice.lower() == "exit":
            print("Thank you for playing, goodbye!")
            exit(0)
        else:
            print("Please choose one of the options")


class SaveGame:
    """Saves timestamp, current room, and player name, health, attack, defense, inventory"""
    def __init__(self, player_character):
        time_now = datetime.now().timestamp()
        save_name = player_character.name.lower() + ".save"
        print(f"Now saving...")
        cwd = os.getcwd()
        print(save_name, cwd)
        full_path = os.path.join(cwd, save_name)
        print(full_path)


class LoadGame:
    """Reads """
    def __init__(self):
        pass


class NewGame:
    def __init__(self):
        self.game_start()


    def game_start(self):
        print("Please enter your name:")
        name = input("> ").title()
        print("Please select your difficulty: \n\n> EASY\n> MEDIUM\n> HARD")
        health = {"easy": 5, "medium": 0, "hard": -5}
        difficulty = input("> ")
        print(f"Your name is {name} and you want to play on {difficulty}, correct?")
        choice = input("> ")
        if choice == "yes":
            print("cool")
        else:
            print("shame")
        player_character = player.Player(name, health[difficulty])
        SaveGame(player_character)
        #dungeon.CreateRoom(player_character)

class GameOver:
    def __init__(self, death):
        print(f"You died because of {death}")

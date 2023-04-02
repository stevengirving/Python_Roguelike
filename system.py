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
            Menu()


class SaveGame:
    """Saves timestamp, current room, and player name, health, attack, defense, inventory"""
    def __init__(self, player_character):
        pc = player_character
        time_now = datetime.now().timestamp()
        save_name = f"{pc.name.lower()}.save"
        print(f"Now saving...")
        cwd = os.getcwd()
        full_path = os.path.join(cwd, save_name)
        save_content = f"{time_now}|{pc.name}|{pc.stats}|{pc.inventory}"
        try:
            open(full_path, 'w').write(save_content)
            print(f"File saved successfully at {full_path}")
        except:
            print("Save failed")


class LoadGame:
    """Reads .save file to re-create player character at previous room"""
    def __init__(self):
        print("\nPlease choose your save file:\n")
        save_name = input("> ")
        try:
            saved_character = open(f"{save_name}.save").read().split("|")
        except:
            print("Save file not found\n")
            Menu()
        print(f"File information:\nSave time: datetime.fromtimestamp({saved_character[0]})\nPlayer name: {saved_character[1]}")
        player_character = player.Load(saved_character[1], saved_character[-1], saved_character[2], saved_character[3])
        print(player_character.name)
        dungeon.CreateRoom(player_character)

class NewGame:
    def __init__(self):
        self.game_start()


    def game_start(self):
        print("\nPlease enter your name:")
        name = input("> ").title().strip()
        print("\nPlease select your difficulty: \n\n> EASY\n> MEDIUM\n> HARD\n")
        health = {"easy": 5, "medium": 0, "hard": -5}
        difficulty = input("> ")
        print(f"\nYour name is {name} and you want to play on {difficulty}, correct?")
        choice = input("> ")
        if choice == "yes":
            print("\ncool")
        else:
            print("\nshame")
        player_character = player.Player(name, health[difficulty])
        dungeon.CreateRoom(player_character)

class GameOver:
    def __init__(self, death):
        print(f"You died because {death}")
        exit(0)

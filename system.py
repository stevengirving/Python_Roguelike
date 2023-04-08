import os
from datetime import datetime
import player
import enemy
import dungeon
from os import system as clear

class Menu:
    def __init__(self):
        clear("clear")
        print("Welcome to the game! This is a small randomized dungeon crawler.")
        print("\n\nMAIN MENU\n\n> NEW GAME\n> LOAD GAME\n> EXIT\n\n")
        choice = input("> ")
        if choice.lower() == "new game":
            NewGame()
        elif choice.lower() == "load game":
            LoadGame()
        elif choice.lower() == "exit":
            print("\nThank you for playing, goodbye!")
            input("\n> CLOSE")
            clear("clear")
            exit(0)
        else:
            print("Please choose one of the options")
            Menu()


class SaveGame:
    """Saves timestamp, player name, health, attack, room"""
    def __init__(self, player_character):
        pc = player_character
        time_now = datetime.now().timestamp()
        save_name = f"{pc.name.lower()}.save"
        save_health = pc.stats["health"]
        save_attack = pc.stats["attack"]
        save_room = pc.stats["room"]
        print("\nSave your game?\n\n> YES\n> NO\n")
        if input("> ") == "yes".lower():
            print(f"\nNow saving...\n")
            cwd = os.getcwd()
            full_path = os.path.join(cwd, save_name)
            save_content = f"{time_now}|{pc.name}|{save_health},{save_attack}|{save_room}"
            try:
                open(full_path, 'w').write(save_content)
                print(f"\nFile saved successfully at {full_path}")
            except:
                print("Save failed")
        else:
            print("No save made")


class LoadGame:
    """Reads .save file to re-create player character at previous room"""
    def __init__(self):
        print("\nPlease choose your save file:\n")
        save_name = input("> ")
        try:
            saved_character = open(f"{save_name}.save").read().split("|")
        except:
            print("Save file not found\n")
            input("\n> NEXT")
            Menu()
        saved_stats = saved_character[2].split(",")
        print("File information:\nSave time: ",
              datetime.fromtimestamp(float(saved_character[0])),
              f"\nPlayer name: {saved_character[1]}",
              f"\nRooms completed: {saved_stats[-1]}",
             )
        print("\nLoad game?")
        if input("> ") == "yes".lower():
            player_character = player.Load(saved_character[1],
                                           saved_stats,
                                          )
            dungeon.CreateRoom(player_character)
        else:
            clear("clear")
            Menu()

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
            print("\nThank you for confirming, please enjoy!")
        else:
            print("\nTry Again")
            NewGame()
        player_character = player.Player(name, health[difficulty])
        input("\n> START")
        clear("clear")
        dungeon.CreateRoom(player_character)

class GameOver:
    def __init__(self, death):
        print(f"\nYou died because {death}")
        input("\n> CLOSE")
        clear("clear")
        exit(0)

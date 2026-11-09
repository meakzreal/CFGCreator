
import os
import time

def start_system_cfg():
    print("Starting Cfg Editor!")
    time.sleep(1)
    cfg_editor()
    return True

def print_cfg():
    print("Printing CFG!")
    time.sleep(1)

    if os.path.exists("cfg.txt"):
        with open("cfg.txt", "r") as file:
            print(file.read())
    else:
        print("No CFG Found!")

def cfg_editor():
    GAME_NAME = input("game name? >> ").strip().lower()
    if GAME_NAME == "":
        GAME_NAME = "PLACEHOLDER"

    GAME_VERSION = input("Game Version? >> ").strip().lower()
    if GAME_VERSION == "":
        GAME_VERSION = "PLACEHOLDER"

    GAME_DIFFICULTY = input("Game Difficulty? >> ").strip().lower()
    if GAME_DIFFICULTY == "":
        GAME_DIFFICULTY = "PLACEHOLDER"

    GAME_RESPAWN_TIME = input("Game Respawn Time? >> ").strip().lower()
    if GAME_RESPAWN_TIME == "":
        GAME_RESPAWN_TIME = "PLACEHOLDER"

    PLAYER_STARTING_HEALTH = input("Player Starting Health >> ").strip().lower()
    if PLAYER_STARTING_HEALTH == "":
        PLAYER_STARTING_HEALTH = "PLACEHOLDER"

    PLAYER_MAX_HEALTH = input("Player Max Health >> ").strip().lower()
    if PLAYER_MAX_HEALTH == "":
        PLAYER_MAX_HEALTH = "PLACEHOLDER"

    PLAYER_STARTING_MONEY = input("Players Starter Cash? >> ").strip().lower()
    if PLAYER_STARTING_MONEY == "":
        PLAYER_STARTING_MONEY = "PLACEHOLDER"

    PLAYER_STARTING_LEVEL = input("Players Starting Level? >> ").strip().lower()
    if PLAYER_STARTING_LEVEL == "":
        PLAYER_STARTING_LEVEL = "PLACEHOLDER"

    PLAYER_XP_MULTIPLIER = input("Players Xp Multiplier? >> ").strip().lower()
    if PLAYER_XP_MULTIPLIER == "":
        PLAYER_XP_MULTIPLIER = "PLACEHOLDER"

    PLAYER_SPEED_MULTIPLIER = input("Players Speed Multiplier? >> ").strip().lower()
    if PLAYER_SPEED_MULTIPLIER == "":
        PLAYER_SPEED_MULTIPLIER = "PLACEHOLDER"

    WORLD_NAME = input("World Name? >> ").strip().lower()
    if WORLD_NAME == "":
        WORLD_NAME = "PLACEHOLDER"

    WORLD_SIZE = input("World Size? >> ").strip().lower()
    if WORLD_SIZE == "":
        WORLD_SIZE = "PLACEHOLDER"

    WORLD_BORDER = input("World Border? >> ").strip().lower()
    if WORLD_BORDER == "":
        WORLD_BORDER = "PLACEHOLDER"

    time.sleep(2)
    os.system("cls") if os.name == "nt" else os.system("clear")

    print("\n========== CONFIGURATION ==========")
    print(f"Game Name: {GAME_NAME}")
    print(f"Game Version: {GAME_VERSION}")
    print(f"Game Difficulty: {GAME_DIFFICULTY}")
    print(f"Game Respawn Time: {GAME_RESPAWN_TIME}")
    print(f"Player Starting Health: {PLAYER_STARTING_HEALTH}")
    print(f"Player Max Health: {PLAYER_MAX_HEALTH}")
    print(f"Player Starting Money: {PLAYER_STARTING_MONEY}")
    print(f"Player Starting Level: {PLAYER_STARTING_LEVEL}")
    print(f"Player XP Multiplier: {PLAYER_XP_MULTIPLIER}")
    print(f"Player Speed Multiplier: {PLAYER_SPEED_MULTIPLIER}")
    print(f"World Name: {WORLD_NAME}")
    print(f"World Size: {WORLD_SIZE}")
    print(f"World Border: {WORLD_BORDER}")

    CONFIRM = input("\nIs This Correct? (Yes/No) >> ").strip().lower()

    if CONFIRM == "yes":
        os.system("cls") if os.name == "nt" else os.system("clear")

        if os.path.exists("cfg.txt"):
            print("Found CFG!")

        with open("cfg.txt", "a") as file:
            file.write(
                f"=============\n"
                f"Game Name: {GAME_NAME}\n"
                f"Game Version: {GAME_VERSION}\n"
                f"Game Difficulty: {GAME_DIFFICULTY}\n"
                f"Game Respawn Time: {GAME_RESPAWN_TIME}\n"
                f"Player Starting Health: {PLAYER_STARTING_HEALTH}\n"
                f"Player Max Health: {PLAYER_MAX_HEALTH}\n"
                f"Player Starting Money: {PLAYER_STARTING_MONEY}\n"
                f"Player Starting Level: {PLAYER_STARTING_LEVEL}\n"
                f"Player XP Multiplier: {PLAYER_XP_MULTIPLIER}\n"
                f"Player Speed Multiplier: {PLAYER_SPEED_MULTIPLIER}\n"
                f"World Name: {WORLD_NAME}\n"
                f"World Size: {WORLD_SIZE}\n"
                f"World Border: {WORLD_BORDER}\n"
                f"=============\n"
            )

        print("SAVED!")
        time.sleep(1)
        return True

    elif CONFIRM == "no":
        return cfg_editor()

    else:
        print("Invalid Option!")
        return False

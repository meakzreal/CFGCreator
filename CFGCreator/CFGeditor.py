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
    cfg_editor()

def cfg_editor():
    GAME_NAME = input("game name? >> ").strip().lower()
    GAME_VERSION = input("Game Version? >> ").strip().lower()
    GAME_DIFFICULTY = input("Game Difficulty? >> ").strip().lower()
    GAME_RESPAWN_TIME = input("Game Respawn Time? >> ").strip().lower()
    PLAYER_STARTING_HEALTH = input("Player Starting Health >> ").strip().lower()
    PLAYER_MAX_HEALTH = input("Player Max Health >> ").strip().lower()
    PLAYER_STARTING_MONEY = input("Players Starter Cash? >> ").strip().lower()
    PLAYER_STARTING_LEVEL = input("Players Starting Level? >> ").strip().lower()
    PLAYER_XP_MULTIPLIER = input("Players Xp Multiplier? >> ").strip().lower()
    PLAYER_SPEED_MULTIPLIER = input("Players Speed Multiplier? >> ").strip().lower()
    PLAYER_FALL_DAMAGE = input("Fall Damage Enabled? (True Or False) >> ")
    PLAYER_FRIENDLY_FIRE = input("Friendly Fire Enabled? (True Or False) >> ")
    PLAYER_PVP_ENABLED = input("Player PVP Enabled? (True Or False) >> ")
    WORLD_NAME = input("World Name? >> ").strip().lower()
    WORLD_SIZE = input("World Size? >> ").strip().lower()
    WORLD_BORDER = input("World Border? >> ").strip().lower()
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
    print(f"Player Fall Damage: {PLAYER_FALL_DAMAGE}")
    print(f"Player Friendly Fire: {PLAYER_FRIENDLY_FIRE}")
    print(f"Player PVP: {PLAYER_PVP_ENABLED}")
    print(f"World Name: {WORLD_NAME}")
    print(f"World Size: {WORLD_SIZE}")
    print(f"World Border: {WORLD_BORDER}")

    CONFIRM = input("\nIs This Correct? (Yes/No) >> ").lower()
    
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
            f"Player Fall Damage: {PLAYER_FALL_DAMAGE}\n"
            f"Player Friendly Fire: {PLAYER_FRIENDLY_FIRE}\n"
            f"Player PVP: {PLAYER_PVP_ENABLED}\n"
            f"World Name: {WORLD_NAME}\n"
            f"World Size: {WORLD_SIZE}\n"
            f"World Border: {WORLD_BORDER}\n"
            f"=============\n"
            )
        print("SAVED!")
        time.sleep(1)
        exit()
        
    elif CONFIRM == "no":
        return True
    
    else:
        print("SAVED!")
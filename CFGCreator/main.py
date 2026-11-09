## ==========================================
## Project: Server.CFG
## Author: Meakz
## Purpose: Creating a Game CFG
## ------------------------------------------
## Version: 1.0
## Created: 08/11/2026
## File: main.py
## ==========================================

import os
import time
import CFGeditor
    
while True:
    def start_system():
     global choice_to_start
    os.system("cls")
    time.sleep(2)
    print("=======================")
    print("Opening System!")
    choice_to_start = input("Write CFG Using 'w' or 'exit' >> ").lower()
    
    if choice_to_start == "w":
        CFGeditor.start_system_cfg()
        
    elif choice_to_start == "exit":
        print("closing")
        exit()
        
        
    else:
        print("Invalid Please Press USE 'w' OR exit!")
        time.sleep(4)
        start_system()
        
start_system()
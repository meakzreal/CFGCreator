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
import CFGprinter
    
while True:
    def start_system():
     global choice_to_start
    os.system("cls")
    time.sleep(2)
    print("=======================")
    print("Opening System!")
    choice_to_start = input("Print CFG (p) OR Edit CFG (e) >> ").lower()
    
    if choice_to_start == "e":
        CFGeditor.start_system_cfg()
        
    elif choice_to_start == "exit":
        print("closing")
        exit()
        
    elif choice_to_start == "p":
        CFGprinter.print_cfg()
        
    else:
        print("Invalid Please Press USE P OR E OR exit!")
        time.sleep(4)
        start_system()
        
start_system()
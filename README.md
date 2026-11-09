# CFG Creator

A Python terminal program for creating game configuration files.

**Author:** Meakz  
**Version:** 1.0  
**Created:** 08/11/2026  
**Language:** Python  
**Storage:** `cfg.txt`

---

## WHAT IS IT?

CFG Creator is a Python program I made to create game configurations through the terminal.

Instead of manually writing settings into a file, the program asks you questions about your game, players and world, then puts everything together into a configuration.

Once finished, you can review everything before saving it to `cfg.txt`.

## FEATURES

- Create game configurations through terminal prompts.
- Set game name, version and difficulty.
- Configure player health, starting money and starting level.
- Set XP and player speed multipliers.
- Configure world name, size and border.
- Set game respawn time.
- Automatically use `PLACEHOLDER` when an input is left blank.
- Preview your configuration before saving.
- Confirm your settings before they are written to a file.
- Save multiple configurations to `cfg.txt`.

## CONFIGURATION SETTINGS

| Setting | Description |
|---|---|
| Game Name | Name of the game |
| Game Version | Current game version |
| Game Difficulty | Game difficulty setting |
| Game Respawn Time | Player respawn time |
| Player Starting Health | Health players start with |
| Player Max Health | Maximum player health |
| Player Starting Money | Starting player cash |
| Player Starting Level | Starting player level |
| Player XP Multiplier | XP multiplier |
| Player Speed Multiplier | Player speed multiplier |
| World Name | Name of the world |
| World Size | Size of the world |
| World Border | World border setting |

## PROJECT STRUCTURE

```text
CFGCreator/
│
├── main.py
├── CFGeditor.py
├── cfg.txt
└── README.md
```

| File | Purpose |
|---|---|
| `main.py` | Main menu and program startup. |
| `CFGeditor.py` | Handles configuration creation and saving. |
| `cfg.txt` | Stores generated configurations. |

## HOW TO USE

Make sure Python 3.x is installed.

Open a terminal inside the `CFGCreator` folder and run:

```bash
python main.py
```

Select `w` to start creating a configuration.

Answer the questions presented in the terminal.

Once all settings have been entered, the program displays your configuration and asks whether everything is correct.

Type `yes` to save or `no` to enter the settings again.

Configurations are saved to `cfg.txt`. New configurations are added underneath existing ones.

## IMPORTS I USED

**`os`**

Used for clearing the terminal and checking whether files exist.

Documentation: https://docs.python.org/3/library/os.html

**`time`**

Used for adding delays between messages and actions in the terminal.

Documentation: https://docs.python.org/3/library/time.html

## LIMITATIONS

This is currently a prototype and a personal Python project.

The generated configurations are saved as normal text. They aren't automatically applied to a game or server.

Settings are also currently entered as text rather than being validated against specific game requirements.

## WHY I MADE IT

I wanted to make something where I could actually create and save game settings rather than just manually writing everything into a text file.

It's also given me a chance to practise Python using functions, multiple files, user input and file handling.

Still working on it and planning to add more configuration options!

---

pretty cool project if you ask me.

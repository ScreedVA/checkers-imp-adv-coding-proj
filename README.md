# 🏁 Checkers Implementation in Python 
> Built within the pygame framework as a university project

## Table of Contents
- Introduction
- Features
- Installation
- Usage
- Contact Info
- Dependancies
- References

## Introduction
This package is an implementation of the well known checkers board game, and the rules are based on the international draughts guidelines. The checkers-main package consists of 2 modules utility and game each responsible for handling thier respective features for the game. This is my first time creating a project of this scale using pygame.

## Features
- Graphical User Interface
- Multiplayer Mode: Play 1v1 with a second player
- Save and Load Games: Your previous game is auto-saved upon quitting 
- Checker Rule Implementation: Game rules are based on international checkers guidelines


## Installation
### Installation from GitHub
To install the application:


Create project directory(In Terminal)
```bash
mkdir checkers-imp-adv-coding-proj-techscreed
```

Enter directory(In Terminal)
```bash
cd checkers-imp-adv-coding-proj-techscreed
```

Clone repository(In Terminal)
```bash
git clone https://github.com/ScreedVA/checkers-imp-adv-coding-proj.git
```

Move into repository directory(In Terminal)
```bash
cd checkers-imp-adv-coding-proj
```

Create virtual environment (In Terminal)
```bash
python -m venv .venv
```

Activate virtual environment (In Terminal)
```bash
.venv\Scripts\activate
```

Update pip if nessasary (In Terminal) 
```bash
python.exe -m pip install --upgrade pip
```

Install package dependancies (In Terminal)
```bash
pip install -r requirements.txt
```

### Installation from Pypi
Create project directory (In Terminal)
```bash
mkdir checkers-imp-adv-coding-proj-techscreed
```

Enter directory (In Terminal)
```bash
cd checkers-imp-adv-coding-proj-techscreed
```

Create virtual environment(In Terminal)
```bash
python -m venv .venv
```

Activate virtual environment(In Terminal)
```bash
.venv\Scripts\activate
```

Install package from Pypi(In Terminal)
```bash
pip install checkers-imp-adv-coding-proj
```

## Usage - After Installed with Pypi
> There are 2 ways you can run this package
### Example 1 Running package with CLI Command
Run application (In Terminal)
```bash
run_checkers_round
```
>  Output:
You have no previous games, Starting round...

### Example 2 Running package through execution file
Create project directory (In Terminal)
```bash
mkdir checkers-imp-adv-coding-proj-techscreed
```

Enter project directory (In Terminal)
```bash
cd checkers-imp-adv-coding-proj-techscreed
```

Create file for execution and import main from checkers-main package (In Terminal)
```bash
echo > main.py "from checkers_main import main"
```

Call main function in main.py (In Script)
```bash
if __name__ == "__main__":
    main()
```

Run application execution file (In Terminal)
```bash
python main.py
```

## Usage - After Installed from GitHub
### Example 1 Running package through execution file
Enter repository directory if not already (In Terminal)
```bash
cd checkers-imp-adv-coding-proj
```

Run application execution file (In Terminal)
```bash
python main.py
```
>  Output:
You have no previous games, Starting round...

## Example 2 Installing and Running Package locally with Egg files
Enter repository directory if not already (In Terminal)
```bash
cd checkers-imp-adv-coding-proj
```

Install package locally (In Terminal)
```bash
pip install -e .
```

Run package locally with CLI command(In Terminal)
```bash
run_checkers_round
```

## Contact Info
[LinkedIn Profile](https://www.linkedin.com/in/christian-damete-yeboa-bb79442a3/)


## Dependancies
- Pygame Framework handles graphical user interface functionality
- Pillow Library is used for image manipluation and cropping
- Json libary handles python dictionary to json serialization


## References
- The render_game_env() method which utilizes modular congruences to asses rows and columns to draw evenly positioned squares is inspired from an article by Sundar Sing - Singh, S. (2017, December 10). [D3: Modulo operation to create a grid.](https://medium.com/@eesur/d3-modulo-operation-to-create-a-grid-f47101831a ) 

- The game images used throughout the project are by "andi" on [OpenGameart.ORG](https://opengameart.org/content/checkers) 



# Checkers Implementation in Python 
> Built within the pygame framework as a university project

## Table of Contents
- Introduction
- Features
- Installation
- Usage
- Contact Info
- Dependancies

## Introduction
This project is comprised of 2 modules within the mypackage directory each responsible for handling thier respective features for the game, This project took around 20 - 25 hours to complete including research and experimentation with the pygame framework. This is my first time creating a project of this scale using pygame.

## Features
- Graphical User Interface
- Multiplayer Mode: Play 1v1 with a second player
- Save and Load Games: Your previous game is auto-saved upon quitting 
- Checker Rule Implementation: Game rules are based on international checkers guidelines


## Installation
### Installation from GitHub
To install the application:

Clone repository
```bash
git clone https://github.com/ScreedVA/checkers-imp-adv-code-proj.git
```

Move into repository directory
```bash
cd checkers-imp-adv-code-proj
```

Create virtual environment
```bash
python -m venv .venv
```

Activate virtual environment
```bash
.venv\Scripts\activate
```

Install pip (if nessasary) 
```bash
python -m pip install --upgrade pip
```

Install package locally
```bash
pip install -e .
```
### Installation from Pypi

Create project directory
```bash
mkdir checkers-imp-adv-code-proj-techscreed
```

Enter directory
```bash
cd checkers-imp-adv-code-proj-techscreed
```

Create virtual environment
```bash
python -m venv .venv
```

Activate virtual environment
```bash
.venv\Scripts\activate
```

Install package from Pypi
```bash
pip install checkers-imp-adv-code-proj
```

## Usage
### Example 1
Run application
```bash
run_checkers_round
```
>  Output:
You have no previous games, Starting round...

### Example 2
Run application
```bash
run_checkers_round
```
>  Output:
Would you like to load(L) your previous game or start a new game(N)

```bash
N
```
> Output: 
Starting new round...

### Example 3
Run application
```bash
run_checkers_round
```
>  Output:
Would you like to load(L) your previous game or start a new game(N)

```bash
L
```
> Output: 
Loading previous round...


## Contact Info
[LinkedIn Profile](https://www.linkedin.com/in/christian-damete-yeboa-bb79442a3/)


## Dependancies
- Pygame Framework handles graphical user interface functionality
- Pillow Library is used for image manupluation and cropping
- Json libary handles python dictionary to json serialization



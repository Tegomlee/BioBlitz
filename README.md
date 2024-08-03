# BioBlitz

## Description

This is a simple Agar.io clone I made in python using pygame-ce. The player controls a cell that eats other cells. Some are inanimate while a select few are controlled by AI (Not a real AI model). Will you come out on top?

## Features

* Player movement in all 8 directions with applied normalization
* Rendering using a dynamic rendering surface
* Managing multiple objects using object pooling techniques

## Installation

This project uses python 3.12 and pygame-ce 2.5.0 (SDL 2.30.3). Make sure you have at least these versions installed.

If you dont have the dependencies installed or want to ensure you have the dependencies installed, follow the dependencies instructions below first, then follow the project instructions.

### Dependencies

1. **Check for python installation**

Run the `python` or `python3` command from your preferred command console.
You should get an output that says the version number, make sure it is either 3.12 or above. Below is an example of what mine looks like.
```bash
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
If you get something else, like what I put below as an example, you have to [download python](https://www.python.org/downloads/). Follow the instructions and add python to your system's path.
```bash
'python' is not recognized as an internal or external command, operable program or batch file.
```
```bash
'python3' is not recognized as an internal or external command, operable program or batch file.
```

2. **Check for pygame-ce installation**

Once you have verified your python installation, run the `python` or `python3` command and then run `import pygame`. It should display the version of pygame-ce and SDL (pygame-ce's interal graphics API). Below is an example of what you should see:
```bash
>>> import pygame
pygame-ce 2.5.0 (SDL 2.30.3, Python 3.12.3)
```
If you get the error below, follow the instructions to install [pygame-ce](https://pyga.me/docs/index.html) by running `pip install pygame-ce` or `pip3 install pygame-ce` on a new command console window.
```bash
>>> import pygame
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pygame'
```

### Project

1. **Clone the repository**
```bash
git clone https://github.com/Tegomlee/BioBlitz.git
```
2. **Navigate to the directory**
```bash
cd path-to-repository-installation
```
3. **Run the python application**
```bash
python main.py
```
```bash
python3 main.py
```

## Goals

This is a learning project for me and not intended to be distributed as a complete software. The main goals of this project are:

* Learning how to use python effectively using modules and creating your own as well as following best practices.
* Finish a project by effectively using time-management and detering scope creep
* Learning how to use GitHub, Licensing a game, and documenting my project.

## License

This project is licensed under the **GPL v3.0** license. For more details, see the full license text in the [LICENSE](./LICENSE) file.

This license allows you to freely use, modify, and distribute the software, provided that any derivative works also comply with the GPL v3.0 terms.

## Disclaimer

This project is provided "as-is" without any warranties. It is intended for educational purposes and is not affiliated with, endorsed by, or associated with Agar.io or its creators. All trademarks, logos, and copyrights associated with Agar.io are the property of their respective owners.
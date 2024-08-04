"""
    BioBlitz is an Agar.io clone in python I wrote for Educational purposes
    Copyright (C) 2024  Bryan Sanchez

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
File: debug.py
Description: Defines the Debug class to introduce some more utility to print
             statements. Will also have colors in the console
Author: Bryan Sanchez [Tegomlee]
Date: 08-03-2024
License: GPL v3.0

Dependencies:
- colorama
- typing
- datetime
"""

from colorama import Fore, Style
from typing import Any
from datetime import datetime

class Debug:

    @staticmethod
    def log(param: Any) -> None:
        time_string = datetime.now().strftime("%H:%M:%S")
        print(f"[LOG] [{time_string}] - {param}")


    @staticmethod
    def log_warning(param: Any) -> None:
        time_string = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.YELLOW}[WARNING] [{time_string}] - {param}{Style.RESET_ALL}")


    @staticmethod
    def log_error(param: Any) -> None:
        time_string = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[ERROR] [{time_string}] - {param}{Style.RESET_ALL}")

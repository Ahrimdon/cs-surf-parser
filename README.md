# Counter-Strike Surf Times Parser

![image](assets/surf.png)

## Table of Contents

- [Counter-Strike Surf Times Parser](#counter-strike-surf-times-parser)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Instructions](#instructions)
  - [License](#license)

## Introduction
Haven't you always wanted to neatly organize your Counter-Strike surf times? Well now you can! Counter-Strike Surf Times Parser is a handy Python script that allows you to parse and sort your Counter-Strike surf times with ease. The script offers three different sorting methods - Rank, Time, or Alphabetical Order of the map name. This allows you to have a concise and organized view of your best (or worst) surf times!

## Features
- **Efficient Parsing**: Efficiently parses your Counter-Strike surf times from your `console.log`.
- **Sorting**: Offers three different sorting methods for easy viewing:
  - Rank
  - Time
  - Alphabetical Order
- **Output**: Outputs the sorted data to a log file.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have a `Windows/Linux/Mac` machine running Python 3.5 or later.
  * When installed choosing `ADD TO PATH` is recommended.
* Your Counter-Strike `console.log` file is updated with your latest surf times.

## Instructions
Follow the steps below to use the Counter-Strike Surf Times Parser:

1. **Step 1**: Change `Enable Developer Console (~)` to `Yes` and type `con_logfile console.log`
  * Your can add this to your `autoexec.cfg` to log the console automatically
2. **Step 2**: In game, use the command to display your rank (e.g. !rank), select your Name and then select `Finished Maps`. This will print your finished maps to the console as well as output it to the log file
3. **Step 3**: Open your `console.log` (usually C:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/csgo/console.log), and copy **ONLY** your completed surf maps into a new file named `surf_maps.log` (make sure the script is in the same directory)
4. **Step 4**: Navigate to the folder in Terminal (e.g. `cd C:/path/to/folder`) and use the command `python parse_surf_maps.py`. Select the desired method of sorting.
5. **Step 5**: Your parsed and sorted maps will be in a new file named `parsed_surf_maps.log`


## License
Distributed under the MIT License. See `LICENSE` for more information.

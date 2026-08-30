==================================================
              OOP COFFEE MACHINE
==================================================

DESCRIPTION
-----------
A Python console application that simulates an automated coffee 
vending machine using Object-Oriented Programming (OOP) principles. 
It processes user orders, manages resource levels, handles coin-based 
payments, and calculates change.

FEATURES
--------
* Order Selection: Supports ordering Espresso, Latte, or Cappuccino.
* Inventory Checking: Verifies if water, milk, and coffee are available.
* Payment System: Accepts quarters, dimes, nickels, and pennies, 
  verifying sufficient payment and issuing change.
* Maintenance Commands: 
  - "report" : Displays current resource levels and total profits.
  - "off"    : Powers down the machine execution loop.

PROJECT STRUCTURE
-----------------
* main.py           : Execution entry point and main application loop.
* menu.py           : Defines 'Menu' and 'MenuItem' classes for drinks.
* coffee_maker.py   : Defines 'CoffeeMaker' class to track resources.
* money_machine.py  : Defines 'MoneyMachine' class to process coins.

HOW TO RUN
----------
1. Ensure Python 3.x is installed.
2. Run the main script from your terminal:
   python main.py

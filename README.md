# python-calculator
A simple calculator built in Python with a loop and input validation.
This is a basic calculator code written in python language
# Functionalities:
- It can perform the "+","-","/","*" operations
- In case of operator other than that the program show a message saying Invalid operator
- In case of someone write the num1 & num2 in alphabets or like 90/ the program show Enter a valid number as this one is invalid, but the program does not stop it is also asking you Do you want to perform another calculation at the same time. It is because of using Try/except code.
- In case of "/" operation the program will first check that if num2==0 it will say the denominator can't be                  zero. 
- While loop is used in this program which allow the user to keep performing calculation as they are giving                  the input as Yes.
- It can accept the input as Yes,yes,YES,yEs because with condition the lower() method is used.
- It also accepts space before and after yes because strip() method is used.
## Requirements
- First python 3 must be installed
## How to run cal.py
- Open cal.py in visual stuido code and then click on run in the top left side of VS Code and click on start debugging
- After that terminal will be open and is asking you for input
- Once the program works and then stops, to again start it just type this command in terminal `py cal.py` and it will again ask you for the input.


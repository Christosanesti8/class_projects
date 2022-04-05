# Brandon French
# french_lab4.py
# March 29, 2022
# inputs an operator and two numbers of the user's choice
# and outputs them into an expression.

operand = input ("Please select one option: add/subtract/multiply/divide: ")
if operand == "divide" or operand == "subtract" or operand == "multiply" or operand == "add":
    print (f"You chose to {operand}!")
    num_one = input ("Please select your first number: ")
    float_one = float(num_one)
    num_two = input ("Please select your second number: ")
    float_two = float(num_two)
    if operand == "divide":
        print (f"{float_one} / {float_two} = {float_one/float_two}")
    elif operand == "multiply":
        print (f"{float_one} * {float_two} = {float_one*float_two}")
    elif operand == "add":
        print (f"{float_one} + {float_two} = {float_one+float_two}")
    else:
        print (f"{float_one} - {float_two} = {float_one-float_two}")
    input(f'Thank you for using this calculator! Press "Enter" to exit.')

else:
    input(f'Your input {operand} is incorrect. Please press "Enter" to try again.')


# Brandon French
# french_lab3.py
# March 29, 2022
# chooses one operator, then inputs numbers to calculate.

operand = input ("Please select one option: add/subtract/multiply/divide: ")
if operand == "divide" or operand == "subtract" or operand == "multiply" or operand == "add":
    print (f"You chose {operand}!")
    num_one = input ("Please select your first number: ")
    num_two = input ("Please select your second number: ")
    float_one = float(num_one)
    float_two = float(num_two)
else:
    print (f"Your input {operand} is not valid.")

if operand == "divide":
    print (f"{float_one} / {float_two} = {float_one/float_two}")
elif operand == "multiply":
    print (f"{float_one} * {float_two} = {float_one*float_two}")
elif operand == "add":
    print (f"{float_one} + {float_two} = {float_one+float_two}")
else:
    print (f"{float_one} - {float_two} = {float_one-float_two}")

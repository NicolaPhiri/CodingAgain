"""
Name: Nicola
Surname: Phiri
Project name: Odd or Even
Date: 13/09/26
"""

intNumber = int(input("Please enter a number: "))
intRemainder = intNumber % 2
if intRemainder == 0:
    print(f"{intNumber} is an even number.")

else:
    print(f"{intNumber} is an odd number.")
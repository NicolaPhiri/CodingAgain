"""
Name: Nicola
Surname: Phiri
Date: 13/09/26
Task Name: Favorite number
"""
strName = input("What is your name?: ")
intCurrentAge = int(input("How old are you?: "))
intFavoriteNumber = int(input("What is your favorite number?: "))
intFutureAge = intCurrentAge + 5
inFavoriteNumberAge = intFutureAge * intFavoriteNumber

print(f"Hi {strName}! In 5 years, you will be {intFutureAge}.\n{intFutureAge} x {intFavoriteNumber} = {inFavoriteNumberAge}")
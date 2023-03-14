## Control Flow with if / else and Conditional Operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


## Exercise 1 - Odd or Even
"""Instructions
Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

therefore: 6 % 2 = 0

5 ÷ 2 = 2 x 2 + 1, remainder is 1.

therefore: 5 % 2 = 1

14 ÷ 4 = 3 x 4 + 2, remainder is 2.

therefore: 14 % 4 = 2"""

number = 56

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number")

## if-elif-else

if condition1:
    do A
elif condition2:
    do B
else:
    do this

## Exercise 2 - BMI 2.0

"""Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

Example Input
weight = 85
height = 1.75
Example Output
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.

The testing code will check for print output that is formatted like one of the lines below:

"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

bmi = 22

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


"""Exercise 3 - Leap Year

Instructions:

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, 
leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, 
this video does it more justice: https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input 1
2400
Example Output 1
Leap year.
Example Input 2
1989
Example Output 2
Not leap year.

"""

year = int(input("Which year do you want to check? "))

"""  Refer to the flow chart here: 
https://bit.ly/36BjS2D    """

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


""" Multiple If Statements in Succession

Multiple If Statements:

if condition1:
 do A
if condition2:
 do B
if condition3:
 do C


Refer to the flow chart here: 
https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

"""
Exercise 4 - Pizza Order Practice

Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

Example Input
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
Example Output
Your final bill is: $28.

"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

"""
***Logical Operators***
A and B ----> True
C or D------> False
not E-------> if it's True, becomes False. If it's False then it becomes True

this flow chart:
https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day%203%20Logical%20Operators.drawio#R7VtZc9o6FP41zH2iY0teH0uWZpqkQy%2BZ29CXOwYrthNjUVkQyK%2BvjGWwLbEFL6HTzCSxjyVhfec7myQ68GKy%2BEKcqX%2BPXRR2gOIuOvCyA4CqAYP9SyTLVGJqXOCRwOWNNoJB8Ia4UOHSWeCiuNCQYhzSYFoUjnEUoTEtyBxC8Gux2RMOi586dTwkCAZjJxSlPwKX%2BqnUAuZGfoMCz88%2BWTXs9MnEyRrzmcS%2B4%2BLXnAhedeAFwZimV5PFBQoT8DJc0n7XW56uX4ygiB7SoR9ZTw%2FfyQD19fm%2Fc3dxF%2FzCXT6NmC6zCSOXzZ%2FfYkJ97OHICa820h7Bs8hFyagKu9u0ucN4yoQqEz4jSpdcmc6MYiby6STkT9kLk%2BVj0v%2BTAUEmGDJBV%2FmkmHomuVzwz0jvlvm7PiLBBFFEuFBEgwMU4xkZox0QZKxyiIfojnZ62i7BJ%2FcBHOsvCLO3IUvWgKDQocG8yB%2BH09Bbt%2BNdPxPiLHMNpjiIaJwbuZ8IWANuUZABthqR25Oq63mts4t0xOwu92ob0YoZR7DEbpklmqrlWaJ8TIJotRBEYICqFQlgK8UR0vfknTbMOJZohtE8zzgWcyeccXS4b01cm%2BFMGHF6Hl0pU1GZz5904LVATeLjyWjGZtl79QOKBlNnpd1XFp%2BKBNvKiDkiFC126jB7qppFlLKw9bqJFarBZX4uTpSVlld7DuPjIYRtmOr7bQscaFtq1bZ1EshA4OmAzYCKVFwDq%2B6n41MQhhc4xGTVF7o6stzE7cWU4BeUe2KBEWTWWQ2BYZHAQMJfIOGvVhd%2FNQHaCyf6J%2FEALD1EpyFcAV5QKcIlsXfLrAeuy682%2BL%2F%2FzaXPLvk%2BvOl71zdexsRzMXddNHfptD6WuesyTn4URgKzZMENUlLuqhUBrm9YgInNjhaxcMLAi9j1mGGRZG29BIOAVWKf%2BYNJ4LopgVEcvDmj1VAJhXkqw8bVex39MhmLcTZO6VsRzFYp0ENbQBlK%2FCSoDWUxVxqi%2BOxhBpa2F2etJpylnkiMR2143FwttK6OD6mEDvLUuzzwXk9tVO2p5dUIUJKZ55kBgV4cZEvd847aRA6I8lfx%2BXZWWyFa%2FtZ%2FzbLQzm4tgVKGP3%2B8PfT6PwfImj8%2BPAS9STtZKloE9DF3Pdzoid1tNJPcFFaO2laoFMLWMuJdb52LiskyepsrMcASAoQiSYQlqYNeW23Wsk9qhsD1JADHrlaqsKh8zSpthpTzCRvual9c3tzbWy8XUzXnIoYkKWUq1HTRBBuuRu3i%2Bgi0RBu0a1pOkiJlCkjdoThOHK6%2FKuElecO5lUxqGfMD%2FV5tJRNoJVN%2BvwerPJPdsnMHyhFKL6ugZrdhbXEb4iZw84tYejl6t%2B051vRpJ3qrzUTvyuuEd0VvXTkuekPNOiF6l3s3Hb3tLWYoiUVN26FmfLD4LVnmVEFXtc4%2BakNV8Hi6iLXeZNxWoYg1A1rBJPnDpnb%2BoB%2BQKpmNpkqyTH6rD1D2%2BwBhs9gYW2j0VNpejnCUqMB1Yn%2FtXCqAVzeL8AKJ91Bl%2BK6PSJwCsH3%2F%2BGI8erfgFvwKlvfPN8v%2BfVekdBtR%2FaD4vGvZJ7885M%2FnXfx0iYKv9n%2Bz5a06uDNesnnWncPqalHDh2awRx8%2BsuSZcmWnj3ZgLcRlsZxpOiwbWnthWQqVaFafPYYHUJIlCKXLfnVxLeLcooVuvm9BsYpoITXyViqSg3zXLp%2B013dVfrD2JJBbCRDZXkW2IXHkXgWofrPiJI2aH0qjorN6dSJ%2BpjRMPNKIZbbG6lzp1MfMi5x0qlTIwJTVjzwDq8BLlQ%2FqrkNyPulSbNFNWXW5Ka1VC1pbzTD3pIXdvl2u7swMSDz%2FliZG4lnjoxKjpi0FlnZtDNlhbaWmNEoKrFj9%2FQlnuMo4r9fXGjjDtcuacjA%2F%2BCgxQ0ydpPMoSMeIVzFBW5wXrVmeWoDblKSpKrCz1aZGiC3uNPwBR0ABLEVaCa8rOgPKbjdfDEzr283XK%2BHVbw%3D%3D
 
 
if condition1 & condition2 & condition3:
  do this
else:
 do this
  

"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


"""
***Exercise 5 - Love Calculator***

Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.

The testing code will check for print output that is formatted like one of the lines below:

"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."

Score Comparison
Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

Name 1	Name 2	Score
Catherine Zeta-Jones     	Michael Douglas    	99
Brad Pitt	Jennifer Aniston	73
Prince William	Kate Middleton	67
Angela Yu	Jack Bauer	53
Kanye West	Kim Kardashian	42
Beyonce	Jay-Z	23
John Lennon	Yoko Ono	18

Hint
The lower() function changes all the letters in a string to lowercase.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

The count() function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

"""


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:45]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print):
    with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print)

  def test_1(self):
    self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')

  def test_2(self):
    self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')

  def test_3(self):
    self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')

  def test_4(self):
    self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py')

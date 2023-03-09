#Data Types
#Strings
print("Hello"[0])

print("123" + "345")

#Integer

print(123 + 345)

#Float
3.45857

#Boolean
True
False
##  Booleans don't have quotation marks around them, otherwise it would turn them into a String.

num_char = len(input("what is your name?"))

##print("Your name has" + num_char + "characters.")

print(type(len(input("what is your name?"))))

new_num_char = str(num_char)

print("Your name" + " " + new_num_char + "characters.")

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print(str(70) + str(100))

### Instructions

## Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

## Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

## Example Input
# 39
## Example Output
#3 + 9 = 12
#12

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
3 + 5
type(two_digit_number)
print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

result = first_digit + second_digit
print(result)

print(type(first_digit))

result = int(first_digit) + int(second_digit)
print(result)

## Exercise 2 - BMI Calculator

# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Example Input
weight = 80
height = 1.75
# Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837
26

## Hint
# 1.Check the data type of the inputs.
# 2.Try to use the exponent operator in your code.
# 3.Remember PEMDAS.
# 4.Remember to convert your result to a whole number (int).

# 🚨 Don't change the code below 👇
height = input("enter your height in m:  ")
weight = input("enter your weight in kg:  ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# bmi = weight / height ** 2
print(type(height))

bmi = int(weight)/ float(height) ** 2
print(bmi)
#26.122448979591837

bmi_as_int = int(bmi)
print(bmi_as_int)
#26

## Number Manipulation and F Strings in Python

8 / 3
#2.6666666666666665
print(round(8 / 3))
#3

print(round(8 / 3, 2))
#2.67

print(round(2.66666666666666 , 2))
#2.67

print(8 // 3)
#2
type(print(8 // 3))
#int

print(4 / 2)
#2.0

result = 4 / 2
result /= 2
print(result)
#1 . Because it's four divide by two, then divided by two again.

score = 0
height = 1.8
isWinning = True
# User scores a point
score += 1
print(score)
#1

print("Your score is" + score)
#TypeError: can only concatenate str (not "int") to str

print("Your score is" + str(score))
#Your score is1

## f-String in Python -----> It is very important that the f string is preceded by single or double quotes

print(f"your score is {score}", your height is {height}, you are winning is {isWinning})

## Exercise 3 - Life in Weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
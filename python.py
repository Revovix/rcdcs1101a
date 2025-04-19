# This prints out the sum of 5 + 3
a = 5
b = 3
sum = a + b
print("The sum of 5 + 3 is", sum)

# This function determines if the inputed numeber is odd or even
number = int(input("\nPlease enter a number:"))
if number % 2 == 0:
    print("It's even")
else:
    print("It's odd")

# This prints out a random number ranging from 1 to 6
for i in range(1, 6):
    print(i)

# This prints out the sum of given 2 set of number by the user
print("Please enter 2 number for addition")
x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
print("Result:", x + y)

# Make the user guess a number between 1 and 10
secret = 10
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret:
    print("Correct")
else:
    print("Try again!")
# Made the secret number 10 because the previous number (100) was not listed

# Ask the user for their name
name = input("What is your name? ")

# Say hello
print("Hello, " + name + "!")

H = "Hello"
W = "World"
def greet():
    print(H + " " + W)
greet()

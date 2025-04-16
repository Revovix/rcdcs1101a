a = 5
b = 3
sum = a + b
print(" The sum is:", sum)

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("It's even")
else:
    print("It's odd")

for i in range(1, 6):
    print(i)

x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
print("Result:", x + y)

secret = 100
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret:
    print("Correct")
else:
    print("Try again!")

# Ask the user for their name
name = input("What is your name? ")

# Say hello
print("Hello, " + name + "!")

H = "Hello"
W = "world"
def greet():
    print(H + W)
greet()


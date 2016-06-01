# Call this file intro.py
# This is the first class
# This is some new Python stuff
# I don't know what a virtual environment is
# Help
# Help really
# Hello world
# print "Hello world" doesn't work!!!
print("Hello world!")
print('Hello world!')

# Can't do this thing that doesn't
# even make sense anyway
# print("Hello world!')

print(10)

print(10 + 10)

# Won't put a space
print("Hello" + "world!")

print("Hello" + " " + "world!")
print("Hello " + "world!")

# http://stackoverflow.com/questions/961632/converting-integer-to-string-in-python
# >>> str(10)
# '10'

print("Hello" + str(10))
print("Hello" + "10")

print("Hello, Soma")
print("Hello, " + "Soma")

# Variables are magic
# Variables are good
name = "Dennis"
print("Hello, " + name)

name = input("What's your name?")
print("Hello, " + name)

year_of_birth = input("What year were you born in? ")
age = 2016 - int(year_of_birth)
print("You are roughly " + str(age) + " years old")
# Secret trick if you wanna put a bunch
# of things together
print("You are roughly", age, "years old")

# Make sure all of your stuff is in order
if age == 33 or age > 100:
    print("So cool!!!! You get a free beer unit!!!!")
elif age >= 21:
    print("Here's your beer unit")
elif age >= 19:
    print("Why don't you have a fake ID?")
elif age >= 13:
    print("Hey cool teen give me some tips about snapchat")
elif age >= 2 and age < 4:
    print("I'm glad you can talk now")
elif age < 0:
    print("You are an idiot, or from the future which is also stupid")
else:
    print("Nope, sorry")

print("Goodbye")

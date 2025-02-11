# Part A - Intro
# Ask the user for their name and save it to a variable!

name = input("What is your name? ")

# Store their answer in the variables below.
summer = 2
fall = 2
winter = 1
spring = 1

# Part B - Questions

# Question #1
print("What color do you like the most?")
print(" 1) Red")
print(" 2) Blue")
print(" 3) Green")
print(" 4) Yellow")
color = input("Enter the number of your choice: ")

# If they like red, add a point to summer
# If they like blue, add a point to winter
# If they like green, add a point to spring
# If they like yellow, add a point to fall

if color == "1":
    summer += 1
elif color == "2":
    winter += 1
elif color == "3":
    spring += 1
elif color == "4":
    fall += 1

# Question #2
print("Do you like warm or cold?")
print(" 1) Warm")
print(" 2) Cold")
warm_cold = input("Enter the number of your choice: ")

# If they like warm, add a point to summer and spring
# If they like cold, add a point to fall and winter

if warm_cold == "1":
    summer += 1
    spring += 1
elif warm_cold == "2":
    fall += 1
    winter += 1

# Question #3
print("Do you like drinking warm drinks or cold drinks?")
print("1) Warm Drinks")
print("2) Cold Drinks")
drink_choice = input("Enter the number of your choice: ")

# If they like warm drinks, ask them if they like hot cocoa or tea
# If they like hot cocoa, add a point to winter
# If they like tea, add a point to spring
# If they like cold drinks, ask them if they like lemonade or iced tea
# If they like lemonade, add a point to summer
# If they like iced tea, add a point to fall

if drink_choice == "1":
    print("Do you prefer hot cocoa or tea?")
    print("1) Hot Cocoa")
    print("2) Tea")
    warm_drink = input("Enter the number of your choice: ")
    if warm_drink == "1":
        winter += 1
    elif warm_drink == "2":
        spring += 1
elif drink_choice == "2":
    print("Do you prefer lemonade or iced tea?")
    print("1) Lemonade")
    print("2) Iced Tea")
    cold_drink = input("Enter the number of your choice: ")
    if cold_drink == "1":
        summer += 1
    elif cold_drink == "2":
        fall += 1 

# Question #4
print("What activity do you like to do outside?")
print("1) Swimming")
print("2) Skiing")
print("3) Gardening")
print("4) Hiking")
activity = input("Enter the number of your choice: ")

# If they like to swim, add a point to summer
# If they like to ski, add a point to winter
# If they like to garden, add a point to spring
# If they like to hike, add a point to fall

if activity == "1":
    summer += 1
elif activity == "2":
    winter += 1
elif activity == "3":
    spring += 1
elif activity == "4":
    fall += 1

# Question #5
print("What month were you born in?")
month = input("Enter your birth month: ")

# If they were born in June, July, or August, add a point to summer
# If they were born in September, October, or November, add a point to fall
# If they were born in December, January, or February, add a point to winter
# If they were born in March, April, or May, add a point to spring

if month in ["June", "July", "August"]:
    summer += 1
elif month in ["September", "October", "November"]:
    fall += 1
elif month in ["December", "January", "February"]:
    winter += 1
elif month in ["March", "April", "May"]:
    spring += 1

# Part C - Results

# Based on the answers, print out the season they are most like!
# Use conditionals to do this.

# How can you find the season with the max count?
# Remember that in the event of a tie, the user should be sorted into
# the season in alphabetical order, so if there is a tie between summer 
# and spring, the user should be sorted into spring.

season = "None"
max_score = 0

if summer > max_score:
    season = "Summer"
    max_score = summer
if fall > max_score:
    season = "Fall"
    max_score = fall
if winter > max_score:
    season = "Winter"
    max_score = winter
if spring > max_score:
    season = "Spring"
    max_score = spring

# The following code does not need to be changed
print("Thank you for taking the quiz,", name, "!")
print("You are most like", season, "!")
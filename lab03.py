# Part A - Temperature Conversion
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Test the function
print("Celsius to Fahrenheit (0°C):", celsius_to_fahrenheit(0))

# Part B - Inches to Centimeters
# Function to convert inches to centimeters
def inches_to_centimeters(inches):
    return inches * 2.54

# Test the function
print("Inches to Centimeters (10 inches):", inches_to_centimeters(10))

# Part C - Total Bill Calculation
# Function to calculate the total bill including tip
def total_bill(meal_cost, tip_percent):
    return meal_cost + (meal_cost * tip_percent / 100)

# Test the function
print("Total Bill ($50 meal, 20% tip):", total_bill(50, 20))
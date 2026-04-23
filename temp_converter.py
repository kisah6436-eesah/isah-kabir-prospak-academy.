# 1. Get Celsius Temperature
celsius_str = input("30*c: ")

# 2. Convert to Float
celsius_value = float(celsius_str)

# 3. Apply Formula: (C * 9/5) + 32
fahrenheit_value = (celsius_value * 9/5) + 32

# 4. Print Result (formatted to 1 decimal place)
print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_value:.1f} degrees Fahrenheit.")

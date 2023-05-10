# Create a fuzzy set
temperature = [0, 20, 30, 40]

# Create membership functions for the fuzzy set
low = lambda x: min(x, 20) / 20
medium = lambda x: max(0, min(x - 20, 10)) / 10
high = lambda x: max(0, x - 30) / 10

# Get the membership value of a specific input
temperature_value = 25

low_membership = low(temperature_value)
medium_membership = medium(temperature_value)
high_membership = high(temperature_value)

# Print the membership values
print(low_membership)
print(medium_membership)
print(high_membership)

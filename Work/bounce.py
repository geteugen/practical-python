# bounce.py
#
# Exercise 1.5
height = 100  # Meters
factor = 3 / 5  # New height vs old height
bounce_index = 1

while bounce_index <= 10:
    height = height * factor
    print(bounce_index, round(height, ndigits=4))
    bounce_index = bounce_index + 1

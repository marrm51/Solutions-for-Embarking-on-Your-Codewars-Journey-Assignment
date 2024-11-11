# Problem 1: Create a function that takes an integer as an argument and returns 
# "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd_v1(number):
    return "Even" if number % 2 == 0 else "odd" 
# Solution: using the modulo operator 

# Problem 2: We need a function that can transform a number (integer) into a string.

def number_to_string_v1(number):
    return str(number)
# Solution: using a str() function

# Problem 3: Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def count_vowels_v1(input_str):
    vowels = "aeiou"
    count = 0 
    for char in input_str: 
        if char in vowels: 
            count += 1 
# Solution: Using a for loop and conditional check
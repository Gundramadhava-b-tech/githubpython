# Remove Vowels from a Given String

input_string = "This is an example string."
vowels = "aeiouAEIOU"
result_string = ""

for char in input_string:
    if char not in vowels:
        result_string += char

print(result_string)

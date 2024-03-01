# Mutable List Example
my_list = [1, 2, 3, 4]
print("Original List:", my_list)

# Modify the list
my_list[2] = 10
print("Modified List:", my_list)  # Output: [1, 2, 10, 4]

# Immutable String Example
my_string = "Hello"
print("Original String:", my_string)

# Try to modify the string (this will raise an error)
# my_string[0] = 'h'  # Uncommenting this line will raise TypeError

# Create a new string with modification
new_string = my_string.replace('H', 'h')
print("Modified String:", new_string)  # Output: hello

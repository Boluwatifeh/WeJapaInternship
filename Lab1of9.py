# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

# .capitalize() method, this method capitalizes the first letter in a word
first_name = 'boluwatife'
print(first_name.capitalize())

# .title(), this method capitalizes the first string in every word
print('hello, world'.title())

# .upper() returns a string with all character in uppercase
print('hello, world'.upper())

# .swapcase() returns a copy of the string with uppercase characters converted to lowercase and vice versa.
print('HELLO, WORLD'.swapcase())

# .strip()
print('www.wejapa.com'.strip('w'))

# .startswith returns tue if a string starts with a prefix and false otherwise
comment = 'we-japa internship is the best to acquire relevant tech skills'
print(comment.startswith('we'))

# .replace()
full_name = 'Israel Boluwatife'
print(full_name.replace('Israel', 'Ogundeyi'))

# islower()
print('these are all lower case letters'.islower())

# String Data Type

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

str3 = '123'
# str3 = str3 + 1 # TypeError: can only concatenate str (not "int") to str.

x = int(str3) + 1 # Converting numbers in a string into a number by using int().
print(x)

# Reading and Converting
name = input('Enter:')

print(name)

apple = input('Enter:')

# x = apple - 10 # TypeError: unsupported operand type(s) for -: 'str' and 'int'.

x = int(apple) - 10 # Input numbers converted from strings.
print(x)

# Looking Inside Strings
fruit = 'banana'
# b a n a n a
# 0 1 2 3 4 5
letter = fruit[1] # Getting second character from a string by using an index specified in [].
print(letter)

x = 3
w = fruit[x -1]
print(w)

# A Character Too Far
zot = 'abc'
# print(zot[5]) # IndexError: string index out of range.

# Strings Have Length
fruit = 'banana'
print(len(fruit)) # The built-in function len gives us a length of a string.

# Looping Through Strings
fruit = 'banana'
index = 0
# Loop will run 6 times and each time will print index and letter that is in that string at the index.
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# for Statement Example Through Strings
fruit = 'banana'
for letter in fruit:
    print(letter)

# Looping and Counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a': # Counting letter "a" by the loop in a string.
        count = count + 1
print(count)

# Slicing Strings
s = 'Monty Python'
print(s[0:4]) # Slicing from 0 to 4 but don't include 4.

print(s[6:7]) # Slicing from 6 to 7 but don't include 7.

print(s[6:20]) # Slicing from 6 to 20 so is more than a string letters it gives from 6 to the end of a string.

print(s[:2]) # Slicing from beginning of the string until 2 but don't include 2.

print(s[8:]) # Slicing from 8 to the end of the string.

print(s[:]) # Prints full string.

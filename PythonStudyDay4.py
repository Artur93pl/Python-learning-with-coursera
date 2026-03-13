#Numeric Expressions

# Addition
xx = 2
xx = xx + 2
print(xx)

# Multiplication
yy = 440 * 12
print(yy)

# Division
zz = yy / 1000
print(zz)

# Remainder
jj = 23
kk = jj % 5
print(kk)

# Power
print(4 ** 3)

ee = ('hello' +  'there')
print(ee)

# Several types of Numbers.
# Numbers have two main types.
# Integers are whole numbers like: -14, -2, 1, 100, 401233.
xx = 1
type (xx) # xx is a integer.
print(xx)

# Floating Point Numbers have decimal parts: -2.5, 0.0, 98.6, 14.0.
temp = 98.6
type(temp) # temp is a float.
print(temp)

# Type Conversions.
# When you put an integer and floating point in an expression,
# the integer is implicitly converted to a float.

print(float(99) + 100)

i = 42
type(i)

f = float(i)
print(f)

type(f)
# You can control this with the built=in functions int() and float().

# Integer Division produces a floating point result.
print(10 / 2)

print(9 / 2)

print(99 / 100)

# String Conversions
# You can also use int() and float() to convert between strings and integers.

sval = '123'
type(sval)

ival = int(sval)
type(ival)
print(ival + 1)

# You will get error if the string does not contain numeric characters.

# User Input
# We can instruct Python to pause and read data from the user using the input() function.

nam = input('Enter your name: ')
print('Welcome', nam)
# The input() function returns a string.
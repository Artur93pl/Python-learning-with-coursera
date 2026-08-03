def thing(): # Creating a new function.
    print("Hello")
    print("Fun")

thing() # Calling the thing function.
print("Zip")
thing()

# Max Function
big = max("Hello world")
print(big)

tiny = min("Hello world")
print(tiny)

# Type Conversions
print (float(99) / 100)

i = 42
type(i)

f = float(i)
print(f)

type(f)

print(1 + 2 * float(3) / 4 - 5)

# String Conversions
# You will get an error if the string does not contain numeric characters
sval = "123"
type(sval)
# print(sval + 1) this will give back traceback error

# Int Function
ival = int(sval)
type(ival)
print(ival + 1)

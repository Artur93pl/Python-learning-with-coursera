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

x = 5
print("Hello")

def print_lyrics(): # This function was not invoke
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print("Yo")
print_lyrics() # Now I call (invoke) the function
x = x + 2
print(x)

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'pl':
        print('Czesc')
    else:
        print('Hello')
greet('es')

greet('pl')

greet('en')

# Return values

def greet():
    return 'Hello'

print(greet(), 'Glenn')
print(greet(), 'Arturo')

# Multiple Parameters / Arguments
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

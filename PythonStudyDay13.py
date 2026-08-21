# String Concatenation

a = 'Hello'
b = a + 'There'
print(b)

print("---")

c = a + ' ' + 'There'
print(c)

print("---")
# Using in as a Logical Operator

fruit = 'banana'
'n' in fruit
# True
'm' in fruit
# False
'nan' in fruit
# True
if 'a' in fruit:
    print('Found it!')

print("---")

# String Comparison
word = input('Enter a word: ')

if word == 'banana':
    print('All right, bananas')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas')

print("---")

# String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print("---")
print(greet.upper())
print("---")
print('Hi There' .lower())

print("---")

stuff = 'Hello world'
print(type(stuff)) # Class str.

print(dir(stuff)) # Methods in class str.

print("---")

# Searching a String
fruit = 'banana'
pos = fruit.find('na')
print(pos)

print("---")

aa = fruit.find('z')
print(aa)

print("---")

# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)

print("---")

nstr = greet.replace('o','X')
print(nstr)

print("---")

#Stripping Whitespace
greet = '   Hello Bob   '
greet.lstrip() # Remove whitespace at the left.
greet.rstrip() # Remove whitespace at the right.
greet.strip() # Removes both beginning and ending whitespace.

# Prefixes
line = 'Please have a nice day'
line.startswith('Please')
# True
line.startswith('p')
# False

# Parsing and Extracting
data = 'From stephen.marguard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # Position 21.

print("---")

sppos = data.find(' ', atpos)
print(sppos) # Position 31.

print("---")

host = data[atpos+1 : sppos]
print(host)

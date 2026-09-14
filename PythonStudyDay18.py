# Best Friends: Strings and Lists
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)

line = 'A lot           of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)

print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))

print("\n----------------------\n" )

# The Double Split Pattern

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
print(pieces[1])

print("\n----------------------\n" )


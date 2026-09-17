# What Is Not A "Collection"?
x = 2
x = 4
print(x)

print("\n----------------------\n" )

# Lists (Review)
cards = list()
cards.append(12)
cards.append(3)
cards.append(75)
print(cards)
print(cards[1])
cards[1] = cards[1] + 2
print(cards)

print("\n----------------------\n" )

# Dictionaries
cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)
print(cabinet['fall'])
cabinet['fall'] = cabinet['fall'] + 2
print(cabinet)

print("\n----------------------\n" )

# Comparing Lists and Dictionaries
lst = list()   # Lists use numbers to look up values
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()   # Dictionaries use keys to look up values
ddd['age'] = 21
ddd['course'] = 183
print(ddd)
ddd['age'] = 23
print(ddd)

print("\n----------------------\n" )

# Dictionary Literals (Constants)
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100 }
print(jjj)
ooo = { }
print(ooo)

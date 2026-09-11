# A list Is a Kind of Collection


friends = [ 'Joseph', 'Glenn', 'Sally']

carryon = [ 'socks', 'shirt', 'perfume']

# List Constants

print([1, 24, 17])

print(['red', 'yellow', 'blue'])

print(['red', 24, 98.6])

print([ 1, [5, 6], 7])

print([])

# Lists and Definite Loops - Best Pals
friends = [ 'Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

z = [ 'Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')

# Looking Inside Lists

friends = [ 'Joseph', 'Glenn', 'Sally'] # 0 is Joseph, 1 is Glenn and 2 is Sally
print(friends[0])

# List Are Mutable
fruit = 'Banana'
# fruit[0] = 'b' gives Traceback 'str' object doses not supported
# Strings are "immutable"
x = fruit.lower()
print(x)

lotto = [2, 14, 26, 41, 63]
print(lotto)

lotto[2] = 28 # Lists are "mutable"
print(lotto)

# How Long is a List?
greet = 'Hello Bob'
print(len(greet))

x = [1, 2, 'joe', 99]
print(len(x))

# Using the Range Function
print(range(4))
friends = [ 'Joseph', 'Glenn', 'Sally']
print(len(friends))

print(list(range(len(friends))))

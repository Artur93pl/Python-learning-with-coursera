# Concatenating Lists Using +

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

print("\n----------------------\n" )

# Lists Can Be Sliced Using :
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

print("\n----------------------\n" )

# List Methods
x = list()
print(type(x))
print(dir(x))

print("\n----------------------\n" )

# Building a List from Scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

print("\n----------------------\n" )

# Is Something in a List?
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

print("\n----------------------\n" )

# Lists are in Order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])

print("\n----------------------\n" )

# Built-in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

print("\n----------------------\n" )

# Counting in a Loop
from PythonStudyDay9 import largest_so_far

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing in a Loop

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Finding the Average in a Loop

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# Filtering in a Loop

print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

# Search Using a Boolean Variable

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3 :
        found = True
    print(found, value)
print('After', found)

# How To Find the Smallest Value
small_so_far = -1
print('Before', small_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < small_so_far:
        small_so_far = the_num
    print(small_so_far, the_num)
print('After', small_so_far)

# Using None flag value

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None :
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

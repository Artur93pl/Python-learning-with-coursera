# Conditional Statements Part 1.

# Conditional Steps
x = 5
if x < 10:
    print('It is smaller!')
if x > 20:
    print('It is larger!')

print('Finish!')

# Comparison Operators
x = 5
if x == 5 :
    print('Eguals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 :
    print('Less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')

# One-Way Decisions
x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

# Thin about begin/end blocks
x = 5
if x > 2 :
    print('x is greater than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2 :
        print('i is greater than 2')
    print('Done with i', i)
print('All Done')

# Two-way Decisions
x = 4
if x > 2 :
    print('Bigger')
if x < 2 :
    print('Smaller')
print('All Done')

# Conditional Statements Part 2

# Multi-way
x = 8
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else :
    print('large')
print('Done')

# Multi-way Puzzles
x = 1
if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else :
    print('Something else')

x = 15
if x < 2 :
    print('Below 2')
elif x < 20 :
    print('Below 20')
elif x < 10 :
    print('Below 10')
else :
    print('Something else')

# Conditional Statements Part 3
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

# Sample try /except
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

fhand = open('mbox.txt', 'r') # Opening a file, if you try to open a file that is not there you will get back a traceback.
print(fhand, '\n') # Prints a name of file, mode and encoding.

print(open('mbox.txt').read()) # Open and read the file.

# The newline Character

stuff ='Hello\nWorld!'
print(stuff)

stuff = 'X\nY'
print(stuff)

print(len(stuff))

# File Handle as a Sequence
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

# Counting Lines in a File
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

# Reading the *Whole* File
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

# Searching Through a File
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From '):
        print(line)

# Searching Through a File (fixed)
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Remove new lines.
    if line.startswith('From '):
        print(line)

# Skipping with Continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Remove new lines.
    if line.startswith('From '):
        continue
    print(line)

# Using in to Select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # Remove new lines.
    if not '@uct.ac.za' in line:
        continue
    print(line)

# Prompt for File Name
fname = input('Enter file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Bad File Names
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
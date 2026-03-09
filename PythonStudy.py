# First code from Python PlayGround at Coursera

# This code is opening the file "rome.txt" in read mode "r".
fh = open("rome.txt", "r")

# Creating a variable called count and assign 0 to it.
# This will keep track of how many lines are in the file.
count = 0
# Loop through each line in the file.
for line in fh:
    # Print the line after removing extra whitespace
    # such as newline characters at the end.
    print(line.strip())
    # Increase the count by 1 for each line read.
    count = count + 1
# After the loop finishes, print the total number of lines.
print(count,"Lines")
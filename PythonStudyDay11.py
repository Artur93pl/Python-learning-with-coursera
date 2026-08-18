num = 0        # counts how many valid numbers have been entered
tot = 0.0      # running total (float) of all valid numbers entered

while True:
    sval = input("Enter a number: ")   # always read input as a string first

    if sval == 'done':                 # sentinel value to stop the loop
        break

    try:
        fval = float(sval)             # try converting the string to a float
    except:
        print("Invalid Input")         # runs if float() fails (e.g. "bob")
        continue                       # skip the rest of this loop and ask again

    # print(fval)                      # (debug) show the converted value

    num = num + 1                      # only reached for valid numbers, so increment count
    tot = tot + fval                   # add this number to the running total

# print('ALL DONE')                    # (debug) confirms the loop has ended

print(tot, num, tot / num)             # print total, count, and the average (total / count)
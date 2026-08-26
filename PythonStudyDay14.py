# Exercise with coursera video to get 0.8475 from string str.

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
piece = str[ipos+2:]
print(piece)
# print(piece+42.0) # Will give traceback error
value = float(piece)
print(value)
# String : 
# s = ' ' , " " , """ """
# 1. String are immutable
# 2. Strings is ordered data structures - indexing and slicing

# s = "Python sample string"
# print(type(s))

# s1 = "Python"
# print(id(s1))

# s1 = "Java"
# print(id(s1))

# INDEXING
s = "Python sample string"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[-1])
# print(s[100])

# SLICING
# print(s[0:6])
# print(s[7:])
# print(s[:6])

# STRIDE
# print(s[::2])
# print(s[::-1])

for value in s[::2]:
    print(value)

# help(str)
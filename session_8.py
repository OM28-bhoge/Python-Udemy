# break
# continue
# enumerated

# for value in range(10):
#     print(value)

l = [10,20,30,40,50,60]
key = 300

# for index,value in enumerate(l):
#     # print(index, value)
#     if value == key:
#         print("Element Found at index" , index)
#         break
#     else:
#         continue
#         print("statement after continue statement")
# else:
#     print("Element Not Found")

# print("Statemnt after the for loop")

for index,value in enumerate(l):
    # print(index, value)
    if value == key:
        print("Element Found at index" , index)
        break
    else:
        pass
        # print("statement after continue statement")
else:
    print("Element Not Found")

# for value in l:

# else
# break
# continue
# pass
# enumerate
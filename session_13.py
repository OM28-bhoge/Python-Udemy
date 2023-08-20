# list

# 1 Lists are mutable - add update and delete
# 2 ordered indexing and slicing
# 3 heterogeneous datatypes
# l = [10,20,30,40 , "Python" , "Java",[100,200,300]]
# print(l)
# print(l,type(l))

# indexing and slicing:
# print(l[-1][1])
# print(l[20])
# print(l[1:3])
# print(l[::-1])

l = [100,200,300,400,500]

# for value in l[::2]:
#     print(value) 

# append
# num1 = 100
# print(id(num1))
# print(id(l))
# l.append(600)
# print(id(0))
# print(l)

# extend

# l.extend([500,600,700,800])
# print(l)

# l.append([500,600,700,800])
# print(l)

# l.extend("Python")
# print(l)

# insert

# l.insert(1,1000)
# print(l)

l = [10 , 20 , 30]
# l2=l
l2 = l.copy()
l.append(40)
print(id(l),id(l2))
print(l,l2)
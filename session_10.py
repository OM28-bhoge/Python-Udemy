# Q1 ) Write a python program to find those numbers which are divisible by 7 and 5 ,  between 1500 and 2700 (both included)
# ANS -
# for num in range(1500 , 2701):
#     if num % 7 == 0 and num % 5 == 0:
#         print(num)
        
# Q2 ) Write a python program to count the number of even and odd numbers from  a series of numbers.
# Sample numbers :
#     numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected output :
#     Even numbers : 5
#     Odd numbers : 4
# ANS :- 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)

# Q3) Write a Python program which iterates the integers from 1 to 50. For Multiples of three print "Buzz" . For Numbers which are multiples of both three and five print "FizzBuzz"
# ANS : - 

# for num in range(1 , 50) :
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# Q4) write a python program to calculate the sum and average of n integer numbers
# ANS : -

# n = int(input("Ente the number of integers: "))

# sum_of_numbers = 0
# average = 0

# for i in range(n):
#     number = int(input("Enter the number: "))
#     sum_of_numbers += number
# if n != 0:
#     average = sum_of_numbers / n

# print("Sum of the numbers: ", sum_of_numbers)

# print("Average of the numbers: ", average)

# Q5)Factorial of any number n is represented by n! and is equal to
# 1*2*3*...* (n-1)*n.
# E.g.-
# 4!=1"2"3°4=24
# 3! = 3*2*1=6
# 2! = 2*1=2
# Also,
# 1! = 1
# O! = 1
# Write a program to calculate factorial of a number.
# ANS : -
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input("Enter the number: "))

# print(factorial(n))

    
# 1. Write a function to add two numbers.
# def add(a,b) :
#     return a+b
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print(add(x,y))
import math


#-------------------------------------------------------------------------#

# 2. Write a function to subtract two numbers.
# def subtract(a , b) :
#     if a > b :
#         return  a-b
#     else :
#         return b-a
#
# print(subtract(int(input("Enter a : ")), int(input("Enter b : "))))

#-------------------------------------------------------------------------#

# 3. Write a function to multiply two numbers.
# def multiply(a, b) :
#     return  a*b
#
# print(multiply(int(input("Enter a : ")),int(input("Enter b : "))))


#-------------------------------------------------------------------------#

# 4. Write a function to divide two numbers safely.
# def div(a , b) :
#     if b != 0 :
#         return a/b
#     else:
#         return  0
#
# print(div(int(input("Enter a : ")),int(input("Enter b : "))))
#-------------------------------------------------------------------------#

# 5. Write a function to find the maximum of two numbers.
# def maxInTwo(a , b ) :
#     if a > b :
#         return a
#     else :
#         return  b
# print(maxInTwo(10,49))

#-------------------------------------------------------------------------#

# 6. Write a function to find the minimum of two numbers.
# def min (a , b) :
#     if a < b :
#         return a
#     else:
#         return  b
#
# print(min(14,12))

#--------------------------------------------------------------------------------------#

# 7. Write a function to check whether a number is even or odd.
# def evenOdd(num) :
#     if num%2==0 :
#         return "Even"
#     return "Odd"
#
# print(evenOdd(15))

#--------------------------------------------------------------------------------------#

# 8. Write a function to check whether a number is prime.
# def primeOrNot(num) :
#     for i in range(2, math.isqrt(num)+1,1):
#         if num % i == 0 :
#             return "Not Prime"
#     return "Prime"
#
# while(True) :
#     val = int(input("Enter value : "))
#     if val == 0 :
#         break
#     print(primeOrNot(val))

#--------------------------------------------------------------------------------------#

# 9. Write a function to calculate the factorial of a number.
# def fact(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i
#     return  fact
# val = int(input("Enter Val : "))
# print(fact(val))

#--------------------------------------------------------------------------------------#

# 10. Write a function to generate the Fibonacci series up to N terms.

# def fibo(n) :
#     first = 0
#     second = 1
#     for i in range(0,n-2):
#         print(first)
#         temp = second
#         second = first+second
#         first = temp
# fibo(int(input("Enter Seq : ")))

#--------------------------------------------------------------------------------------#

# 11. Write a function to check whether a number is a palindrome.

# def checkPalindrome(num):
#     n = num
#     rev = 0
#     while n > 0 :
#         rev = (rev * 10 ) + (n % 10)
#         n = n//10
#     print(num == rev)
#
# checkPalindrome(int(input("Enter Num : ")))

#--------------------------------------------------------------------------------------#

# 12. Write a function to calculate the sum of digits of a number.

# def sumofdigit(val):
#     total = 0
#     while val > 0 :
#         total = total + val % 10
#         val = val // 10
#     print(total)
#
# sumofdigit(int(input("Enter value   : ")))

#------------------------------------------------------------------------------------#

# 13. Write a function to reverse the digits of a number.

# def rev(num) :
#     sec_num = 0
#     while num > 0 :
#         sec_num = sec_num * 10 + num % 10
#         num = num // 10
#     print(sec_num)
#
# num = int(input("Enter num : "))
# rev(num)


#--------------------------------------------------------------------------------------#

# 14. Write a function to calculate the average of a list of numbers.

# def calculateAvg():
#     final_num = 0
#     counter = -1
#     while True:
#         num = int(input("Enter val : "))
#         counter+=1
#         if num < 0 :
#             break
#         final_num = (final_num + num)
#     print("Average is : " , final_num/counter)
# calculateAvg()

#--------------------------------------------------------------------------------------#

# 15. Write a function to calculate the area of different shapes.
# def shapeArea():
#     choose = int(input("Enter 1 for square , 2 for circle , 3 for triangle : "))
#     if choose == 1 :
#         side = int(input("Enter sides : "))
#         return side * side
#     elif choose == 2 :
#         r = int(input("Enter Radius : "))
#         return  int(math.pi*math.pow(r,2))
#     elif choose == 3 :
#         h = int(input("Enter height : "))
#         b = int(input("Enter base : "))
#         return  0.5 * b * h
#     else:
#         return "Not a valid option "
#
# print(shapeArea())

#--------------------------------------------------------------------------------------#

# 16. Write a program to build a simple calculator using functions.

# def cal () :
#     operator = int(input("Enter 1 for add , Enter 2 for sub , Enter 3 for mul , Enter 4 for div : "))
#     if operator == 1 :
#         a = int(input("Enter  a : "))
#         b = int (input("Enter b : "))
#         return  a + b
#     elif operator == 2 :
#         a = int(input("Enter  a : "))
#         b = int(input("Enter b : "))
#         return math.ceil(a - b)
#
#     elif operator == 3 :
#         a = int(input("Enter  a : "))
#         b = int(input("Enter b : "))
#         return a * b
#     elif operator == 4 :
#         a = int(input("Enter  a : "))
#         b = int(input("Enter b : "))
#         return a // b
#     else :
#         return "Invalid Option"
# print(cal())

#--------------------------------------------------------------------------------------#

# 17. Write a function to calculate the power of a number.
# def power(num , num2) :
#     val = 1
#     for i in range(1 , num2+1, 1):
#         val = val * num
#     return  val
#
# print(power(int(input("Enter Number : ")), int(input("Enter Power : "))))

#--------------------------------------------------------------------------------------#

# 18. Write a function to convert Celsius to Fahrenheit.
# def f_to_c (c):
#     return (c*9)/5 + 32
# print(f_to_c(25))


#--------------------------------------------------------------------------------------#

# 19. Write a function to convert Fahrenheit to Celsius.
# def celsisuToFahrenit(f):
#     return (f - 32 ) * 5 / 9
#
# print(celsisuToFahrenit(200))

#--------------------------------------------------------------------------------------#

# 20. Write a function to calculate simple interest.
def simple_interest(p,r,t):
    return  (p*r*t)/100

print(simple_interest(1000,10))



#--------------------------------------------------------------------------------------#

# # Even or Odd
# num = int(input("Enter val :"))
# if num%2==0:
#     print("Even")
# else :
#     print("Odd")

#-------------------------------------------------#

# Positive, Negative, or Zero
# val = int(input("Enter any num : "))
# if val>0:
#     print("Positive")
# elif val < 0 :
#     print("Negative")
# else:
#     print("Zero")

#-------------------------------------------------#

# Largest of Two Numbers
# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# if num1>num2:
#     print("Num 1 is greater")
# elif num2>num1 :
#     print("Num 2 is Greater")
# else :
#     print("Both is = ")

#-------------------------------------------------#

# Largest of Three Numbers
# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# num3 = int(input("Num3 : "))
# if num1 > num2:
#     if num1 > num3:
#         print("Num 1")
#     elif num3 > num2 :
#         print("Num 3")
# else :
#     if num2 > num3:
#         print("Num 2")
#     else :
#         print("Num 3")

#-------------------------------------------------#

# Smallest of Three Numbers
# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# num3 = int(input("Num3 : "))
#
# if num1 > num2 :
#     if num3 > num2:
#         print("Num 2")
#     elif num1 > num3:
#         print("Num 3")
# else:
#     if num3 > num1:
#         print("Num 1")
#     else :
#         print("Num 3")

#-------------------------------------------------#

# Leap Year
# year = int(input("Enter Year : "))
# if year%100==0:
#     if year%400 ==0:
#         print("Leap Year")
#     else :
#         print("Not a leap year")
#
# elif year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#-------------------------------------------------#

# Eligible for Voting
# age = int(input("Enter age : "))
# if age >= 18 :
#     print("Can Vote")
# else :
#     print("Can't vote")

#-------------------------------------------------#

# Pass or Fail
# marks = int(input("Enter Marks : "))
# if marks > 33 :
#     print("pass")
# else :
#     print("Fail")

#-------------------------------------------------#

# Grade Calculator
# percentage = int(input("Enter % : "))
# grade= ""
# if 60 <= percentage < 75:
#     grade="C"
# elif 75 <= percentage < 90:
#     grade = "B"
# elif 90 <= percentage <= 100 :
#     grade = "A"
# else :
#     grade = "D"
# print("Grade is : ",grade)
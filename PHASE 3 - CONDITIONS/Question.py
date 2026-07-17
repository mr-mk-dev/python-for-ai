# 1. Write a program to check whether a number is even or odd.

# num = int(input("Enter val :"))
# if num%2==0:
#     print("Even")
# else :
#     print("Odd")

#-------------------------------------------------#

# 2. Write a program to check whether a number is positive, negative, or zero.

# val = int(input("Enter any num : "))
# if val>0:
#     print("Positive")
# elif val < 0 :
#     print("Negative")
# else:
#     print("Zero")

#-------------------------------------------------#

# 3. Write a program to find the largest of two numbers.

# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# if num1>num2:
#     print("Num 1 is greater")
# elif num2>num1 :
#     print("Num 2 is Greater")
# else :
#     print("Both is = ")

#-------------------------------------------------#

# 4. Write a program to find the largest of three numbers.

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# num3 = int(input("Num3: "))
#
# if num1 >= num2 and num1 >= num3:
#     print("Num1 is the largest")
# elif num2 >= num1 and num2 >= num3:
#     print("Num2 is the largest")
# else:
#     print("Num3 is the largest")

#-------------------------------------------------#

# 5. Write a program to find the smallest of three numbers.

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# num3 = int(input("Num3: "))
#
# if num1 >= num2 and num1 >= num3:
#     print("Num1 is the largest")
# elif num2 >= num1 and num2 >= num3:
#     print("Num2 is the largest")
# else:
#     print("Num3 is the largest")

#-------------------------------------------------#

# 6. Write a program to check whether a given year is a leap year.

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

# 7. Write a program to check whether a person is eligible to vote.

# age = int(input("Enter age : "))
# if age >= 18 :
#     print("Can Vote")
# else :
#     print("Can't vote")

#-------------------------------------------------#

# 8. Write a program to check whether a student has passed or failed based on marks.

# marks = int(input("Enter Marks: "))
#
# if marks >= 33:
#     print("Pass")
# else:
#     print("Fail")

#-------------------------------------------------#

# 9. Write a program to calculate a student's grade based on marks.

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

#-------------------------------------------------#

# 10. Write a program to check whether a number is both positive and even.

# num = int(input("Enter Num : "))
# if num>0 and num%2==0:
#     print("Positive and even")
# else:
#     print("Not Sure")

#-------------------------------------------------#

# 11. Write a program to validate a person's age within an acceptable range.

# age = int(input("Enter Age: "))

# if 18 <= age <= 60:
#     print("Valid Age")
# else:
#     print("Invalid Age")

#-------------------------------------------------#

# 12. Write a program to check whether a given day is a weekend.

# day = input("Enter Day :")
# if day == "Sunday" or day == "Saturday" :
#     print("Weekend")
# else :
#     print("Not a weekend")

#-------------------------------------------------#

# 13. Write a program to check login access using a username and password.


# username = "Manish"
# password = "Pass"
# login_id = input("Enter username : ")
# login_pass = input("Enter Password : ")
# if login_id == username and login_pass == password :
#     print("Login successes")
# else:
#     print("Invalid Userid or password")

#-------------------------------------------------#

# 14. Write a program to find the largest of three numbers using the and operator

# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))

# if a >= b and a >= c:
#     print("A is greatest")
# elif b >= a and b >= c:
#     print("B is greatest")
# else:
#     print("C is greatest")

#-------------------------------------------------#

# 15. Write a program to check whether three given sides form a valid triangle

# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
#
# if a >= b and a >= c:
#     print("A is greatest")
# elif b >= a and b >= c:
#     print("B is greatest")
# else:
#     print("C is greatest")

#-------------------------------------------------#

# 16. Write a program to check discount eligibility based on purchase amount.
# amount = float(input("Enter Purchase Amount: "))
# is_member = input("Member (yes/no): ")
#
# if amount >= 5000 or is_member.lower() == "yes":
#     print("Discount Applied")
# else:
#     print("No Discount")

#-------------------------------------------------#

# 17. Write a program to check whether a password meets security conditions.

# password = input("Enter Password : ")
#
# if len(password) >= 8 :
#     print("Strong Pass")
# else :
#     print("Not a strong pass")

#-------------------------------------------------#

# 18. Write a program to validate marks entered are within an allowed range.
# marks = int(input("Enter Marks : "))
# if 0 <= marks <= 100 :
#     print("Valid Marks : ",marks)
# else :
#     print("Invalid Marks")

#-------------------------------------------------#

# 19. Write a program to check admission eligibility based on marks and age.
# age = int(input("Enter Age: "))
# marks = int(input("Enter Marks: "))
#
# if age >= 18 and marks >= 60:
#     print("Admission Approved")
# else:
#     print("Admission Rejected")


#-------------------------------------------------#

# 20. Write a program to categorize BMI into underweight, normal, or overweight

# weight = float(input("Enter weight (kg): "))
# height = float(input("Enter height (m): "))
#
# bmi = weight / (height ** 2)
#
# print("BMI:", round(bmi, 2))
#
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# else:
#     print("Overweight")

#-------------------------------------------------#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on :- 06-Apr-2020
Name of Course:- Python BootCamp
Name of File:- Answers of exercise
Name of Autho:- SAmir Mastekar
"""
import os
print("Hello, welcome to Python Exercise")
#----------------------------------------------------------------------
'''
Question 1
Can you write a short program that will print out the version of Python
that you are using?
'''
print(os.system("Python --version"))

#----------------------------------------------------------------------
'''
Question 2
Write a program that requests five names separated by commas and create a
list containing those names. Print your answer.
For example James,Alison,Fred,Sally,Matthew
should return ['James','Alison','Fred','Sally','Matthew']
'''
# nameList = []
# user_inputloop = "yes"
# while(user_inputloop == "yes"):
	# user_input = input('Please enter user name')
	# nameList.append(user_input)
	# user_inputloop=input('Do you want to Continue(Enter \'yes\')>>').lower()
# print(nameList)

#----------------------------------------------------------------------
'''
Question 3
Write a program to determine whether a given number is within 10 of 100 or 200.
'''
# userInput =int(input("Enter the number>> "))
# if(userInput <10):
	# print("The given number is below the 10")
# elif(userInput >= 10 and userInput<= 100):
	# print(f'The given {userInput} is within 10 and 100')
# elif(userInput >= 100 and userInput<= 200):
	# print(f'The given {userInput} is within 100 and 200')
# else:
	# print("Out of range")

#-----------------------------------------------------------------------
'''
Question 4
Write a program that takes a list of non-negative integers and prints 
each integer to the screen the same number of times as the value of the 
integer, each new value on a new line. For example
[2,3,4,1] would print:
22
333
4444
1
'''
# userInput = int(input("Please enter non-negative number:- "))
# numberString = str(userInput)
# print(numberString*userInput)

#-----------------------------------------------------------------------
'''
Question 5
Write some code that will return the number of CPUs in the system.
'''
print("Number of CPU:- " + str(os.cpu_count()))

#-----------------------------------------------------------------------
'''
Question 6
Write a program that will return the sum of the digits of an integer.
'''
# userInput = int(input("enter the number:- "))
# sum =0
# while(userInput != 0):
	# sum = userInput%10 + sum
	# userInput = userInput//10
# print(f'Sum of digit is {sum}')

#-----------------------------------------------------------------------
'''
uestion 7
Write a program that converts text into pig latin. Pig latin works as follows:
All letters before initial vowel are placed at the end of the word 
and then 'ay' is added (explanation adapted from Wikipedia), so pig
 becomes igpay, cat becomes atcay, potential becomes otentialpay etc.
'''
# userInput = input("enter the tex:- ").lower()
# output1 = ''
# output2=''
# for char in userInput:
	# if(char == 'a' or char == 'e' or  char == 'i' or char=='o' or char=='u'):
		# output2=char+output1
		# print(output2)
	# else:
		# output1 = output2 + char
		# print(output1)
# print(output2 +'ay')

#------------------------------------------------------------------------
'''
Question 8
Write a function that will check for the occurrence of double letters in
a string. If the string contains double letters next to each other it
will return True, otherwise it will return False.
'''
# usreInput = input("enter the string:-")

# def My_function(userInput):
	# preChar=''
	# for char in userInput:
		# if(preChar == char):
			# return bool(True)
		# preChar = char
		# return False

# print(My_function(usreInput))

#--------------------------------------------------------------------------
'''
Question 9
Write a function that will check if a string is a palindrome.
'''
#userInput = input("enter the string:- ")

# def palidrome(inputString):
	# returnString = ''.join(reversed(inputString))
	# return returnString

# if(userInput == palidrome(userInput)):
	# print("yes")
# else:
	# print("No, Sorry")

#--------------------------------------------------------------------------
'''
Question 10
Write a function def add_commas(numbers) that will add commas to an integer 
and return it as a string. For example add_commas(1000000) will return 1,000,000 
Do it first without using string fomratting or f strings.
'''

#--------------------------------------------------------------------------
'''
Question 11
Write a function that will convert an integer into binary.
'''
# userInput = int(input("Enter the number:- "))
# print(f'Binary is :- {bin(userInput)}')

#--------------------------------------------------------------------------
'''
Question 12
Write a function that calculates the sum of all integers up to n. 
Use the iterative method and the formula and compare the results. 
(sum of n integers given by S = (n(n+1))/2)
'''
# userInput = int(input("Enter the number:-"))

# def byInterativeMethod(num):
	# sum = 0
	# for i in range(1,num+1):
		# sum = sum + i
	# return sum
# print(f'Sum  of all integer {byInterativeMethod(userInput)}')
# print("**********************By Formula**********************")
# def byFormulaMethod2(num):
	# S = num*(num+1)/2
	# print(S)
# byFormulaMethod2(userInput)

#----------------------------------------------------------------------------
'''
Question 15
Write a function that takes a positive integer n and converts it into hours and minutes.
45 would return 0h:45mins 135 would return 2h:15mins
'''
# userInput = int(input("Enter the number:- "))
# if(userInput<60):
	# print(f'oh::{userInput}mins')
# else:
	# hour=userInput//60
	# reminder= userInput%60
	# print(f'{hour}h :: {reminder}mins')

#---------------------------------------------------------------------------
'''
Question 16
Write a function to determine whether all numbers in a list are unique.
'''
# myList = [1, 4, 5, 4, 8, 8, 9, 10]
# def detUniqueNumber(List):
	# newList = []
	# for item in List:
		# if item not in newList:
			# newList.append(item)
	# return newList

# uniqueList = detUniqueNumber(myList)
# print(f'Original List:- {myList}')
# print(f'Modified List:- {uniqueList}')

#----------------------------------------------------------------------------
'''
Question 17
Write a function to add two positive integers together without using the + operator.
'''
# def add_with_plus_operatot(a, b):
	# while(b != 0):
		# data = a & b
		# print(data)
		# a=a ^ b 
		# print(a)
		# b = data<<1
		# print(b)
		# return a

# print(add_with_plus_operatot(10, 4))

#--------------------------------------------------------------------------
'''
Question 20
Write a function which prints the prime numbers in a given range.
'''
userRange = int(input("Enter the range:- "))
for val in range(1, userRange+1):
	if(val>1):
		for num in range(2, val):
			if((val%num)==0):
				break
		else:
			print(val)
				














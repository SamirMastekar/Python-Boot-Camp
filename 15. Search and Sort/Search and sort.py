"""
Name of Course:- Python Boot Camp
Name Author:- Samir Mastekar
Name of file:-Search And Sort
"""

#Linear Search
def linear_search(item, my_list):
    i = 0 
    found = False
    while i < len(my_list) and found == False:
        if my_list[i] == item:
            found = True
        else:
            i = i + 1
    return found

test = [6,5,8,2,3,45,87,24,70]
print(linear_search(87,test))
print(linear_search(88,test))

#Binary Search
def binary_search(item, my_list):
    found = False
    first = 0
    last = len(my_list) - 1
    
    while first <= last and found == False:
        midpoint = (first + last)//2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

test = [6,5,8,2,3,45,87,24,70]
print(linear_search(87,test))
print(linear_search(88,test))

#Bubble Search
def bubble_sort(my_list):
    swap_again = True
    n = len(my_list)
    while n > 0 and swap_again == True:
        n = n - 1
        swap_again == False
        
        for i in range(n):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swap_again = True
    return my_list
	
test_2 = [70,24,87,45,6,3,2,8,5]
print(bubble_sort(test_2))

#Insertion Sort
def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        value = my_list[i]
        j = i
        while j > 0 and my_list[j-1] > value:
            my_list[j] = my_list[j-1]
            j = j - 1
        my_list[j] = value
    return my_list

test_2 = [70,24,87,45,6,3,2,8,5]
print(bubble_sort(test_2))
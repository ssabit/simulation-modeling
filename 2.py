# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wiSHIm7TACtDfHG9t0lF9gXmqoM4X-GI
"""

number_list = input("Enter number with comma: ")
#print(number_list)
#print(type(number_list))
li = list(number_list.split(","))
remove_duplicates=list(set(li))

remove_duplicates=list(map(int,remove_duplicates))

#print(type(remove_duplicates))
remove_duplicates.sort()
print("Number of unique items-",remove_duplicates)
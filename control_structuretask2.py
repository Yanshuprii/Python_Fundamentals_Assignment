# -*- coding: utf-8 -*-
"""Control_structuretask2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TgYNENX76YVq-o8Tfs_jGli6mHoaHxnX
"""

# Programming with control structures
def classify_number():
  num=int(input("enter a number to classify: ")) #asking input from the user
  if num>0:
    print("positive")
  elif num<0:
    print("negative")
  else:
    print("zero")

a=input("enter 'exit' to exit: ") #to store something in 'a' before running the loop
while a!="exit":
  classify_number() #calling the function
  a=input("enter 'exit' to exit") #here written twice because we need to show this statement in loop until user enters exit
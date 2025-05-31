"""
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""

file=open('sample.txt','r')
try: 
    f1=file.read()
    print(f1)
    file.close()
except  Exception:
    print("Error: The file 'sample.txt' was not found.")

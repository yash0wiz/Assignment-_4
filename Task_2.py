"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 
"""

file=open('output.txt','w')
print("Enter text to write to the file: ")
in_put=input()
f1=file.write(in_put)
print("Data successfully written to output.txt.")

file=open('output.txt','a')
print("Enter additional text to append: ")
in_put1=input("\n")
f1=file.write(in_put1)
print("Data successfully appended.\n")

file=open('output.txt','r')
print("Final content of output.txt:")
f1=file.read()
print(f1)
file.close()


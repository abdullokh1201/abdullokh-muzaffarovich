Python Exception Handling: Exercises, Solutions, and Practice
Exception Handling Exercises
#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def safe_division(a, b):
    try
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero!")

num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

safe_division(num1, num2)



#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def get_integer_input():
    try:
        user_input = input("Please enter an integer: ")
        number = int(user_input)
        print("You entered:", number)
    except ValueError:
        print("ValueError: The input is not a valid integer. Please enter an integer.")

get_integer_input()

#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def open_file_with_handling(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError as e:
        print("FileNotFoundError caught:", e)
        print("The file does not exist. Please check the file name and try again.")

file_name = input("Enter the filename to open: ")
open_file_with_handling(file_name)

#4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def get_numbers_and_add():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2
        print("The sum of", num1, "and", num2, "is", result)
    
    except ValueError:
        print("ValueError: Both inputs must be numerical values.")
    except TypeError:
        print("TypeError: Invalid type of input provided.")

get_numbers_and_add()

#5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def open_file_with_permission_handling(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except PermissionError as e:
        print("PermissionError caught:", e)
        print("You don't have the necessary permissions to read this file.")
    except FileNotFoundError as e:
        print("FileNotFoundError caught:", e)
        print("The file does not exist.")

# Example usage
file_name = input("Enter the filename to open: ")
open_file_with_permission_handling(file_name)

#6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def access_list_element():
    my_list = [10, 20, 30, 40, 50]
    
    try:
        index = int(input("Enter an index to access (0–4): "))
        print("Element at index", index, "is", my_list[index])
    except IndexError as e:
        print("IndexError caught:", e)
        print("The index you entered is out of range.")
    except ValueError:
        print("Invalid input! Please enter an integer index.")

access_list_element()

#7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
def get_user_input():
    try:
        number = float(input("Please enter a number: "))
        print("You entered:", number)
    except KeyboardInterrupt:
        print("\nInput cancelled by user (KeyboardInterrupt).")

get_user_input()

#8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def safe_division(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ArithmeticError as e:
        print("ArithmeticError caught:", e)
        print("An arithmetic error occurred during the division.")

num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))
safe_division(num1, num2)

#9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
def read_file_with_handling(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n", content)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError caught:", e)
        print("There was an issue decoding the file. Try using a different encoding (e.g., 'latin-1').")

file_name = input("Enter the filename to open: ")
read_file_with_handling(file_name)

#10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
def list_operation():
    my_list = [1, 2, 3, 4, 5]
    
    try:
        my_list.push(6)
    except AttributeError as e:
        print("AttributeError caught:", e)
        print("It seems you're trying to use a method that doesn't exist for lists. Try using 'append' instead.")

list_operation()



Python File Input Output: Exercises, Practice, Solution
File Input/Output Exercises
#1.Write a Python program to read an entire text file.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


#2.Write a Python program to read first n lines of a file.
n = int(input("Enter number of lines: "))
with open("example.txt", "r") as file:
    for _ in range(n):
        print(file.readline(), end="")

#3.Write a Python program to append text to a file and display the text.
with open("example.txt", "a") as file:
    file.write("\nThis is the new appended line.")

with open("example.txt", "r") as file:
    print(file.read())

#4.Write a Python program to read last n lines of a file.
n = int(input("Enter number of lines from end: "))
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end="")

#5.Write a Python program to read a file line by line and store it into a list.
with open("example.txt", "r") as file:
    lines = file.readlines()
print(lines)

#6.Write a Python program to read a file line by line and store it into a variable.
with open("example.txt", "r") as file:
    array = [line.strip() for line in file]
print(array)

#7.Write a Python program to read a file line by line and store it into an array.
with open("example.txt", "r") as file:
    words = file.read().split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
print(longest_words)

#8.Write a Python program to find the longest words.
with open("example.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Number of lines:", line_count)

#9.Write a Python program to count the number of lines in a text file.
from collections import Counter

with open("example.txt", "r") as file:
    words = file.read().split()
    frequency = Counter(words)
print(frequency)

#10.Write a Python program to count the frequency of words in a file.
import os

file_size = os.path.getsize("example.txt")
print("File size in bytes:", file_size)

#11.Write a Python program to get the file size of a plain file.
lines = ["First line", "Second line", "Third line"]
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

#12.Write a Python program to write a list to a file.
with open("example.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

#13.Write a Python program to copy the contents of a file to another file.
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

#14.Write a Python program to combine each line from the first file with the corresponding line in the second file.
import random

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(random.choice(lines))

#15.Write a Python program to read a random line from a file.
file = open("example.txt", "r")
print("Is file closed?", file.closed)
file.close()
print("Is file closed now?", file.closed)

#16.Write a Python program to assess if a file is closed or not.
with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)

#17.Write a Python program to remove newline characters from a file.
import re

with open("example.txt", "r") as file:
    text = file.read()
    words = re.split(r'[,\s]+', text.strip())
    print("Total words:", len(words))

#18.Write a Python program that takes a text file as input and returns the number of words in a given text file.


Note: Some words can be separated by a comma with no space.
import glob

char_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as file:
        char_list.extend(list(file.read()))
print(char_list)

#19.Write a Python program to extract characters from various text files and put them into a list.
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")

#20.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string

letters_per_line = 5
with open("alphabet.txt", "w") as file:
    alphabet = string.ascii_uppercase
    for i in range(0, len(alphabet), letters_per_line):
        file.write("".join(alphabet[i:i+letters_per_line]) + "\n")

#21.Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

def write_alphabet_to_file(letters_per_line, filename="alphabet.txt"):
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    
    with open(filename, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i + letters_per_line]
            file.write(line + '\n')
    
    print(f"Alphabet written to '{filename}' with {letters_per_line} letters per line.")
letters_per_line = int(input("Enter number of letters per line: "))
write_alphabet_to_file(letters_per_line)


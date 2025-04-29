#1. Create your own virtual environment and install some python packages.

Creating Virtual environment
python -m venv myvenv

To activate myvenv
myvenv/Scripts/activate or activate.bat

To deactivate
deactivate

#2. Create custom modules.
Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def reverse_string(string):
    return string[::-1]

def count_vowels(string):
    c = 0
    for s in string:
        if s.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            c += 1
    return c

#3. Create custom packages.
Create geometry package.
 geometry\
     __init__.py
     circle.py
 
Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
Create file_operations package.
 file_operations\
     __init__.py
     file_reader.py
     file_writer.py
 
Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).

import math
def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius



def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)



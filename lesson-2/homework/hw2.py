#1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
                             
from datetime import datetime

name = input("Enter your name: ")

year_of_birth = int(input("Enter your year of birth: "))

current_year = datetime.now().year

age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")

#2Extract Car Names
Extract car names from the following text: 

text = 'LMaasleitbtui'

 malibu = ''

 lasetti = ''

 malibu += text[1] + text[3] + text[5] + text[7] + text[9] +text[11]

lasetti += text[0] + text[2] + text[4] +text[6] + text[8] + text[10] + text[12]

print(malibu)

print(lasetti)



#3 Extract Car Names
Extract car names from the following text:

txt = 'MsaatmiazD'
text = 'MsaatmiazD'

damas = ''

matiz = ''

damas += text[-1] + text[-3] + text[-5] + text[-7] + text[-9]

matiz += text[0] + text[2] + text[4] +text[6] + text[8]

print(damas)

print(matiz)

#4. Extract Residence Area
Extract the residence area from the following text:

txt = "I'am John. I am from London"

if "I am from" in txt:
 
  residence_area = txt.split("I am from")[1].strip()
   
  print("Residence Area:", residence_area)

#5 Reverse String
Write a Python program that takes a user input string and prints it in reverse order.

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print(reversed_string)

#6 Count Vowels
Write a Python program that counts the number of vowels in a given string.

ef count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
         count += 1
    return count

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print(vowel_count)
#7 Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.

def find_max_value(numbers):
    return max(numbers)

user_input = input("Enter a list of numbers separated by spaces: ")
number_list = [float(num) for num in user_input.split()]
max_value = find_max_value(number_list)
print( max_value)

#8 Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

def check_palindrome(word):

    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False


user_input = input("Enter a word: ")
if check_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")

    print(f"'{user_input}' is not a palindrome.")

#9 Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.

def extract_domain(email):

    parts = email.split('@')


    if len(parts) == 2:
        return parts[1]
    else:
        return "Invalid email address"


user_email = input("Enter your email address: ")
domain = extract_domain(user_email)
print(domain)

#10  Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.

  def generate_random_password(length):

    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits  # 0-9
    special_characters = string.punctuation  # Special characters like !, @, #

    all_characters = letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


password_length = int(input("Enter the length of the password: "))
password = generate_random_password(password_length)



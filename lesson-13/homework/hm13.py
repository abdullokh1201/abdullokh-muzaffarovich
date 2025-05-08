
#1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime, date

def calculate_age(birthdate):
    today = date.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        previous_month = today.month - 1 if today.month > 1 else 12
        previous_year = today.year if today.month > 1 else today.year - 1
        days += (date(previous_year, previous_month + 1, 1) - date(previous_year, previous_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    
    try:
        birthdate = datetime.strptime(birth_input, "%Y-%m-%d").date()
        years, months, days = calculate_age(birthdate)
        print(f"\nYou are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid input. Please enter the date in YYYY-MM-DD format.")

main()

#2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime, date

def days_until_birthday(birthdate):
    today = date.today()

    next_birthday = birthdate.replace(year=today.year)


    if next_birthday < today:
        next_birthday = birthdate.replace(year=today.year + 1)


    days_remaining = (next_birthday - today).days
    return days_remaining

def main():
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")

    try:
        birthdate = datetime.strptime(birth_input, "%Y-%m-%d").date()
        days_left = days_until_birthday(birthdate)

        if days_left == 0:
            print("\n🎉 Today is your birthday! Happy Birthday! 🎂")
        else:
            print(f"\n🎈 There are {days_left} day(s) left until your next birthday.")
    except ValueError:
        print("Invalid input. Please enter the date in YYYY-MM-DD format.")

main()

#3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

def schedule_meeting():
  
    current_input = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    
    try:
        current_dt = datetime.strptime(current_input, "%Y-%m-%d %H:%M")
        
    
        hours = int(input("Enter meeting duration - Hours: "))
        minutes = int(input("Enter meeting duration - Minutes: "))
        
        duration = timedelta(hours=hours, minutes=minutes)
        end_time = current_dt + duration
        
        print("\n🗓️ Meeting Start: ", current_dt.strftime("%Y-%m-%d %H:%M"))
        print("⏳ Duration     : ", f"{hours} hour(s) and {minutes} minute(s)")
        print("✅ Meeting Ends : ", end_time.strftime("%Y-%m-%d %H:%M"))

    except ValueError:
        print("❌ Invalid input. Please use the format YYYY-MM-DD HH:MM for date and time.")

schedule_meeting()

#4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

def convert_timezone():
   
    date_input = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    current_tz = input("Enter your current timezone (e.g., 'America/New_York'): ")
    target_tz = input("Enter the target timezone (e.g., 'Europe/London'): ")

    try:
        naive_datetime = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
        
        current_timezone = pytz.timezone(current_tz)
        
        localized_datetime = current_timezone.localize(naive_datetime)
        
        target_timezone = pytz.timezone(target_tz)
        converted_datetime = localized_datetime.astimezone(target_timezone)
        
        print(f"\nYour time in {current_tz}: {localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
        print(f"Converted time in {target_tz}: {converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
        
    except ValueError:
        print("Invalid input. Please ensure the date and time format is 'YYYY-MM-DD HH:MM'.")
    except pytz.UnknownTimeZoneError:
        print("Invalid timezone. Please enter a valid timezone (e.g., 'America/New_York').")

convert_timezone()
#sql

Enter the date and time (YYYY-MM-DD HH:MM): 2025-05-08 14:30
Enter your current timezone (e.g., 'America/New_York'): America/New_York
Enter the target timezone (e.g., 'Europe/London'): Europe/London

Your time in America/New_York: 2025-05-08 14:30:00 EDT-0400
Converted time in Europe/London: 2025-05-08 19:30:00 BST+0100

import pytz
print(pytz.all_timezones)

#5.Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

import time
from datetime import datetime

def countdown_timer():
    future_input = input("Enter the future date and time (YYYY-MM-DD HH:MM): ")
    
    try:
        future_time = datetime.strptime(future_input, "%Y-%m-%d %H:%M")
        
        while True:
            current_time = datetime.now()
            
            time_left = future_time - current_time
            
            if time_left.total_seconds() <= 0:
                print("⏰ The time has come! The countdown has ended.")
                break
            
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"\rTime remaining: {time_left.days} days, {hours:02}:{minutes:02}:{seconds:02}", end="")
            
            time.sleep(1)
    
    except ValueError:
        print("Invalid input. Please ensure the date and time format is 'YYYY-MM-DD HH:MM'.")

countdown_timer()

#6.Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email):
        return True
    else:
        return False

def main():
    email = input("Enter your email address: ")
    
    if validate_email(email):
        print("✅ The email address is valid.")
    else:
        print("❌ Invalid email address. Please enter a valid one.")

main()

#7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

import re

def format_phone_number(phone_number):
    digits = re.sub(r'\D', '', phone_number)
    
    if len(digits) == 13 and digits.startswith("998"):
        formatted_number = f"+998 ({digits[3:5]}) {digits[5:8]}-{digits[8:]}"
        return formatted_number
    else:
        return "❌ Invalid phone number. It must start with +998 and have 9 digits after the country code."

def main():
    phone_number = input("Enter an Uzbekistan phone number (e.g., +998 90 123 4567): ")
    
    formatted_number = format_phone_number(phone_number)
    
    print(f"Formatted Phone Number: {formatted_number}")

main()

#8Password Strength Checker: Implement a password strength checker.
Ask the user to input a password and check if it meets certain criteria
(e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = []
    if length_error:
        errors.append("❌ Password must be at least 8 characters long.")
    if uppercase_error:
        errors.append("❌ Password must contain at least one uppercase letter.")
    if lowercase_error:
        errors.append("❌ Password must contain at least one lowercase letter.")
    if digit_error:
        errors.append("❌ Password must contain at least one digit.")
    if special_char_error:
        errors.append("❌ Password should contain at least one special character (e.g., !, @, #, etc.).")

    if errors:
        print("\nPassword is ❌ **weak**. Please fix the following:")
        for error in errors:
            print(error)
    else:
        print("\n✅ Your password is strong!")

def main():
    password = input("Enter your password: ")
    check_password_strength(password)

main()


#9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text.
Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

def word_finder():
    sample_text = """
    In the middle of difficulty lies opportunity. The important thing is not to stop questioning.
    Look deep into nature, and then you will understand everything better. Try not to become a man of success,
    but rather try to become a man of value. The true sign of intelligence is not knowledge but imagination.
    """

    word = input("Enter a word to search for: ").strip()

    pattern = rf'\b{re.escape(word)}\b'
    matches = re.findall(pattern, sample_text, re.IGNORECASE)

    print(f"\n🔍 Searching for '{word}'...")
    if matches:
        print(f"✅ Found {len(matches)} occurrence(s):")
        highlighted_text = re.sub(pattern, lambda m: f"[{m.group(0)}]", sample_text, flags=re.IGNORECASE)
        print("\n" + highlighted_text)
    else:
        print("❌ No matches found.")

word_finder()


#10.Date Extractor: Write a program that extracts dates from a given text. 
Ask the user to input a text, and then identify and print all the dates present in the text.

import re

def extract_dates(text):
    date_patterns = [
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',            
        r'\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b',              
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4}\b', 
        r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?,?\s+\d{4}\b'  
    ]

    combined_pattern = "|".join(date_patterns)

    matches = re.findall(combined_pattern, text, flags=re.IGNORECASE)

    return matches

def main():
    print("📅 Date Extractor\n")
    user_input = input("Enter some text: ")
    
    found_dates = extract_dates(user_input)

    if found_dates:
        print(f"\n✅ Found {len(found_dates)} date(s):")
        for date in found_dates:
            print(f" - {date}")
    else:
        print("\n❌ No dates found in the text.")

main()

  

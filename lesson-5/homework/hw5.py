#1.

def is_leap(year): """ Determines whether a given year is a leap year.

A year is a leap year if:
- It is divisible by 4, and
- It is NOT divisible by 100, unless it is also divisible by 400.

Parameters:
year (int): The year to be checked.

Returns:
bool: True if the year is a leap year, False otherwise.
"""
if not isinstance(year, int):
    raise ValueError("Year must be an integer.")

return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



def is_leap(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input('enter a year'))

# leap year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

#2. Conditional Statements Exercise
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format
A single line containing a positive integer, n.

Constraints
1 <= n <= 100
Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0
3
Sample Output 0
Weird
                                           
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

if __name__ == "__main__":
    n = int(input().strip())
    if 1 <= n <= 100:
        check_weird(n)
    else:
        print("Input out of bounds. Please enter a number between 1 and 100.")

      #3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
Give two solutions.

Solution 1 with if-else statement.

Solution 2 without if-else statement.

      def even_numbers_with_if(a, b):
    if a % 2 != 0:
        a += 1
    if a > b:
        return []
    return list(range(a, b + 1, 2))
print(even_numbers_with_if(3, 10))  # [4, 6, 8, 10]

                                           

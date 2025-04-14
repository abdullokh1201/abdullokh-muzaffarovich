#1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {
    "apple": 10,
    "banana": 5,
    "cherry": 20,
    "date": 15
}

ascending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", ascending_sorted)
print("Descending order:", descending_sorted)

#2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.

Sample Dictionary:

{0: 10, 1: 20}
Expected Result:

{0: 10, 1: 20, 2: 30}


my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print(my_dict)
#3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
Expected Result:

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}

print(merged_dict)

#4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

Sample Dictionary (n = 5):

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

           
def generate_squares(n):

    squares_dict = {x: x**2 for x in range(1, n+1)}
    return squares_dict


n = 5
squares = generate_squares(n)

print(squares)

#5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

       squares_dict = {x: x**2 for x in range(1, 16)}

print(squares_dict)

       #Set Exercises
#1. Create a Set
Write a Python program to create a set.
       
my_set = set([1, 2, 3, 4, 5])

another_set = {10, 20, 30, 40, 50}

print("Set created using set() function:", my_set)
print("Set created using curly braces:", another_set)

#2. Iterate Over a Set
Write a Python program to iterate over sets.

     
my_set = {1, 2, 3, 4, 5}

for element inmy_set:
    print(element)

#3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.
           
my_set = {1, 2, 3, 4}

my_set.add(5)

my_set.update([6, 7, 8])

print("Updated set:", my_set)\

#4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.
my_set = {1, 2, 3, 4, 5}

my_set.remove(3)

my_set.discard(2)

my_set.discard(10)

random_item = my_set.pop()

my_set.clear()

print("Random item removed with pop():", random_item)
print("Set after clearing:", my_set)

#5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}


item_to_remove = 3

if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"Item {item_to_remove} removed from the set.")
else:
    print(f"Item {item_to_remove} is not present in the set.")

print("Updated set:", my_set)
           
           
  

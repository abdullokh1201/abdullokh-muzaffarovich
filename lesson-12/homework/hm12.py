#1.Exercise 1: Threaded Prime Number Checker

Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

  import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, primes_list, lock):
    for num in range(start, end):
        if is_prime(num):
            with lock:
                primes_list.append(num)

def threaded_prime_checker(start, end, num_threads):
    primes_list = []
    lock = threading.Lock()
    thread_list = []
    range_size = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * range_size
        thread_end = start + (i + 1) * range_size if i != num_threads - 1 else end
        thread = threading.Thread(target=check_primes_in_range, args=(thread_start, thread_end, primes_list, lock))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    return sorted(primes_list)

if __name__ == "__main__":
    start_range = int(input("Enter the starting number of the range: "))
    end_range = int(input("Enter the ending number of the range: "))
    num_threads = int(input("Enter the number of threads to use: "))

    prime_numbers = threaded_prime_checker(start_range, end_range, num_threads)
    print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")


#2.Exercise 2: Threaded File Processing

Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.


import threading
from collections import defaultdict

def count_words_in_chunk(file_path, start_line, end_line, word_counts, lock):
    with open(file_path, 'r') as file:
        for _ in range(start_line):
            file.readline()
        
        for line_num in range(start_line, end_line):
            line = file.readline()
            if not line:
                break
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?()[]{}":;')
                with lock:
                    word_counts[word] += 1

def threaded_word_counter(file_path, num_threads):
    with open(file_path, 'r') as file:
        total_lines = sum(1 for _ in file)
    
    lock = threading.Lock()
    word_counts = defaultdict(int)
    thread_list = []
    lines_per_thread = total_lines // num_threads

    for i in range(num_threads):
        start_line = i * lines_per_thread
        end_line = start_line + lines_per_thread if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=count_words_in_chunk, args=(file_path, start_line, end_line, word_counts, lock))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    return word_counts

def display_word_counts(word_counts):
    print("\nWord Occurrences:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    num_threads = int(input("Enter the number of threads to use: "))

    word_counts = threaded_word_counter(file_path, num_threads)
    display_word_counts(word_counts)
Enter the file path: large_text_file.txt
Enter the number of threads to use: 4

Word Occurrences:
a: 150
an: 25
the: 800
example: 10
text: 55
...


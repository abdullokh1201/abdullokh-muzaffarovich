#1.Task: JSON Parsing
write a Python script that reads the students.jon JSON file and prints details of each student.

  import json

def read_students_file(file_path):
    try:
        with open(file_path, 'r') as file:
            students_data = json.load(file)
            return students_data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
    return []

def print_student_details(students):
    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}:")
        for key, value in student.items():
            print(f"  {key.capitalize()}: {value}")

def main():
    file_path = 'students.json'
    students = read_students_file(file_path)
    if students:
        print_student_details(students)

if __name__ == "__main__":
    main()

[
    {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A"
    },
    {
        "name": "Bob Smith",
        "age": 22,
        "grade": "B"
    }
]

#2.

import requests

def get_weather_data(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data ({response.status_code})")
        return None

def print_weather_info(weather_data):
    if weather_data:
        name = weather_data.get('name')
        temp = weather_data['main'].get('temp')
        humidity = weather_data['main'].get('humidity')
        description = weather_data['weather'][0].get('description')

        print(f"Weather in {name}:")
        print(f"  Temperature: {temp}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Condition: {description.capitalize()}")

def main():
    city = "Tashkent"
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    weather_data = get_weather_data(city, api_key)
    print_weather_info(weather_data)

if __name__ == "__main__":
    main()
pip install requests

python weather_tashkent.py

#3.Task: JSON Modification
Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

  import json
import os

# Path to the JSON file
BOOKS_FILE = 'books.json'

# Load books from the JSON file
def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Save books to the JSON file
def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()

    books = load_books()
    books.append({
        "title": title,
        "author": author,
        "year": year
    })
    save_books(books)
    print(f"✅ Book '{title}' added successfully!")

# Update an existing book
def update_book():
    books = load_books()
    title_to_update = input("Enter the title of the book to update: ").strip()

    for book in books:
        if book['title'].lower() == title_to_update.lower():
            print(f"Editing '{book['title']}'")
            book['title'] = input("New title (leave blank to keep current): ") or book['title']
            book['author'] = input("New author (leave blank to keep current): ") or book['author']
            book['year'] = input("New year (leave blank to keep current): ") or book['year']
            save_books(books)
            print("✅ Book updated successfully!")
            return

    print("❌ Book not found.")

# Delete a book
def delete_book():
    books = load_books()
    title_to_delete = input("Enter the title of the book to delete: ").strip()

    updated_books = [book for book in books if book['title'].lower() != title_to_delete.lower()]

    if len(updated_books) < len(books):
        save_books(updated_books)
        print(f"✅ Book '{title_to_delete}' deleted successfully!")
    else:
        print("❌ Book not found.")

# Main menu
def main():
    while True:
        print("\n📚 Book Manager")
        print("1. Add a new book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            print("👋 Exiting program.")
            break
        else:
            print("❗ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
[
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": "1813"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": "1949"
    }
]

#4.
Task: Movie Recommendation System
Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OMDb API key
OMDB_URL = "http://www.omdbapi.com/"

# Predefined popular movie titles (OMDb doesn't support genre search directly)
MOVIE_TITLES = [
    "Inception", "The Dark Knight", "Interstellar", "The Matrix", "Pulp Fiction",
    "The Shawshank Redemption", "The Godfather", "Forrest Gump", "Fight Club", 
    "Gladiator", "The Prestige", "Titanic", "The Silence of the Lambs",
    "The Lord of the Rings", "Avengers: Endgame", "Black Panther"
]

def fetch_movie(title):
    params = {
        "t": title,
        "apikey": API_KEY
    }
    response = requests.get(OMDB_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Failed to fetch data from OMDb API.")
        return None

def recommend_movie_by_genre(genre):
    filtered_movies = []
    for title in MOVIE_TITLES:
        data = fetch_movie(title)
        if data and "Genre" in data:
            if genre.lower() in data["Genre"].lower():
                filtered_movies.append(data)

    if filtered_movies:
        selected = random.choice(filtered_movies)
        print("\n🎬 Recommended Movie:")
        print(f"Title: {selected['Title']}")
        print(f"Year: {selected['Year']}")
        print(f"Genre: {selected['Genre']}")
        print(f"Plot: {selected['Plot']}")
        print(f"IMDB Rating: {selected['imdbRating']}")
    else:
        print(f"No movies found in the genre '{genre}'.")

def main():
    genre = input("Enter a movie genre (e.g., Action, Drama, Sci-Fi): ").strip()
    recommend_movie_by_genre(genre)

if __name__ == "__main__":
    main()

  

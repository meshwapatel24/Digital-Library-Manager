import csv

FILE_NAME = "books.csv"


def load_books():
    books = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books.append(row)

    except FileNotFoundError:
        pass

    return books


def save_books(books):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "title", "author", "genre", "rating"]
        )

        writer.writeheader()
        writer.writerows(books)
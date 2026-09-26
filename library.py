from storage import load_books, save_books


def add_book(book):
    books = load_books()

    for b in books:
        if b["id"] == book["id"]:
            return False, "Book ID already exists!"

    books.append(book)
    save_books(books)

    return True, "Book added successfully!"


def update_book(book_id, new_book):
    books = load_books()

    for book in books:
        if book["id"] == book_id:
            book.update(new_book)
            save_books(books)
            return True, "Book updated successfully!"

    return False, "Book not found!"


def delete_book(book_id):
    books = load_books()

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            return True, "Book deleted successfully!"

    return False, "Book not found!"


def search_books(keyword):
    books = load_books()
    result = []

    keyword = keyword.lower()

    for book in books:
        if (keyword in book["title"].lower()
                or keyword in book["author"].lower()
                or keyword in book["genre"].lower()):

            result.append(book)

    return result


def filter_books(genre):
    books = load_books()

    return [
        book for book in books
        if book["genre"].lower() == genre.lower()
    ]
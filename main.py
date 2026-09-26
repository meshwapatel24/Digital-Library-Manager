import tkinter as tk
from tkinter import ttk, messagebox

from library import add_book, update_book, delete_book, search_books, filter_books
from storage import load_books
from charts import show_genre_chart, show_rating_chart, get_summary


def clear_fields():
    id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)


def get_data():
    return {
        "id": id_entry.get(),
        "title": title_entry.get(),
        "author": author_entry.get(),
        "genre": genre_entry.get(),
        "rating": rating_entry.get()
    }


def validate():
    if any(x.get() == "" for x in
           [id_entry, title_entry, author_entry, genre_entry, rating_entry]):
        messagebox.showerror("Error", "Please fill all fields")
        return False

    try:
        rating = float(rating_entry.get())
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Rating must be between 1 and 5")
        return False

    return True


def refresh(books=None):
    for item in table.get_children():
        table.delete(item)

    if books is None:
        books = load_books()

    for b in books:
        table.insert("", tk.END,
                     values=(b["id"], b["title"], b["author"],
                             b["genre"], b["rating"]))

    total, avg = get_summary()
    total_label.config(text=f"Total Books: {total}")
    average_label.config(text=f"Average Rating: {avg:.2f}")


def add():
    if validate():
        ok, msg = add_book(get_data())
        messagebox.showinfo("Library", msg)
        if ok:
            clear_fields()
            refresh()


def update():
    if validate():
        ok, msg = update_book(id_entry.get(), get_data())
        messagebox.showinfo("Library", msg)
        if ok:
            clear_fields()
            refresh()


def delete():
    if id_entry.get() == "":
        messagebox.showerror("Error", "Enter Book ID")
        return

    ok, msg = delete_book(id_entry.get())
    messagebox.showinfo("Library", msg)

    if ok:
        clear_fields()
        refresh()


def search():
    refresh(search_books(search_entry.get()))


def filter_genre():
    refresh(filter_books(filter_entry.get()))


root = tk.Tk()
root.title("Digital Library Manager")
root.geometry("900x650")


tk.Label(
    root,
    text="DIGITAL LIBRARY MANAGER",
    font=("Arial", 20, "bold")
).pack(pady=10)


frame = tk.Frame(root)
frame.pack()


tk.Label(frame, text="Book ID").grid(row=0, column=0, padx=5, pady=5)
id_entry = tk.Entry(frame)
id_entry.grid(row=0, column=1)


tk.Label(frame, text="Title").grid(row=0, column=2, padx=5)
title_entry = tk.Entry(frame)
title_entry.grid(row=0, column=3)


tk.Label(frame, text="Author").grid(row=1, column=0, padx=5, pady=5)
author_entry = tk.Entry(frame)
author_entry.grid(row=1, column=1)


tk.Label(frame, text="Genre").grid(row=1, column=2, padx=5)
genre_entry = tk.Entry(frame)
genre_entry.grid(row=1, column=3)


tk.Label(frame, text="Rating").grid(row=2, column=0, padx=5, pady=5)
rating_entry = tk.Entry(frame)
rating_entry.grid(row=2, column=1)


buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="Add Book", width=12, command=add).grid(row=0, column=0, padx=5)
tk.Button(buttons, text="Update", width=12, command=update).grid(row=0, column=1, padx=5)
tk.Button(buttons, text="Delete", width=12, command=delete).grid(row=0, column=2, padx=5)
tk.Button(buttons, text="Show All", width=12, command=refresh).grid(row=0, column=3, padx=5)


search_frame = tk.Frame(root)
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search").grid(row=0, column=0)

search_entry = tk.Entry(search_frame, width=25)
search_entry.grid(row=0, column=1, padx=5)

tk.Button(search_frame, text="Search", command=search).grid(row=0, column=2)


tk.Label(search_frame, text="Genre Filter").grid(row=1, column=0, pady=5)

filter_entry = tk.Entry(search_frame, width=25)
filter_entry.grid(row=1, column=1)

tk.Button(search_frame, text="Filter", command=filter_genre).grid(row=1, column=2)


columns = ("ID", "Title", "Author", "Genre", "Rating")

table = ttk.Treeview(root, columns=columns, show="headings", height=12)
table.pack(pady=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=160)


summary = tk.Frame(root)
summary.pack(pady=5)

total_label = tk.Label(summary, text="Total Books: 0",
                       font=("Arial", 12, "bold"))
total_label.grid(row=0, column=0, padx=30)

average_label = tk.Label(summary, text="Average Rating: 0",
                         font=("Arial", 12, "bold"))
average_label.grid(row=0, column=1, padx=30)


charts = tk.Frame(root)
charts.pack(pady=10)

tk.Button(
    charts,
    text="Genre Chart",
    width=15,
    command=show_genre_chart
).grid(row=0, column=0, padx=10)

tk.Button(
    charts,
    text="Rating Chart",
    width=15,
    command=show_rating_chart
).grid(row=0, column=1, padx=10)


refresh()

root.mainloop()
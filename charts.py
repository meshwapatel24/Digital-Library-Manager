import pandas as pd
import matplotlib.pyplot as plt


def show_genre_chart():
    df = pd.read_csv("books.csv")

    if df.empty:
        return

    genre_count = df["genre"].value_counts()

    genre_count.plot(kind="bar")

    plt.title("Books by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.show()


def show_rating_chart():
    df = pd.read_csv("books.csv")

    if df.empty:
        return

    rating_count = df["rating"].value_counts().sort_index()

    rating_count.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Book Rating Distribution")
    plt.ylabel("")
    plt.show()


def get_summary():
    df = pd.read_csv("books.csv")

    if df.empty:
        return 0, 0

    total_books = len(df)
    average_rating = df["rating"].astype(float).mean()

    return total_books, average_rating
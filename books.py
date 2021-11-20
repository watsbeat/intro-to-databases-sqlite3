# 💁🏻‍♀️ Import the sqlite3 module into your file - this is bundled with your Python install
import sqlite3

# 💁🏻‍♀️ Connect to SQLite DB - opens a connection to the SQLite database file, i.e. books.db
# 👉🏼 The books.db file will be generated when you run this file in your terminal: `python3 books.py`
connection = sqlite3.connect("books.db")

# 💁🏻‍♀️ The cursor object is used to invoke methods that execute SQL, fetch data from query results
cursor = connection.cursor()

# Ex 1: Fix the error caused by the table already existing
cursor.execute("""
    DROP TABLE IF EXISTS books
""")

# 💁🏻‍♀️ .execute() executes an SQL statement against the db
cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        pages INTEGER,
        current_page INTEGER
    )
""")

cursor.execute("""
    INSERT INTO books VALUES (
        0, 'A great book', 213, 27
    )
""")

cursor.execute("""
    INSERT INTO books VALUES (
        1, 'Another great book', 395, 387
    )
""")

cursor.execute("""
    INSERT INTO books VALUES (
        2, 'An okay book', 120, 45
    )
""")

# 💁🏻‍♀️ .commit() is used to save changes invoked by a transaction to the database
connection.commit()

# Ex 2: Get all records from the books table
# 👉🏼 Wrap in a function so we can reuse this later on...

def get_all_book_data():
    allBooks = cursor.execute("""
        SELECT * FROM books
    """)

    bookTitles = []

    for book in allBooks:
        print('book data:', book)
        bookTitles.append(book[1])

    print('titles list:', bookTitles)

get_all_book_data()

# Ex 3: Get the title & pages of book with id 0
firstBook = cursor.execute("""
    SELECT title, pages FROM books WHERE id=0
"""
)

# 💁🏻‍♀️ .fetchone() fetches the next row of a query result or None when no more data
print('First book:', firstBook.fetchone())

# Ex 4: Delete "A great book" from db
cursor.execute("""
    DELETE FROM books WHERE id=0
""")

# Ex 5: Change the current page of "Another great book" to 100
cursor.execute("""
    UPDATE books SET current_page=100 WHERE id=1
""")

connection.commit()

# Ex 6: Find how many hours it will take a user to read each book
def calculate_read_time():
    books_with_page_counts = cursor.execute("SELECT title, pages FROM books")
    read_speed = input('How many pages do you read per minute? ')

    for book in books_with_page_counts:
        read_time = book[1] / float(read_speed) / 60
        print('%.2f' % read_time, 'hours to read', book[0])

    # 👉🏼 We don't need to commit after SELECTs, since we're not changing data, just retrieving it.

calculate_read_time()

# Ex 7: Add tech books to the database
tech_books = [
    {'title': 'Clean Code', 'pages': 300, 'current_page': 2},
    {'title': 'Pragmatic Programmer', 'pages': 400, 'current_page': 60},
    {'title': 'Refactoring', 'pages': 420, 'current_page': 95},
]

def add_tech_book(tech_book):
    # 💁🏻‍♀️ An SQL statement may be parameterized, i.e. placeholders
    cursor.execute("INSERT INTO books (title, pages, current_page) VALUES (?, ?, ?)",
        (tech_book['title'], tech_book['pages'], tech_book['current_page']))
    connection.commit()

for tech_book in tech_books:
    add_tech_book(tech_book)

# 👉🏼 Let's check our book data again → we should see the tech books added
get_all_book_data()

# 💁🏻‍♀️ Remember to close the db connection when you're done with it - commit any changes!
connection.close()
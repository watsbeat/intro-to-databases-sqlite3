# Introduction to Databases

```
🎯 Lesson Goals

-   Understand what a database is
-   Understand that we can use a database in order for data to persist

Things we'll be doing:

-   How to create a database using sqlite3
-   How to insert data into the database
-   How to fetch data from the database
```

## 0. What is a Database?

Simply put, a database is where we store data (information) for access and management. Before computers, we stored data in physical systems like printed books or cards.

We use databases so that we can persist data - so that the data remains even after the process that created it has finished.

There are many different types of databases, but we'll be focusing on "relational" databases.

## 1. What is a Relational Database?

-   **Relational** database management system (RDMS) = a common type of database, where "data is stored in tables so it can be used in relation to other datasets" - makes it easy to find specific info.

---

### 1.2 Database Tables

-   Store similar data in a structured manner
-   Have columns (fields) and rows (records)
-   Column is labelled with descriptive name and has a _data type_, e.g. "title" field should have string data only.
-   Can have millions of records
-   May "relate" to other tables in the database via key, e.g. we've set "id" as the primary key for the books table.

#### Table Example: Books

| id  | title              | pages | current_page |
| --- | ------------------ | ----- | ------------ |
| 0   | A great book       | 213   | 27           |
| 1   | Another great book | 395   | 387          |

### 1.2 When Should We Use a Relational Database?

Depends on your data!

> A relational database can be considered for any information need in which data points relate to each other and must be managed in a secure, rules-based, consistent way. Relational databases have been around since the 1970s. - [Oracle](https://www.google.com/search?q=why+use+a+relational+database&oq=why+use+a+relational+database&aqs=chrome..69i57.5002j0j7&sourceid=chrome&ie=UTF-8#:~:text=database%3F-,A%20relational%20database%20can,around%20since%20the%201970s.,-What)

<details>
    <summary>Compare non-relational database (stores data in a non-tabular form)</summary>

> Non-relational databases often perform faster because a query doesn't have to view several tables in order to deliver an answer, as relational datasets often do. Non-relational databases are therefore ideal for storing data that may be changed frequently or for applications that handle many different kinds of data. - [MongoDB](https://www.mongodb.com/non-relational-database)

</details>

---

## 2. What is SQL?

-   SQL = **S**tructured **Q**uery **L**anguage
-   Used for querying a database - to create, read, update or delete data (CRUD) generally stored in a "relational" database
-   SQL syntax comes in different flavours like PostgreSQL or MySQL. We're going to be using SQLite.

---

## 3. SQLite3

> A popular open source SQL database. It can store an entire database in a single file. One of the most significant advantages this provides is that all of the data can be stored locally without having to connect your database to a server. - [Source: 'What is a RDBMS?'](https://www.codecademy.com/articles/what-is-rdbms-sql)

-   Easy to use relational database engine - a **relational** database management system (RDMS)
-   Python includes a "sqlite3" module for working with this database.

📙 Read the official docs [here](https://docs.python.org/3/library/sqlite3.html)

#### 💡 How to install the SQLite VSCode Extension

-   We open the `.db` file in our code editor to view the database, but this isn't very readable - you'll probably see a message saying that the file "is either binary or uses an unsupported text encoding."
-   So we can use this helpful tool to explore and query SQLite databases within VSCode, e.g. it lets us view the tables nicely.

**Instructions:**

1. Go to this [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) and install the extension
2. To use the extension, open View > Command Palette and search for `SQLite: Open Database`.
3. When you select this command, you should be prompted to "Choose a database" and see options that include your newly created `books.db` - select this.
4. In your VSCode Explore (the left sidebar), you should see a toggle section called `SQLite Explorer` - click the "Show Table" play button next to the table you want to view, i.e. `books`. This should open up the a readable books table in your editor 🎉

---

## 🏋🏻 Exercises

1. Fix the re-run error caused by table already existing
2. Get all book data from the db, but only print the titles
3. Get book from db where id is 1
4. Delete 'A great book' from db
5. Change the current page of 'Another great book' to 100
6. Ask users how many pages they read per minute and print how long it will take to read each book
7. Add all books in `techBooks` to the db -> only write one SQL statement.

```python
techBooks = [
    {'title': 'Clean Code', 'pages': 300, 'current_page': 2},
    {'title': 'Pragmatic Programmer', 'pages': 400, 'current_page': 60},
    {'title': 'Refactoring', 'pages': 420, 'current_page': 95},
]
```

💡 Use a function, pass book properties as parameters

---

## ℹ️ Final Notes

-   Writing custom SQL can be complex, so we can use an ORM (Object Relation Mapper) instead, e.g. _Django ORM_.
-   An ORM abstracts away the database layer and lets us interact with the database models.

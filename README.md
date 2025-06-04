# Many-to-Many Relationship Example with SQLAlchemy

This project demonstrates how to implement a many-to-many relationship between `Author` and `Book` models using SQLAlchemy ORM with an SQLite in-memory database.

---

## Features

- Define models `Author` and `Book` with a many-to-many relationship via an association table.
- Create and associate authors and books.
- Query authors and their corresponding books.
- Use SQLAlchemy ORM with declarative base and session management.

---

## Setup

1. **Clone the repository** (or copy the code files to your workspace).

2. **Create and activate a virtual environment** (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  

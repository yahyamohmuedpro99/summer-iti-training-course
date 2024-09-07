# Entity-Relationship Diagrams (ERD) and SQL Implementation

## Overview
This lesson focuses on creating Entity-Relationship Diagrams (ERDs) and translating them into SQL statements. We'll use a library management system as our example.

## Learning Objectives
By the end of this lesson, you will be able to:
1. Understand the components of an ERD
2. Create a basic ERD for a given scenario
3. Translate an ERD into SQL statements

## 1. Entity-Relationship Diagram Basics

### Components of an ERD
1. Entities: Represent objects or concepts (e.g., Book, Author)
2. Attributes: Properties of entities (e.g., title, author_name)
3. Relationships: Connections between entities (e.g., Author writes Book)

### Cardinality in Relationships
- One-to-One (1:1)
- One-to-Many (1:N)
- Many-to-Many (M:N)

## 2. Creating an ERD: Library Management System

Let's create an ERD for a simple library management system with the following entities:
- Book
- Author
- Member
- Loan

```

+-------------+     +-------------+
|   Author    |     |    Book     |
+-------------+     +-------------+
| PK author_id|<-+->| PK book_id  |
|   name      |  |  |   title     |
|   birth_year|  |  |   isbn      |
+-------------+  |  |   pub_year  |
                 |  +-------------+
                 |
          +------+------+
          | book_author |
          +-------------+
          | PK,FK book_id   |
          | PK,FK author_id |
          +-------------+

+-------------+     +-------------+
|   Member    |     |    Loan     |
+-------------+     +-------------+
| PK member_id|---->| PK loan_id  |
|   name      |     | FK member_id|
|   email     |     | FK book_id  |
|   join_date |     |   loan_date |
+-------------+     |   due_date  |
                    |   return_date|
                    +-------------+
```

### Explanation of the ERD
1. Author and Book have a many-to-many relationship (an author can write many books, a book can have multiple authors).
2. Member and Book have a many-to-many relationship through the Loan entity.
3. Each entity has a primary key (PK) for unique identification.
4. Relationships are represented by lines between entities, with crow's foot notation indicating cardinality.

## 3. Translating ERD to SQL

Now, let's translate this ERD into SQL statements to create the corresponding database schema.

```sql
-- Create Author table
CREATE TABLE Author (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_year INTEGER
);

-- Create Book table
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    pub_year INTEGER
);

-- Create BookAuthor table (for many-to-many relationship)
CREATE TABLE BookAuthor (
    book_id INTEGER REFERENCES Book(book_id),
    author_id INTEGER REFERENCES Author(author_id),
    PRIMARY KEY (book_id, author_id)
);

-- Create Member table
CREATE TABLE Member (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    join_date DATE DEFAULT CURRENT_DATE
);

-- Create Loan table
CREATE TABLE Loan (
    loan_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Member(member_id),
    book_id INTEGER REFERENCES Book(book_id),
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE
);
```

### Explanation of the SQL Translation
1. Each entity in the ERD becomes a table in SQL.
2. Attributes become columns in their respective tables.
3. Primary keys are defined using `PRIMARY KEY`.
4. Foreign keys are created using `REFERENCES` to establish relationships between tables.
5. The many-to-many relationship between Book and Author is resolved by creating an intermediate table `BookAuthor`.

## 4. Key Points in ERD to SQL Translation

1. **Primary Keys**: Always create a unique identifier for each entity, typically using `SERIAL PRIMARY KEY` in PostgreSQL for auto-incrementing integers.

2. **Foreign Keys**: Use `REFERENCES` to create foreign key constraints, ensuring referential integrity.

3. **Many-to-Many Relationships**: Resolve these by creating an intermediate table with foreign keys to both related entities.

4. **Data Types**: Choose appropriate SQL data types for each attribute (e.g., VARCHAR for strings, INTEGER for whole numbers, DATE for dates).

5. **Constraints**: Implement constraints like `NOT NULL` for required fields and `UNIQUE` for fields that must have unique values.

6. **Default Values**: Use `DEFAULT` clause to set default values where appropriate.

## 5. Practice Exercise

Try creating an ERD and corresponding SQL statements for a simple online store with the following requirements:
- Store information about products, categories, customers, and orders.
- A product belongs to one category, but a category can have many products.
- A customer can place many orders, and each order can contain multiple products.

## Conclusion

Understanding how to create ERDs and translate them into SQL is a fundamental skill in database design. It helps in visualizing the structure of your database and ensures that you create a well-organized and efficient schema. Practice creating ERDs for different scenarios and writing the corresponding SQL to reinforce these skills.
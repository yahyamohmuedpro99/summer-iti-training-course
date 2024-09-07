# Database Course : Deeper Dive into SQL & Data Modeling

## Overview
Today, we'll explore advanced SQL queries and data modeling concepts, with practical examples to reinforce your learning.

## Goal
Develop your SQL skills to handle complex queries and introduce you to data modeling principles, enabling you to design and implement efficient database structures.

## Curriculum

### 1. Advanced SQL Queries

#### Filtering Data with WHERE Clause
```sql
-- Complex conditions
SELECT * FROM products
WHERE (category = 'Electronics' OR category = 'Computers')
  AND price > 500;

-- Pattern matching
SELECT * FROM customers
WHERE last_name LIKE 'Sm%';

-- Range queries
SELECT * FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

-- Handling NULL values
SELECT * FROM employees
WHERE manager_id IS NULL;
```

#### Sorting Results with ORDER BY
```sql
-- Multiple column sorting
SELECT product_name, category, price
FROM products
ORDER BY category ASC, price DESC;
```

#### Aggregations and Grouping
```sql
-- Basic aggregation
SELECT category, COUNT(*) as product_count, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING COUNT(*) > 5
ORDER BY avg_price DESC;
```

#### Working with Multiple Tables: JOINs
```sql
-- INNER JOIN
SELECT o.order_id, c.customer_name, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- LEFT JOIN
SELECT p.product_name, o.order_id
FROM products p
LEFT JOIN order_items o ON p.product_id = o.product_id;

-- Self-join (finding employees and their managers)
SELECT e1.employee_name, e2.employee_name as manager_name
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

#### Subqueries
```sql
-- Subquery in WHERE clause
SELECT product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- Subquery in SELECT
SELECT 
    category,
    (SELECT COUNT(*) FROM products p2 WHERE p2.category = p1.category) as product_count
FROM 
    products p1
GROUP BY 
    category;
```

#### Real-world Query Examples
```sql
-- Finding top customers by order value
SELECT 
    c.customer_id,
    c.customer_name,
    SUM(oi.quantity * p.price) as total_order_value
FROM 
    customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
GROUP BY 
    c.customer_id, c.customer_name
ORDER BY 
    total_order_value DESC
LIMIT 5;

-- Calculating running totals
SELECT 
    order_date,
    daily_total,
    SUM(daily_total) OVER (ORDER BY order_date) as running_total
FROM (
    SELECT 
        DATE(order_date) as order_date,
        SUM(total_amount) as daily_total
    FROM 
        orders
    GROUP BY 
        DATE(order_date)
) daily_orders;
```

### 2. Data Modeling Basics

#### Creating Tables with Normalization in Mind
```sql
-- First Normal Form: No repeating groups
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE customer_phones (
    customer_id INTEGER REFERENCES customers(customer_id),
    phone_number VARCHAR(20),
    phone_type VARCHAR(10),
    PRIMARY KEY (customer_id, phone_number)
);

-- Third Normal Form: No transitive dependencies
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE product_categories (
    product_id INTEGER REFERENCES products(product_id),
    category_id INTEGER REFERENCES categories(category_id),
    PRIMARY KEY (product_id, category_id)
);
```

### 3. Hands-on: Building a Simple Database

#### Project: Online Bookstore Database
```sql
-- Authors table
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL,
    birth_date DATE
);

-- Books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publication_date DATE,
    isbn VARCHAR(13) UNIQUE,
    price DECIMAL(10, 2)
);

-- Book-Author relationship (Many-to-Many)
CREATE TABLE book_authors (
    book_id INTEGER REFERENCES books(book_id),
    author_id INTEGER REFERENCES authors(author_id),
    PRIMARY KEY (book_id, author_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    registration_date DATE DEFAULT CURRENT_DATE
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2)
);

-- Order Items table
CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(order_id),
    book_id INTEGER REFERENCES books(book_id),
    quantity INTEGER CHECK (quantity > 0),
    price_at_time DECIMAL(10, 2),
    PRIMARY KEY (order_id, book_id)
);

-- Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(book_id),
    customer_id INTEGER REFERENCES customers(customer_id),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Populating the Database
```sql
-- Insert sample data
INSERT INTO authors (author_name, birth_date) VALUES
('J.K. Rowling', '1965-07-31'),
('George Orwell', '1903-06-25');

INSERT INTO books (title, publication_date, isbn, price) VALUES
('Harry Potter and the Philosopher''s Stone', '1997-06-26', '9780747532699', 19.99),
('1984', '1949-06-08', '9780451524935', 14.99);

INSERT INTO book_authors (book_id, author_id) VALUES
(1, 1),
(2, 2);

-- More INSERT statements for other tables...
```

#### Querying the Bookstore Database
```sql
-- Finding top-selling books
SELECT 
    b.title,
    SUM(oi.quantity) as total_sold
FROM 
    books b
    JOIN order_items oi ON b.book_id = oi.book_id
GROUP BY 
    b.book_id, b.title
ORDER BY 
    total_sold DESC
LIMIT 5;

-- Calculating average ratings for books
SELECT 
    b.title,
    ROUND(AVG(r.rating), 2) as avg_rating,
    COUNT(r.review_id) as review_count
FROM 
    books b
    LEFT JOIN reviews r ON b.book_id = r.book_id
GROUP BY 
    b.book_id, b.title
HAVING 
    COUNT(r.review_id) > 5
ORDER BY 
    avg_rating DESC;

-- Identifying customers with the most orders
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name as customer_name,
    COUNT(o.order_id) as order_count,
    SUM(o.total_amount) as total_spent
FROM 
    customers c
    JOIN orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, customer_name
ORDER BY 
    order_count DESC, total_spent DESC
LIMIT 10;
```

### 4. Review & Addressing Common Issues

#### Common Mistakes and Solutions
```sql
-- Inefficient: Using subquery in WHERE clause for every row
SELECT *
FROM orders
WHERE customer_id IN (SELECT customer_id FROM customers WHERE country = 'USA');

-- More efficient: Using JOIN
SELECT o.*
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.country = 'USA';

-- Inefficient: Not using appropriate indexes
CREATE INDEX idx_customers_country ON customers(country);
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

## Next Steps
In our next session, we'll explore more advanced database concepts, including transaction management, concurrency control, and database performance optimization. We'll also look at how to integrate databases with application development.

Remember to practice these SQL queries and experiment with your own variations to solidify your understanding!
# Day 3: Working with Postgres Features & Real-World Scenarios

## Goal
Explore advanced Postgres features and real-world database use cases.

## 1. Indexes, Constraints, and Transactions 

### a. Indexes

Indexes are data structures that improve the speed of data retrieval operations on a database table. They work similarly to an index in a book, allowing the database to quickly locate the data without scanning the entire table.

```sql
-- Creating an index
CREATE INDEX idx_product_name ON products(name);

-- Analyzing query performance
EXPLAIN ANALYZE SELECT * FROM products WHERE name = 'Laptop';
```

Explanation:
- The first command creates an index on the 'name' column of the 'products' table. This can significantly speed up searches based on product names.
- The second command uses EXPLAIN ANALYZE to show how Postgres executes the query, including whether it uses the index we just created.

### b. Constraints

Constraints are rules enforced on the data columns of a table. They are used to limit the type of data that can go into a table, ensuring the accuracy and reliability of the data.

```sql
-- UNIQUE constraint
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);

-- CHECK constraint
ALTER TABLE products ADD CONSTRAINT positive_price CHECK (price > 0);

-- FOREIGN KEY constraint
ALTER TABLE orders 
ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) 
REFERENCES users(id) 
ON DELETE CASCADE;
```

Explanation:
- The UNIQUE constraint ensures that all values in the 'email' column are different.
- The CHECK constraint ensures that the 'price' is always positive.
- The FOREIGN KEY constraint ensures that every 'user_id' in the 'orders' table exists in the 'users' table. The ON DELETE CASCADE means that if a user is deleted, all their orders will be deleted too.

### c. Transaction Management

A transaction is a unit of work that is performed against a database. Transactions are important for maintaining data integrity in case of errors or system failures.

```sql
BEGIN;
UPDATE products SET stock_quantity = stock_quantity - 1 WHERE id = 1;
UPDATE orders SET status = 'shipped' WHERE id = 1001;
COMMIT;
```

Explanation:
- BEGIN starts a transaction.
- The two UPDATE statements are part of the same transaction.
- COMMIT ends the transaction and saves all changes. If an error occurred between BEGIN and COMMIT, we could use ROLLBACK instead to undo all changes.

## 2. Postgres-Specific Features

### a. JSON and JSONB Support

JSON (JavaScript Object Notation) is a popular data format. Postgres provides robust support for JSON data, with JSONB being a binary, more efficient storage and processing format.

```sql
-- Adding a JSONB column
ALTER TABLE products ADD COLUMN metadata JSONB;

-- Querying JSON data
SELECT * FROM products WHERE metadata @> '{"color": "red"}';
```

Explanation:
- The first command adds a JSONB column named 'metadata' to the 'products' table.
- The second command retrieves all products where the metadata includes the key-value pair "color": "red". The @> operator checks if the left JSON value contains the right JSON path/value entries.

### b. Working with Arrays and Advanced Data Types

Postgres supports array data types, allowing you to store multiple values in a single column. It also provides powerful text search capabilities.

```sql
-- Array operations
SELECT ARRAY[1,2,3] || ARRAY[4,5,6] AS combined_array;

-- Full-text search
CREATE INDEX idx_product_description ON products USING GIN (to_tsvector('english', description));
SELECT * FROM products WHERE to_tsvector('english', description) @@ to_tsquery('english', 'laptop & powerful');
```

Explanation:
- The first query demonstrates array concatenation, combining two arrays into one.
- The second set of commands creates a GIN (Generalized Inverted Index) for full-text search on the 'description' column, then performs a search for products described as both "laptop" and "powerful".

### c. CTEs and Window Functions

Common Table Expressions (CTEs) and Window Functions are powerful features for complex data analysis.

```sql
-- CTE example
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month, SUM(total_amount) AS total
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT month, total, SUM(total) OVER (ORDER BY month) AS running_total
FROM monthly_sales;

-- Window function
SELECT product_id, 
       order_date, 
       quantity,
       SUM(quantity) OVER (PARTITION BY product_id ORDER BY order_date) AS running_total
FROM order_items
JOIN orders ON order_items.order_id = orders.id;
```

Explanation:
- The CTE creates a temporary named result set 'monthly_sales', which is then used in the main query to calculate a running total of sales.
- The window function calculates a running total of quantity sold for each product, ordered by date. The PARTITION BY clause separates the calculation for each product.

## 3. Hands-on: Real-world Scenarios 

### Scenario: E-commerce Database Design and Querying

1. Database Setup

This section creates the basic structure for an e-commerce database with tables for users, products, orders, and order items.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- (Other table creations and data insertions as in the previous response)
```

Explanation:
- SERIAL is used for auto-incrementing IDs.
- Constraints like NOT NULL and UNIQUE are used to ensure data integrity.
- DEFAULT values are set where appropriate.

2. Complex Queries

These queries demonstrate how to extract meaningful business insights from the data.

```sql
-- Find top 5 customers by total order amount
SELECT u.username, SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username
ORDER BY total_spent DESC
LIMIT 5;

-- (Other queries as in the previous response)
```

Explanation:
- The first query joins the users and orders tables, calculates the total spent by each user, and returns the top 5.
- These types of queries are crucial for understanding customer behavior and sales patterns.

3. JSON Operations

JSON operations allow for flexible storage and querying of semi-structured data.

```sql
-- Update JSON data
UPDATE products 
SET metadata = metadata || '{"warranty": "2 years"}'::jsonb 
WHERE name = 'Laptop';

-- Query JSON data
SELECT name, metadata->>'color' AS color
FROM products
WHERE metadata @> '{"storage": "128GB"}';
```

Explanation:
- The first query updates the JSON data, adding a warranty field to the metadata of laptops.
- The second query extracts the color from the metadata and filters for products with 128GB storage.

4. Inventory Management System

This section demonstrates how to use triggers to automatically update inventory when an order is placed.

```sql
-- Create a function to update stock
CREATE OR REPLACE FUNCTION update_stock() RETURNS TRIGGER AS $$
BEGIN
    UPDATE products
    SET stock_quantity = stock_quantity - NEW.quantity
    WHERE id = NEW.product_id;
    
    IF (SELECT stock_quantity FROM products WHERE id = NEW.product_id) < 0 THEN
        RAISE EXCEPTION 'Not enough stock for product %', NEW.product_id;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger
CREATE TRIGGER check_stock
BEFORE INSERT ON order_items
FOR EACH ROW
EXECUTE FUNCTION update_stock();

-- Test the trigger
BEGIN;
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (1, 1, 100, 999.99);
COMMIT;
```

Explanation:
- The function `update_stock()` is called by the trigger every time a new order item is inserted.
- It updates the stock quantity and raises an exception if there's not enough stock.
- The trigger automates this process, ensuring that stock levels are always accurate.

## 4. Wrap-up: Database Best Practices & Scaling 

### a. Security Practices

Security is crucial in database management. Here are some basic practices:

```sql
-- Create a read-only user
CREATE ROLE read_only;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only;
CREATE USER john WITH PASSWORD 'secure_password';
GRANT read_only TO john;

-- Implement row-level security
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY user_orders ON orders FOR SELECT
    USING (user_id = current_user_id());
```

Explanation:
- The first set of commands creates a read-only role and assigns it to a user. This implements the principle of least privilege.
- The second set enables row-level security on the orders table, ensuring users can only see their own orders.

### b. Backup Strategies

Regular backups are essential for data safety.

```bash
# Full backup
pg_dump dbname > backup.sql

# Restore from backup
psql dbname < backup.sql
```

Explanation:
- `pg_dump` creates a full backup of the database.
- The backup can be restored using `psql`.

### c. Database Scaling

As your data grows, you may need to scale your database. Here's an example of table partitioning, one scaling technique:

```sql
-- Example of table partitioning
CREATE TABLE orders_partitioned (
    id SERIAL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2023 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

CREATE TABLE orders_2024 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

Explanation:
- This creates a partitioned table 'orders_partitioned' split by year.
- Each partition is a separate table, which can improve query performance for large datasets.

### d. Final Q&A and Further Learning

- Recap key concepts covered during the day.
- Address any remaining questions from students.
- Provide resources for further learning, such as official documentation, books, and online tutorials.

Remember, mastering these concepts takes practice. Encourage students to experiment with these features in their own projects!
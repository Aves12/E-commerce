# E-commerce & Warehouse System

## Overview
This repository contains the implementation of a simplified e-commerce system and a warehouse inventory management system. It also includes database queries to handle specific requirements for an online bookstore.

The project is divided into three main parts:
1. **System Design**: Simplified e-commerce system with users, products, orders, and payments.
2. **Business Logic**: Inventory management system to track stock levels and manage restocking.
3. **Database Query Handling**: SQL queries for an online bookstore system.

## Part 1: System Design
### Description
- Designed an e-commerce system that supports multiple users who can create, view, and manage orders.
- Each order contains multiple products and is associated with a payment.
- Code is modular and scalable for future expansion.

### Code Location
- The code stubs are located in the `src/system_design.py` file.

### How to Run
- Simply run the Python script:
  ```bash
  python src/system_design.py
  ```

## Part 2: Business Logic Implementation
### Description
- This section implements two functions:
  1. **process_orders()**: Processes sales orders and updates stock levels.
  2. **restock_items()**: Restocks items when their levels drop below a threshold.

- The code handles error cases, such as processing orders for out-of-stock products.

### Code Location
- The business logic functions are located in the `src/inventory_management.py` file.

### How to Run
- Example usage of the two functions:
  ```bash
  python src/inventory_management.py
  ```

## Part 3: Database Query Handling
### Description
- Three SQL queries have been provided to:
  1. Retrieve the top 5 customers based on total quantity of books purchased in the last year.
  2. Calculate the total revenue generated by each author.
  3. Retrieve all books ordered more than 10 times along with their total quantity ordered.

### Query Location
- The SQL queries are in the `src/sql_queries.sql` file.

## Assumptions
- For the system design part, I assumed that all products have a predefined stock level and that orders are only processed for available products.
- I used Python for the system design and business logic implementation, and MySQL syntax for the SQL queries.

## Requirements
- Python 3.x
- Libraries (if applicable, list them in the `requirements.txt` file)

### How to Install Dependencies
- Install required Python packages using the following command:
  ```bash
  pip install -r requirements.txt
  ```

## Class Diagram
- If a visual class diagram is provided, include it in the `diagrams` directory.
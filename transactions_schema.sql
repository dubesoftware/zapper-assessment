-- The Schema contained herein is designed to track transactions between customers and merchants. Therefore, we have three tables mapping to the thrtee entities/ objects that we have identified. These are Customers, Merchants and Transactions.

-- We define the relationship between customers and merchants via the Transactions table.

-- DDL for Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(15)
);

-- DDL for merchants table
CREATE TABLE merchants (
    merchant_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255)
);

-- DDL for transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    merchant_id INT REFERENCES merchants(merchant_id),
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) CHECK (status IN ('pending', 'completed', 'failed')),
    payment_method VARCHAR(50)
);
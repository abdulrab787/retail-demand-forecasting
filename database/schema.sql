CREATE TABLE stores (
    store_nbr INT PRIMARY KEY,
    city VARCHAR(50),
    state VARCHAR(50),
    type CHAR(1),
    cluster INT
);

CREATE TABLE oil (
    date DATE PRIMARY KEY,
    dcoilwtico FLOAT
);

CREATE TABLE holidays (
    date DATE,
    type VARCHAR(30),
    locale VARCHAR(20),
    locale_name VARCHAR(50),
    description VARCHAR(100),
    transferred BOOLEAN
);

CREATE TABLE transactions (
    date DATE,
    store_nbr INT,
    transactions INT
);

CREATE TABLE sales (
    id BIGINT PRIMARY KEY,
    date DATE,
    store_nbr INT,
    family VARCHAR(100),
    sales FLOAT,
    onpromotion INT
);
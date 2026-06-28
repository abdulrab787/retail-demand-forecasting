CREATE OR REPLACE VIEW daily_sales AS
SELECT
    date,
    SUM(sales) AS total_sales
FROM sales
GROUP BY date
ORDER BY date;

CREATE OR REPLACE VIEW daily_sales AS
SELECT
    date,
    SUM(sales) AS total_sales
FROM sales
GROUP BY date
ORDER BY date;

CREATE OR REPLACE VIEW store_sales AS
SELECT
    store_nbr,
    SUM(sales) AS revenue
FROM sales
GROUP BY store_nbr
ORDER BY revenue DESC;

CREATE OR REPLACE VIEW daily_transactions AS
SELECT
    date,
    SUM(transactions) AS total_transactions
FROM transactions
GROUP BY date
ORDER BY date;

CREATE OR REPLACE VIEW store_transactions AS
SELECT
    store_nbr,
    SUM(transactions) AS total_transactions
FROM transactions
GROUP BY store_nbr
ORDER BY total_transactions DESC;

CREATE OR REPLACE VIEW family_sales AS
SELECT
    family,
    SUM(sales) AS total_sales
FROM sales
GROUP BY family
ORDER BY total_sales DESC;

CREATE OR REPLACE VIEW promotion_effect AS
SELECT
    date,
    SUM(onpromotion) AS total_promotions,
    SUM(sales) AS total_sales
FROM sales
GROUP BY date
ORDER BY date;

CREATE OR REPLACE VIEW holiday_sales AS
SELECT
    s.date,
    h.type AS holiday_type,
    SUM(s.sales) AS total_sales
FROM sales s
JOIN holidays h
    ON s.date = h.date
GROUP BY s.date, h.type
ORDER BY s.date;

CREATE OR REPLACE VIEW oil_sales AS
SELECT
    s.date,
    o.dcoilwtico,
    SUM(s.sales) AS total_sales
FROM sales s
JOIN oil o
    ON s.date = o.date
GROUP BY s.date, o.dcoilwtico
ORDER BY s.date;

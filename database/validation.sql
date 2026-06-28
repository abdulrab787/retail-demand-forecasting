SELECT COUNT(*) AS total_sales FROM sales;
SELECT COUNT(*) AS total_stores FROM stores;
SELECT COUNT(*) AS total_transactions FROM transactions;
SELECT COUNT(*) AS total_holidays FROM holidays;
SELECT COUNT(*) AS total_oil FROM oil;

SELECT MIN(date) AS min_date, MAX(date) AS max_date
FROM sales;

SELECT MIN(date), MAX(date)
FROM transactions;

SELECT MIN(date), MAX(date)
FROM oil;

SELECT MIN(date), MAX(date)
FROM holidays;

SELECT *
FROM sales
WHERE sales IS NULL;

SELECT *
FROM sales
WHERE store_nbr IS NULL;

SELECT *
FROM sales
WHERE family IS NULL;

SELECT *
FROM oil
WHERE dcoilwtico IS NULL;

SELECT COUNT(DISTINCT store_nbr) FROM sales;

SELECT COUNT(DISTINCT family) FROM sales;

SELECT date, SUM(sales) AS total_sales
FROM sales
GROUP BY date
ORDER BY date
LIMIT 10;

SELECT date, SUM(sales) AS total_sales
FROM sales
GROUP BY date
ORDER BY date
LIMIT 10;

SELECT COUNT(*) FROM transactions;
SELECT COUNT(DISTINCT store_nbr) FROM transactions;
SELECT COUNT(DISTINCT date) FROM transactions;


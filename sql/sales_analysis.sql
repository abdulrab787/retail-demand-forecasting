SELECT
date,
SUM(sales) AS revenue
FROM sales
GROUP BY date
ORDER BY date;

SELECT
store_nbr,
SUM(sales) AS revenue
FROM sales
GROUP BY store_nbr
ORDER BY revenue DESC
LIMIT 10;

SELECT
family,
SUM(sales) AS revenue
FROM sales
GROUP BY family
ORDER BY revenue DESC;

SELECT
family,
SUM(sales) AS revenue
FROM sales
GROUP BY family
ORDER BY revenue DESC;

SELECT
AVG(sales)
FROM sales;

SELECT
CASE
    WHEN onpromotion > 0 THEN 'Promotion'
    ELSE 'No Promotion'
END AS promotion_status,
AVG(sales) AS avg_sales
FROM sales
GROUP BY promotion_status;
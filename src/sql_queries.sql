-- 1. Retrieve the top 5 customers who have purchased the most books by total quantity over the last year.
SELECT C.customer_id, C.name, SUM(OD.quantity) AS total_books_purchased
FROM Customers C
JOIN Orders O ON C.customer_id = O.customer_id
JOIN OrderDetails OD ON O.order_id = OD.order_id
WHERE O.order_date >= NOW() - INTERVAL 1 YEAR
GROUP BY C.customer_id, C.name
ORDER BY total_books_purchased DESC
LIMIT 5;

-- 2. Calculate the total revenue generated from book sales by each author.
SELECT B.author, SUM(B.price * OD.quantity) AS total_revenue
FROM Books B
JOIN OrderDetails OD ON B.book_id = OD.book_id
GROUP BY B.author
ORDER BY total_revenue DESC;

-- 3. Retrieve all books that have been ordered more than 10 times, along with the total quantity ordered for each book.
SELECT B.book_id, B.title, SUM(OD.quantity) AS total_quantity_ordered
FROM Books B
JOIN OrderDetails OD ON B.book_id = OD.book_id
GROUP BY B.book_id, B.title
HAVING SUM(OD.quantity) > 10
ORDER BY total_quantity_ordered DESC;
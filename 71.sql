-- Recyclable and Low Fat Products
-- Write an SQL query to find the ids of products that are both low fat and recyclable. Return the result table in any order.

SELECT product_id FROM Products WHERE low_fats='Y' AND recyclable='Y';

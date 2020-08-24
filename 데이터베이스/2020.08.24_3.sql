-- Q.도쿄에위치한공급자(Supplier)가생산한상품목록조회:
-- 도시명(City),공급자명(SupplierName),상품명(ProductName),상품가격(Price)
-- Table-Suppliers,Products

SELECT suppliers.city, suppliers.SupplierName, products.ProductName, products.Price
FROM suppliers , products
WHERE suppliers.city = 'Tokyo';

-- Q.분류(Categories)가Seafood인상품명(ProductName):
-- 분류명(CategoryName),상품명(ProductName)
-- Table-Categories,Products

SELECT categories.CategoryName, products.ProductName
FROM categories, products
WHERE categories.CategoryName = 'Seafood';

-- Q.공급자(Supplier)가공급한상품의공급자국가(Country)별로상품카테고리(ProductName)의상품건수와평균가격:
-- 국가명(Country),카테고리명(ProductName),상품건수,평균가격(3개테이블조인)
-- Table-Suppliers,Products,Categories

SELECT suppliers.Country, COUNT(products.ProductName) as CNT, AVG(products.price) 
FROM suppliers, products, categories
WHERE suppliers.SupplierID = products.SupplierID AND categories.CategoryID = products.CategoryID
GROUP BY suppliers.Country
ORDER BY CNT;


-- Q.주문별주문자명(CustomerName),직원명(LastName),배송자명(ShipperName),주문상세갯수:
-- 주문아이디(OrderID),주문자명(CustomerName),직원명(LastName),배송자명(ShipperName),주문상세갯수
-- Table-Orders,Order_Details,Customers(고객,주문자),Employees(직원),Shippers(배송자)

SELECT o.orderID, c.CustomerName, e.LastName, s.ShipperName, count(*)
  FROM orders o, order_details od, customers c, employees e, shippers s
 WHERE o.OrderID = od.OrderID
 AND o.CustomerID = c.CustomerID
 AND o.EmployeeID = e.EmployeeID
 AND o.ShipperID = s.ShipperID
 GROUP BY o.orderID
;


-- Q.판매량(Quantity)상위TOP3공급자(supplier)목록:
-- 공급자명(SupplierName),판매량(Quantity)
-- Table-Suppliers,Products,Order_Details

SELECT  SUM(od.Quantity) as '판매량', s.SupplierName
FROM suppliers s , products p , order_details od
WHERE od.ProductID = p.ProductID 
AND p.SupplierID = s.SupplierID
GROUP BY s.SupplierName
ORDER BY '판매량' DESC
LIMIT 3

-- Q.상품분류(Category)별,고객지역별(City)판매량(Quantity)많은순으로정렬:
-- 카테고리명(CategoryName),고객지역명(City),판매량(Quantity)
-- Table-Order,Order_Details,Customers,Categories,Products

SELECT ct.CategoryName ,SUM(od.Quantity) as '판매량'
FROM orders o, order_details od, customers c, categories ct, products p
WHERE o.orderID = od.orderID
	AND o.customerID = c.customerID
    AND od.productID = p.productID
    AND ct.CategoryID = p.CategoryID
GROUP BY ct.CategoryNAME
ORDER BY '판매량' DESC



































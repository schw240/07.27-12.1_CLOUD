SELECT suppliers.City, suppliers.SupplierName , products.ProductName, products.Price
FROM suppliers
INNER JOIN products 
	ON suppliers.SupplierID = products.SupplierID
WHERE suppliers.City = 'Tokyo'

SELECT c.CategoryName, p.ProductName
FROM categories c
INNER JOIN products p
	ON c.CategoryID = p.CategoryID
WHERE c.CategoryName = 'Seafood'

SELECT
FROM suppliers s
INNER JOIN products p
	ON 
 

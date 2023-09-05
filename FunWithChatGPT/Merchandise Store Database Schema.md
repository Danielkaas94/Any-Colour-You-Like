Creating a database schema for an online merchandise store involves several tables to store information about products, customers, orders, and more. Here's a simplified schema that you can use as a starting point:

1. **Products Table:**
   - ProductID (Primary Key)
   - ProductName
   - Description
   - Price
   - StockQuantity
   - CategoryID (Foreign Key referencing Categories table)
   - VendorID (Foreign Key referencing Vendors table)
   - ImageURL (for product images)
   
2. **Categories Table:**
   - CategoryID (Primary Key)
   - CategoryName

3. **Vendors Table:**
   - VendorID (Primary Key)
   - VendorName
   - ContactInfo
   - Location

4. **Customers Table:**
   - CustomerID (Primary Key)
   - FirstName
   - LastName
   - Email
   - Password (hashed and salted)
   - Address
   - Phone

5. **Orders Table:**
   - OrderID (Primary Key)
   - CustomerID (Foreign Key referencing Customers table)
   - OrderDate
   - TotalAmount

6. **OrderItems Table:**
   - OrderItemID (Primary Key)
   - OrderID (Foreign Key referencing Orders table)
   - ProductID (Foreign Key referencing Products table)
   - Quantity
   - Subtotal

7. **Reviews Table:**
   - ReviewID (Primary Key)
   - ProductID (Foreign Key referencing Products table)
   - CustomerID (Foreign Key referencing Customers table)
   - Rating
   - Comment
   - ReviewDate

8. **Cart Table:**
   - CartID (Primary Key)
   - CustomerID (Foreign Key referencing Customers table)

9. **CartItems Table:**
   - CartItemID (Primary Key)
   - CartID (Foreign Key referencing Cart table)
   - ProductID (Foreign Key referencing Products table)
   - Quantity

This schema should provide a foundation for your online merchandise store. You can expand or modify it based on your specific requirements. Ensure to establish proper relationships between tables, enforce referential integrity, and consider indexing for performance optimization as your database grows. Additionally, implement security measures to protect customer data, especially passwords, using encryption and hashing techniques.
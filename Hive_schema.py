from table_creation import create_table
from Data_load import Load_data
try:
    create_table('Categories', 'CategoryID int,CategoryName string')
    create_table('Cities', 'CityID int,CityName string,Zipcode int,CountryID int')
    create_table('Countries', 'CountryID int,CountryName string,CountryCode string')
    create_table('Customers','CustomerID int,FirstName string,MiddleInitial string,LastName string,CityID int,Address string')
    create_table('Employees','EmployeeID int,FirstName string,MiddleInitial string,LastName string,BirthDate timestamp,Gender string,CityID int,HireDate timestamp')
    create_table('Products','ProductID int,ProductName string,Price int,CategoryID int,Class string,ModifyDate timestamp,Resistant string,IsAllergic string,VitalityDays int')
    create_table('Sales','SalesID int,SalesPersonID int,CustomerID int,ProductID int,Quantity int,Discount float,TotalPrice float,SalesDate timestamp,TransactionNumber string')
    Load_data('categories.csv', 'categories')
    Load_data('cities.csv', 'cities')
    Load_data('countries.csv', 'countries')
    Load_data('customers.csv', 'customers')
    Load_data('employees.csv', 'employees')
    Load_data('products.csv', 'products')
    Load_data('sales.csv', 'sales')
except Exception as e:
    print('Error in hive Schema: ',e)
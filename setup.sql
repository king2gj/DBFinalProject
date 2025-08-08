-- SET UP TABLES --
CREATE TABLE Locations (
    loc_id INT AUTO_INCREMENT PRIMARY KEY,
    loc_name VARCHAR(100),
    loc_street VARCHAR(50),
    loc_city VARCHAR(50),
    loc_state VARCHAR(2),
    loc_zip INT
);

CREATE TABLE Employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    emp_street VARCHAR(50),
    emp_city VARCHAR(50),
    emp_state VARCHAR(2),
    emp_zip INT,
    emp_payrate INT,
    emp_payperiod ENUM ("hourly", "annually"),
    emp_location INT,
    FOREIGN KEY (emp_location) REFERENCES Locations(loc_id)
);

CREATE TABLE EmployeePhoneNumbers (
    emp_id INT,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
    phone_number VARCHAR(15),
    PRIMARY KEY (emp_id, phone_number)
);

CREATE TABLE Products (
    prod_id INT AUTO_INCREMENT PRIMARY KEY,
    prod_name VARCHAR(100),
    prod_manufacturer VARCHAR(100),
    prod_msrp DECIMAL(7, 2)
);

CREATE TABLE Stocks (
    loc_id INT,
    FOREIGN KEY (loc_id) REFERENCES Locations(loc_id),
    prod_id INT,
    FOREIGN KEY (prod_id) REFERENCES Products(prod_id),
    price DECIMAL(7, 2),
    quantity INT,
    PRIMARY KEY (loc_id, prod_id)
);

-- FILL LOCATIONS --
INSERT INTO Locations (loc_name, loc_street, loc_city, loc_state, loc_zip)
VALUES ("Corry Kroger", "1 W Corry St", "Cincinnati", "OH", 45219);

INSERT INTO Locations (loc_name, loc_street, loc_city, loc_state, loc_zip)
VALUES ("Food 4 Less", "1820 W Slauson Ave", "Los Angeles", "CA", 90047);

-- FILL EMPLOYEES --
INSERT INTO Employees (emp_name, emp_street, emp_city, emp_state, emp_zip, emp_payrate, emp_payperiod, emp_location)
VALUES ("Nate Knot", "1234 Placeholder Ave", "Los Angeles", "CA", 90045, 25, "hourly", 2);

INSERT INTO Employees (emp_name, emp_street, emp_city, emp_state, emp_zip, emp_payrate, emp_payperiod, emp_location)
VALUES ("Gwynn Pitz", "555 Fives Ave", "Cincinnati", "OH", 45221, 50000, "annually", 1);

-- FILL EMPLOYEE PHONE NUMBERS --
INSERT INTO EmployeePhoneNumbers (emp_id, phone_number)
VALUES (1, "3235550000");

INSERT INTO EmployeePhoneNumbers (emp_id, phone_number)
VALUES (2, "5135550000");

INSERT INTO EmployeePhoneNumbers (emp_id, phone_number)
VALUES (2, "6145550000");

-- FILL PRODUCTS --
INSERT INTO Products (prod_name, prod_manufacturer, prod_msrp)
VALUES ("Laundry Detergent", "Laundry Company", 19.99);

INSERT INTO Products (prod_name, prod_manufacturer, prod_msrp)
VALUES ("Loaf of bread", "Bakery", 4.99);

INSERT INTO Products (prod_name, prod_manufacturer, prod_msrp)
VALUES ("Gallon of milk", "Farm", 3.99);

-- FILL STOCKS --
INSERT INTO Stocks (loc_id, prod_id, price, quantity)
VALUES (1, 1, 24.99, 300);

INSERT INTO Stocks (loc_id, prod_id, price, quantity)
VALUES (1, 2, 4.99, 500);

INSERT INTO Stocks (loc_id, prod_id, price, quantity)
VALUES (1, 3, 4.99, 1000);

INSERT INTO Stocks (loc_id, prod_id, price, quantity)
VALUES (2, 2, 5.99, 600);

INSERT INTO Stocks (loc_id, prod_id, price, quantity)
VALUES (2, 3, 3.99, 300);
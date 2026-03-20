from sqlite3 import Cursor

import mysql.connector

con = mysql.connector.connect(
    user = "root",
    password = "#$Kp100%",
    host = "localhost",
    port = 3306
)

if con.is_connected():
    print("connected")

cur = con.cursor()
cur.execute("SHOW DATABASES")
for x in cur:
    print(x)
print("\n")

cur.execute("USE GIET")
for x in cur:
    print(x)
print("\n")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#$Kp100%",   
    database="giet"    
)

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#$Kp100%",
    database="giet"   
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS giet (
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    address VARCHAR(50),
    gender CHAR(1),
    designation VARCHAR(50),
    salary INT
)
""")

cursor.execute("SHOW TABLES")
for table in cursor.fetchall():
    print(table)


    import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#$Kp100%",
    database="giet"
)

cursor = conn.cursor()

# Function to run queries
def run_query(title, query):
    print(f"\n--- {title} ---")
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

# 1
run_query("1. All Data", "SELECT * FROM giet")

# 2
run_query("2. Only Name", "SELECT name FROM giet")

# 3
run_query("3. Name and Address", "SELECT name, address FROM giet")

# 4
run_query("4. Roll and Salary", "SELECT roll, salary FROM giet")

# 5
run_query("5. Name = aman", "SELECT * FROM giet WHERE name='aman'")

# 6
run_query("6. Address = delhi", "SELECT * FROM giet WHERE address='delhi'")

# 7
run_query("7. Gender = M", "SELECT * FROM giet WHERE gender='M'")

# 8
run_query("8. Designation = doctor", "SELECT * FROM giet WHERE designation='doctor'")

# 9
run_query("9. Salary = 15000", "SELECT * FROM giet WHERE salary=15000")

# 10
run_query("10. Salary > 20000", "SELECT * FROM giet WHERE salary>20000")

# 11
run_query("11. Salary < 30000", "SELECT * FROM giet WHERE salary<30000")

# 12
run_query("12. Male AND Salary > 20000",
          "SELECT * FROM giet WHERE gender='M' AND salary>20000")

# 13
run_query("13. Female OR Address = raipur",
          "SELECT * FROM giet WHERE gender='F' OR address='raipur'")

# 14
run_query("14. Name starts with 'a'",
          "SELECT * FROM giet WHERE name LIKE 'a%'")

# 15
run_query("15. Name ends with 'h'",
          "SELECT * FROM giet WHERE name LIKE '%h'")

# 16
run_query("16. Address contains 'pur'",
          "SELECT * FROM giet WHERE address LIKE '%pur%'")

# 17
run_query("17. Sort by Name ASC",
          "SELECT * FROM giet ORDER BY name ASC")

# 18
run_query("18. Sort by Salary DESC",
          "SELECT * FROM giet ORDER BY salary DESC")

# 19
run_query("19. Total Employees",
          "SELECT COUNT(*) FROM giet")

# 20
run_query("20. Male Employees Count",
          "SELECT COUNT(*) FROM giet WHERE gender='M'")
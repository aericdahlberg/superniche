
cursor.execute("SELECT * FROM employees WHERE department = %s", ("HR",))
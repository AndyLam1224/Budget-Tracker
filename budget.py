import sqlite3
from expense import Expense

# :memory: starts from scratch, stores in ram- good for testing 
conn = sqlite3.connect('expenses.db')

# c for connection
c = conn.cursor()

c.execute("""CREATE TABLE expenses (
			Name text,
			Category text,
			Cost integer
			)""")

expense_1 = Expense('Raleigh','Housing',300)
c.execute("INSERT INTO expenses VALUES (?,?,?)",(expense_1.name,expense_1.category,expense_1.cost))

conn.commit()
c.execute("SELECT * FROM expenses WHERE Category = ?",('Housing',))
print(c.fetchall())

conn.close()
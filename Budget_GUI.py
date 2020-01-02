from tkinter import *
from tkinter.ttk import *
from analysis import analyze
import datetime
import sqlite3
d = datetime.datetime.today()
month = d.month
# :memory: starts from scratch, stores in ram- good for testing 
conn = sqlite3.connect('expenses11.db')

# c for connection
c = conn.cursor()
# Create expenses table
c.execute("""CREATE TABLE IF NOT EXISTS expenses(
			Name text,
			Category text,
			Cost integer,
			Month text
			)""")
# Updates input into database
def update():
	c.execute("INSERT INTO expenses VALUES (?,?,?,?)",
		(printEntry1.get(),tkvar.get(),printEntry3.get(),month))
	

# Display data from database onto gui
def display():
	c.execute("SELECT * FROM expenses")
	for item in c.fetchall():
		listBox.insert("", "end",values=item)
		
categories = ['Business','Vacation','Food/Drink','Gas','Clothes','Bills','Other']
root = Tk()
root.title('Budget Tracker')
tkvar = StringVar(root)

label1 = Label(root,text='Name').grid(row=1,column=1)
label2 = Label(root,text='Category').grid(row=1,column=2)
label3 = Label(root,text='Cost').grid(row=1,column=3)

printEntry1 = Entry(root)
printEntry1.grid(row=2,column=1)

printEntry2 = OptionMenu(root,tkvar,*categories)
printEntry2.grid(row=2,column=2)

printEntry3 = Entry(root)
printEntry3.grid(row=2,column=3)

# Create treeview with 3 columns
cols = ('Name','Category','Cost','Date')
listBox = Treeview(root,columns=cols,show='headings')
# Set column headings
for col in cols:
    listBox.heading(col, text=col)  
listBox.grid(row=0,column=0,columnspan=4)

printButton = Button(root,text = "Update",command = update).grid(row=3,column=1)
quitButton = Button(root, text = "Quit", command = root.quit).grid(row=3,column=4)
displayButton = Button(root, text = "Display", command = display).grid(row=3,column=2,)
anaylzeButton = Button(root, text = "Analyze", command = analyze).grid(row=3,column=3)

conn.commit()
conn.close()
root.mainloop()


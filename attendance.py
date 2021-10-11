from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import csv
from tkinter import filedialog

mydata = []
class Attendance_data:
	def __init__(self, root):
		self.win = root
		self.canvas = Canvas(self.win, width=1400, height=440, bg='white')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 1400/2)
		y = int(height/2 - 540/2)
		self.win.geometry("1400x440+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Attendance")

	def add_frame6(self):
		self.framel = LabelFrame(self.win, bd = 2, bg = "white", relief = 'ridge', text = 'Attendance Details', font = ("times now roman", 12, "bold"))
		self.framel.place(x = 10, y = 10, width = 690, height = 264)

		#-----Details-----

		self.details = Frame(self.framel, bd = 2, bg = 'white', relief = 'ridge')
		self.details.place(x = 0, y = 5, width = 688, height = 200)

		self.attendance_id = Label(self.details, bg =  "white", text = 'ID: ', font = ("times now roman", 12, "bold"))
		self.attendance_id.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'W')
		self.attendance_id_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_id_entry.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'W')

		self.attendance_roll = Label(self.details, bg =  "white", text = 'Roll No: ', font = ("times now roman", 12, "bold"))
		self.attendance_roll.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = 'W')
		self.attendance_roll_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_roll_entry.grid(row = 0, column = 3, padx = 10, pady = 10, sticky = 'W')

		self.attendance_name = Label(self.details, bg =  "white", text = 'Name: ', font = ("times now roman", 12, "bold"))
		self.attendance_name.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'W')
		self.attendance_name_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_name_entry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = 'W')

		self.attendance_department = Label(self.details, bg =  "white", text = 'Department: ', font = ("times now roman", 12, "bold"))
		self.attendance_department.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = 'W')
		self.attendance_department_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_department_entry.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = 'W')

		self.attendance_time = Label(self.details, bg =  "white", text = 'Time: ', font = ("times now roman", 12, "bold"))
		self.attendance_time.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'W')
		self.attendance_time_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_time_entry.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = 'W')

		self.attendance_date = Label(self.details, bg =  "white", text = 'Date: ', font = ("times now roman", 12, "bold"))
		self.attendance_date.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = 'W')
		self.attendance_date_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_date_entry.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = 'W')

		self.attendance_status = Label(self.details, bg =  "white", text = 'Status: ', font = ("times now roman", 12, "bold"))
		self.attendance_status.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = 'W')
		self.attendance_status_entry = ttk.Entry(self.details, font = ("times now roman", 12, "bold"), width = 20)
		self.attendance_status_entry.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = 'W')
		#-----Buttons-----

		self.buttonFrame = Frame(self.framel, bd = 2, bg = 'white', relief = 'ridge')
		self.buttonFrame.place(x = 0, y = 205, width = 688, height = 37)

		self.exportcsv = Button(self.buttonFrame, width = 16, text = "Export CSV", font = ("times now roman", 12, "bold"), bg = 'blue', fg = 'white', command = self.exportCsv)
		self.exportcsv.grid(row = 0, column = 0)

		self.importcsv = Button(self.buttonFrame, width = 16, text = "Import CSV", font = ("times now roman", 12, "bold"), bg = 'blue', fg = 'white', command = self.importCsv)
		self.importcsv.grid(row = 0, column = 1)

		self.updatecsv = Button(self.buttonFrame, width = 16, text = "Update", font = ("times now roman", 12, "bold"), bg = 'blue', fg = 'white')
		self.updatecsv.grid(row = 0, column = 2)

		self.resetcsv = Button(self.buttonFrame, width = 17, text = "Reset", font = ("times now roman", 12, "bold"), bg = 'blue', fg = 'white')
		self.resetcsv.grid(row = 0, column = 3)

		self.framer = LabelFrame(self.win, bd = 2, bg = "white", relief = 'ridge', text = 'Attendance Stored', font = ("times now roman", 12, "bold"))
		self.framer.place(x = 700, y = 10, width = 690, height = 420)

		#-----TextField-----

		self.text_frame = Frame(self.framer, bd = 2, bg = "white", relief = 'ridge')
		self.text_frame.place(x = 0, y = 5, width = 688, height = 393)

		self.scrollx = ttk.Scrollbar(self.text_frame, orient = HORIZONTAL)
		self.scrolly = ttk.Scrollbar(self.text_frame, orient = VERTICAL)

		self.attendance_table = ttk.Treeview(self.text_frame, column = ("id", "roll", "name", "department", "time", "date"), xscrollcommand = self.scrollx.set, yscrollcommand = self.scrolly.set)

		self.scrollx.pack(side = BOTTOM, fill = X)
		self.scrolly.pack(side = RIGHT, fill = Y)
		self.scrollx.config(command = self.attendance_table.xview)
		self.scrolly.config(command = self.attendance_table.yview)

		self.attendance_table.heading("id", text = "ID")
		self.attendance_table.heading("roll", text = "Roll No")
		self.attendance_table.heading("name", text = "Name")
		self.attendance_table.heading("department", text = "Department")
		self.attendance_table.heading("time", text = "Time")
		self.attendance_table.heading("date", text = "Date")
		self.attendance_table['show'] = 'headings'

		self.attendance_table.column('id', width = 100)
		self.attendance_table.column('roll', width = 100)
		self.attendance_table.column('name', width = 200)
		self.attendance_table.column('department', width = 100)
		self.attendance_table.column('time', width = 100)
		self.attendance_table.column('date', width = 100)

		self.attendance_table.pack(fill = BOTH, expand = 1)

		self.win.mainloop()

	def fetchData(self, rows):
		self.attendance_table.delete(*self.attendance_table.get_children())
		for i in rows:
			self.attendance_table.insert("", END, values = i)

	def importCsv(self):
		global mydata
		fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Open csv', filetypes = (("CSV", "*.csv"), ("All Files", "*.*")), parent = self.win)
		with open(fln) as myfile:
			csvread = csv.reader(myfile, delimiter = ",")
			for i in csvread:
				mydata.append(i)
			self.fetchData(mydata)

	def exportCsv(self):
		try:
			if len(mydata) < 1:
				messagebox.showerror("No Data", "No Data founf to export!", parent = self.win)
				return False
			fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = 'Open csv', filetypes = (("CSV", "*.csv"), ("All Files", "*.*")), parent = self.win)
			with open(fln, mode = 'w', newline = "") as myfile:
				exp_write = csv.writer(myfile, delimiter = ",")
				for i in mydata:
					exp_write.writerow(i)
				messagebox.showinfo("Data Export!", "Your data has been exported to" + os.path.basename(fln) + "successfully", parent = self.win)
		except Exception as es:
			messagebox.showerror("Error!",f"Due to :{str(es)}", parent = self.win)

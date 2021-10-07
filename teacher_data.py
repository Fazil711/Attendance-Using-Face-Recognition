from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

countries = []


world = open("countires_name.txt")
for count in world:
	count = count.rstrip('\n')
	countries.append(count)
tupp = tuple(countries)
tupp = ("",) + tupp

class Teacher_data:
	def __init__(self, root):
		self.win = root
		self.canvas = Canvas(self.win, width=1000, height=440, bg='white')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 1000/2)
		y = int(height/2 - 540/2)
		self.win.geometry("1000x440+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Students")

		self.var_age = StringVar()
		self.var_country = StringVar()
		self.var_address = StringVar()
		self.var_phone = StringVar()
		self.var_id = StringVar()
		self.var_name = StringVar()
		self.var_email = StringVar()
		self.var_password = StringVar()
		
	def add_frame4(self):
		#-----Left-----
		self.framel = LabelFrame(self.win, bd = 2, bg = "white", relief = 'ridge', text = 'Teacher Details', font = ("times now roman", 12, "bold"))
		self.framel.place(x = 10, y = 10, width = 400, height = 411)

		self.teacher_info = LabelFrame(self.framel, bd = 2, bg = "white", relief = 'ridge', text = 'Information', font = ("times now roman", 12, "bold"))
		self.teacher_info.place(x = 0, y = 0, width = 400, height = 320)

		self.label_name = Label(self.teacher_info, bg =  "white", text = 'Name: ', font = ("times now roman", 12, "bold"))
		self.label_name.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.name_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_name)
		self.name_entry.grid(row = 0, column = 1, padx = 10, pady = 5)

		self.label_age = Label(self.teacher_info, bg =  "white", text = 'Age: ', font = ("times now roman", 12, "bold"))
		self.label_age.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.age_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_age)
		self.age_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

		self.label_email = Label(self.teacher_info, bg =  "white", text = 'Email: ', font = ("times now roman", 12, "bold"))
		self.label_email.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.email_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_email)
		self.email_entry.grid(row = 3, column = 1, padx = 10, pady = 5)

		self.label_country = Label(self.teacher_info, bg =  "white", text = 'Country: ', font = ("times now roman", 12, "bold"))
		self.label_country.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = 'W')
		#self.country_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20)
		#self.country_entry.grid(row = 4, column = 1, padx = 10, pady = 5)
		self.country_entry = ttk.Combobox(self.teacher_info, font = ("times now roman", 12, "bold"), width = 18, state = 'readonly', textvariable = self.var_country)
		self.country_entry['values'] = tupp
		self.country_entry.current(0)
		self.country_entry.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = 'W')

		self.label_id = Label(self.teacher_info, bg =  "white", text = 'ID: ', font = ("times now roman", 12, "bold"))
		self.label_id.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.id_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_id)
		self.id_entry.grid(row = 5, column = 1, padx = 10, pady = 5)

		self.label_phone = Label(self.teacher_info, bg =  "white", text = 'Phone: ', font = ("times now roman", 12, "bold"))
		self.label_phone.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.phone_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_phone)
		self.phone_entry.grid(row = 6, column = 1, padx = 10, pady = 5)

		self.label_addr = Label(self.teacher_info, bg =  "white", text = 'Address: ', font = ("times now roman", 12, "bold"))
		self.label_addr.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.addr_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_address)
		self.addr_entry.grid(row = 7, column = 1, padx = 10, pady = 5)

		self.label_pass = Label(self.teacher_info, bg =  "white", text = 'Password: ', font = ("times now roman", 12, "bold"))
		self.label_pass.grid(row = 8, column = 0, padx = 10, pady = 5, sticky = 'W')
		self.pass_entry = ttk.Entry(self.teacher_info, font = ("times now roman", 12, "bold"), width = 20, textvariable = self.var_password)
		self.pass_entry.grid(row = 8, column = 1, padx = 10, pady = 5)

		#-----buttons-----
		self.button_frame = Frame(self.framel, bd = 2, bg = "white", relief = 'ridge')
		self.button_frame.place(x = 0, y = 320, width = 400, height = 70)

		self.button_update = Button(self.button_frame, width = 12, text = "Update", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.update_data1)
		self.button_update.grid(row = 0, column = 0)

		self.button_reset = Button(self.button_frame, width = 12, text = "Reset", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.reset_data)
		self.button_reset.grid(row = 0, column = 1)

		self.button_delete = Button(self.button_frame, width = 13, text = "Delete", font = ("times now roman", 12, "bold"), fg = "white", bg = "red", command = self.delete_data1)
		self.button_delete.grid(row = 0, column = 2)

		self.button_save = Button(self.button_frame, width = 39, text = "Save", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.add_data1)
		self.button_save.grid(row = 1, column = 0, columnspan = 3)


		#-----Right-----
		self.framer = LabelFrame(self.win, bd = 2, bg = "white", relief = 'ridge', text = 'Teacher Details', font = ("times now roman", 12, "bold"))
		self.framer.place(x = 410, y = 10, width = 580, height = 411)

		self.search_teacher = LabelFrame(self.framer, bd = 2, bg = 'white', relief = 'ridge', text = 'Search Teachers', font = ("times now roman", 12, "bold"))
		self.search_teacher.place(x = 5, y = 5, width = 570, height = 70)

		#-----search-----
		self.search_by = Label(self.search_teacher, text = 'Search By', font = ("times now roman", 12, "bold"), bg = "red", fg = 'white', width = 8)
		self.search_by.grid(row = 0, column = 0, padx = (10, 0), pady = 5, sticky = 'W')

		self.search_box = ttk.Combobox(self.search_teacher, font = ("times now roman", 12, "bold"), width = 11, state = 'readonly')
		self.search_box['values'] =('Select', 'ID', 'Phone')
		self.search_box.current(0)
		self.search_box.grid(row = 0, column = 1, pady = 5)

		self.search_para = ttk.Entry(self.search_teacher, font = ("times now roman", 12, "bold"), width = 12)
		self.search_para.grid(row = 0, column = 2, padx = (0,10), pady = 5)

		self.search_button = Button(self.search_teacher, width = 10, text = "Search", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue")
		self.search_button.grid(row = 0, column = 3, pady = 5)

		self.show_button = Button(self.search_teacher, width = 10, text = "Show All", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue")
		self.show_button.grid(row = 0, column = 4, pady = 5)

		#-----Text Field-----
		self.text_frame = Frame(self.framer, bd = 2, bg = "white", relief = 'ridge')
		self.text_frame.place(x = 5, y = 75, width = 570, height = 314)

		self.scrollx = ttk.Scrollbar(self.text_frame, orient = HORIZONTAL)
		self.scrolly = ttk.Scrollbar(self.text_frame, orient = VERTICAL)

		self.teacher_table = ttk.Treeview(self.text_frame, column = ("name", "email", "age", "roll no", "phone", "address", "country", "password"), xscrollcommand = self.scrollx.set, yscrollcommand = self.scrolly.set)

		self.scrollx.pack(side = BOTTOM, fill = X)
		self.scrolly.pack(side = RIGHT, fill = Y)
		self.scrollx.config(command = self.teacher_table.xview)
		self.scrolly.config(command = self.teacher_table.yview)

		self.teacher_table.heading("name", text = "Name")
		self.teacher_table.heading("email", text = "E-mail")
		self.teacher_table.heading("age", text = "Age")
		self.teacher_table.heading("roll no", text = "Roll no")
		self.teacher_table.heading("phone", text = "Phone")
		self.teacher_table.heading("address", text = "Address")
		self.teacher_table.heading("country", text = "Country")
		self.teacher_table.heading("password", text = "Password")
		self.teacher_table['show'] = 'headings'

		self.teacher_table.column('name', width = 150)
		self.teacher_table.column('email', width = 200)
		self.teacher_table.column('age', width = 100)
		self.teacher_table.column('roll no', width = 100)
		self.teacher_table.column('phone', width = 100)
		self.teacher_table.column('address', width = 100)
		self.teacher_table.column('country', width = 100)
		self.teacher_table.column('password', width = 100)

		self.teacher_table.pack(fill = BOTH, expand = 1)
		self.teacher_table.bind("<ButtonRelease>", self.get_cursor1)
		self.fetch_data1()
		self.win.mainloop()

	def add_data1(self):
		if self.var_id.get() == "" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_country.get() == "" or self.var_address.get() == "" or self.var_age.get() == "" or self.var_password.get() == "":
			messagebox.showerror("Error!","All fields are requires", parent = self.win)
		else:
			try:
				conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
				mycursor = conn.cursor()
				mycursor.execute('INSERT INTO registeration VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(
																								self.var_name.get(),
																								self.var_email.get(),
																								self.var_age.get(),
																								self.var_id.get(),
																								self.var_phone.get(),																											
																								self.var_address.get(),
																								self.var_country.get(),
																								self.var_password.get(),
																								))
				conn.commit()
				self.fetch_data1()
				self.reset_data()
				conn.close()
				messagebox.showinfo("Success!","Teacher details has been added successfully", parent = self.win)
			except Exception as es:
				messagebox.showerror("Error!",f"Due to :{str(es)}", parent = self.win)

	def update_data1(self):
		if self.var_id.get() == "" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_country.get() == "" or self.var_address.get() == "" or self.var_age.get() == "" or self.var_password.get() == "":
			messagebox.showerror("Error!","All fields are requires", parent = self.win)
		else:
			try:
				update_prompt = messagebox.askyesno("Update?", "Do you want to update this teacher's details", parent = self.win)
				if update_prompt > 0:
					conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
					mycursor = conn.cursor()
					mycursor.execute('UPDATE registeration SET user_name = %s, email_id = %s, age = %s, phone_no = %s, address = %s, country = %s, passwd = %s WHERE roll_no = %s',(
																																												self.var_name.get(),
																																												self.var_email.get(),
																																												self.var_age.get(),																																											
																																												self.var_phone.get(),																											
																																												self.var_address.get(),
																																												self.var_country.get(),
																																												self.var_password.get(),
																																												self.var_id.get(),
																																												))
				else:
					if not update_prompt:
						return
				conn.commit()
				self.fetch_data1()
				self.reset_data()
				conn.close()
				messagebox.showinfo("Success","Details updated successfully", parent = self.win)
			except Exception as es:
				messagebox.showerror("Error!",f"Due to :{str(es)}", parent = self.win)


	def fetch_data1(self):
		conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
		mycursor = conn.cursor()
		mycursor.execute("SELECT * FROM registeration")
		data = mycursor.fetchall()

		if len(data) != 0:
			self.teacher_table.delete(*self.teacher_table.get_children())
			for i in data:
				self.teacher_table.insert("", END, values = i)
			conn.commit()
		conn.close()

	def get_cursor1(self, event = ""):
		cursor_focus = self.teacher_table.focus()
		content = self.teacher_table.item(cursor_focus)
		data = content['values']

		self.var_name.set(data[0]),
		self.var_email.set(data[1]),
		self.var_age.set(data[2]),
		self.var_id.set(data[3]),
		self.var_phone.set(data[4]),																											
		self.var_address.set(data[5]),
		self.var_country.set(data[6]),
		self.var_password.set(data[7]),

	def delete_data1(self):
		if self.var_id.get() == "":
			messagebox.showerror("Error", "Student ID is neccessary!", parent = self.win)
		else:
			try:
				delete = messagebox.askyesno("Delete!", "Do you want to delete the details?", parent = self.win)
				if delete > 0:
					conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
					mycursor = conn.cursor()
					#mycursor.execute("SET SQL_SAFE_UPDATES = 0;")
					mycursor.execute("DELETE FROM registeration WHERE roll_no = %s ",(self.var_id.get(),))
				else:
					if not delete:
						return
				conn.commit()
				self.fetch_data1()
				self.reset_data()
				conn.close()
				messagebox.showinfo("Deleted!", "Teacher's Details removed", parent = self.win)
			except Exception as es:
				messagebox.showerror("Error",f"Due to: {str(es)}")

	def reset_data(self):
		self.var_name.set(""),
		self.var_email.set(""),
		self.var_age.set(""),
		self.var_id.set(""),
		self.var_phone.set(""),																											
		self.var_address.set(""),
		self.var_country.set(""),
		self.var_password.set(""),
    
   

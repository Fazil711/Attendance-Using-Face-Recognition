from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Student:
	def __init__(self, win):
		self.win = win
		self.canvas = Canvas(self.win, width=1500, height=600, bg='white')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 1500/2)
		y = int(height/2 - 700/2)
		self.win.geometry("1500x600+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Students")

		#-----Variables-----
		self.var_dep = StringVar()
		self.var_course = StringVar()
		self.var_year = StringVar()
		self.var_phone = StringVar()
		self.var_semester = StringVar()
		self.var_dob = StringVar()
		self.var_teacher = StringVar()
		self.var_gender = StringVar()
		self.var_division = StringVar()
		self.var_roll = StringVar()
		self.var_address = StringVar()
		self.var_photo = StringVar()
		self.var_id = StringVar()
		self.var_name = StringVar()
		self.var_email = StringVar()
		self.var_radio1 = StringVar()
		self.var_radio2 = StringVar()

	def addframe2(self):
		#-----Left-----
		self.framel = LabelFrame(self.win, bd = 2, bg = "white", relief = 'ridge', text = 'Student Details', font = ("times now roman", 12, "bold"))
		self.framel.place(x = 20, y = 20, width = 730, height = 540)


		#-----course info-----
		self.current_course = LabelFrame(self.framel, bd = 2, bg = "white", relief = 'ridge', text = 'current course', font = ("times now roman", 12, "bold"))
		self.current_course.place(x = 5, y = 5, width = 720, height = 150)

		self.department = Label(self.current_course, text = 'Department', font = ("times now roman", 12, "bold"), bg = "white")
		self.department.grid(row = 0, column = 0, padx = 10, sticky = 'W')
		self.combo1 = ttk.Combobox(self.current_course, textvariable = self.var_dep, font = ("times now roman", 12, "bold"), width = 17, state = 'readonly')
		self.combo1['values'] =('Select', 'Comp Sci', 'IT', 'Civil', 'Mechanical', 'Electric', 'Telecom', 'Chemical')
		self.combo1.current(0)
		self.combo1.grid(row = 0, column = 1, padx = 10, pady = 10)

		self.course = Label(self.current_course, text = 'Course', font = ("times now roman", 12, "bold"), bg = "white")
		self.course.grid(row = 0, column = 2, padx = 10, sticky = 'W')
		self.combo2 = ttk.Combobox(self.current_course, textvariable = self.var_course, font = ("times now roman", 12, "bold"), width = 17, state = 'readonly')
		self.combo2['values'] =('Select', 'FE', 'SE', 'TE', 'BE')
		self.combo2.current(0)
		self.combo2.grid(row = 0, column = 3, padx = 10, pady = 10)

		self.year = Label(self.current_course, text = 'Year', font = ("times now roman", 12, "bold"), bg = "white")
		self.year.grid(row = 1, column = 0, padx = 10, sticky = 'W')
		self.combo3 = ttk.Combobox(self.current_course, textvariable = self.var_year, font = ("times now roman", 12, "bold"), width = 17, state = 'readonly')
		self.combo3['values'] =('Select', '2019-2020', '2020-2021', '2021-2022', '2022-2023')
		self.combo3.current(0)
		self.combo3.grid(row = 1, column = 1, padx = 10, pady = 10)

		self.semester = Label(self.current_course, text = 'Semester', font = ("times now roman", 12, "bold"), bg = "white")
		self.semester.grid(row = 1, column = 2, padx = 10, sticky = 'W')
		self.combo4 = ttk.Combobox(self.current_course, textvariable = self.var_semester, font = ("times now roman", 12, "bold"), width = 17, state = 'readonly')
		self.combo4['values'] =('Select', 'Sem1', 'Sem2')
		self.combo4.current(0)
		self.combo4.grid(row = 1, column = 3, padx = 10, pady = 10)


		#-----Class Info-----
		self.class_info = LabelFrame(self.framel, bd = 2, bg = "white", relief = 'ridge', text = 'Class Student Information', font = ("times now roman", 12, "bold"))
		self.class_info.place(x = 5, y = 155, width = 720, height = 240)

		#-----student-id-----
		self.student_id = Label(self.class_info, text = 'Student ID: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.student_id.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = 'W')

		self.student_entry = ttk.Entry(self.class_info, textvariable = self.var_id, font = ("times now roman", 12, "bold"), width = 20)
		self.student_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = 'W')

		#-----student name-----
		self.student_name = Label(self.class_info, text = 'Student name: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.student_name.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = 'W')

		self.student_name_entry = ttk.Entry(self.class_info, textvariable = self.var_name, font = ("times now roman", 12, "bold"), width = 20)
		self.student_name_entry.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = 'W')

		#-----class division-----
		self.class_div = Label(self.class_info, text = 'Class Division: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.class_div.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = 'W')

		#self.class_div_entry = ttk.Entry(self.class_info, textvariable = self.var_division, font = ("times now roman", 12, "bold"), width = 20)
		#self.class_div_entry.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = 'W')
		self.class_div_entry = ttk.Combobox(self.class_info, textvariable = self.var_division, font = ("times now roman", 12, "bold"), width = 18, state = 'readonly')
		self.class_div_entry['values'] =('', 'A', 'B', 'C', 'D', 'E', 'F')
		self.class_div_entry.current(0)
		self.class_div_entry.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = 'W')

		#-----rollno-----
		self.roll_no = Label(self.class_info, text = 'Roll No: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.roll_no.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = 'W')

		self.roll_no_entry = ttk.Entry(self.class_info, textvariable = self.var_roll, font = ("times now roman", 12, "bold"), width = 20)
		self.roll_no_entry.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = 'W')

		#-----Gender-----
		self.Gender = Label(self.class_info, text = 'Gender: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.Gender.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = 'W')

		#self.Gender_entry = ttk.Entry(self.class_info, textvariable = self.var_gender, font = ("times now roman", 12, "bold"), width = 20)
		#self.Gender_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = 'W')
		self.Gender_entry = ttk.Combobox(self.class_info, textvariable = self.var_gender, font = ("times now roman", 12, "bold"), width = 18, state = 'readonly')
		self.Gender_entry['values'] =('', 'Male', 'Female')
		self.Gender_entry.current(0)
		self.Gender_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = 'W')

		#-----DOB-----
		self.dob = Label(self.class_info, text = 'Date of Birth: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.dob.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = 'W')

		self.dob_entry = ttk.Entry(self.class_info, textvariable = self.var_dob, font = ("times now roman", 12, "bold"), width = 20)
		self.dob_entry.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = 'W')

		#-----email-----
		self.email_id = Label(self.class_info, text = 'Email: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.email_id.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'W')

		self.email_id_entry = ttk.Entry(self.class_info, textvariable = self.var_email, font = ("times now roman", 12, "bold"), width = 20)
		self.email_id_entry.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = 'W')

		#-----phoneno-----
		self.phone_id = Label(self.class_info, text = 'Phone no: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.phone_id.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = 'W')

		self.phone_id_entry = ttk.Entry(self.class_info, textvariable = self.var_phone, font = ("times now roman", 12, "bold"), width = 20)
		self.phone_id_entry.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = 'W')

		#-----Address-----
		self.address_id = Label(self.class_info, text = 'Address: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.address_id.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = 'W')

		self.address_id_entry = ttk.Entry(self.class_info, textvariable = self.var_address, font = ("times now roman", 12, "bold"), width = 20)
		self.address_id_entry.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = 'W')

		#-----Teacher name-----
		self.teacher_id = Label(self.class_info, text = 'Teacher: ', font = ("times now roman", 12, "bold"), bg = "white")
		self.teacher_id.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = 'W')

		self.teacher_id_entry = ttk.Entry(self.class_info, textvariable = self.var_teacher, font = ("times now roman", 12, "bold"), width = 20)
		self.teacher_id_entry.grid(row = 4, column = 3, padx = 10, pady = 5, sticky = 'W')

		#-----Radio Buttons-----
		self.radiobutton1 = ttk.Radiobutton(self.class_info, variable = self.var_radio1, text = "Take photo sample", value = 'yes')
		self.radiobutton1.grid(row = 6, column = 0)

		self.radiobutton2 = ttk.Radiobutton(self.class_info, variable = self.var_radio2, text = "No photo sample", value = 'no')
		self.radiobutton2.grid(row = 6, column = 1)

		#-----bbuttons-----
		self.bbuttons = Frame(self.framel, bd = 2, bg = "white", relief = 'ridge')
		self.bbuttons.place(x = 5, y = 395, height = 70, width = 720)

		self.save_button = Button(self.bbuttons, width = 17, text = "Save", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.add_student_data)
		self.save_button.grid(row = 0, column = 0)

		self.update_button = Button(self.bbuttons, width = 17, text = "Update", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.update_data)
		self.update_button.grid(row = 0, column = 1)

		self.delete_button = Button(self.bbuttons, width = 17, text = "Delete", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.delete_data)
		self.delete_button.grid(row = 0, column = 2)

		self.reset_button = Button(self.bbuttons, width = 17, text = "Reset", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue", command = self.reset_data)
		self.reset_button.grid(row = 0, column = 3)

		self.take_photo_button = Button(self.bbuttons, width = 35, text = "Take Photo", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue")
		self.take_photo_button.grid(row = 1, column = 0, columnspan = 2)

		self.update_photo_button = Button(self.bbuttons, width = 35, text = "Update Photo", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue")
		self.update_photo_button.grid(row = 1, column = 2, columnspan = 2)




		#-----Right-----
		self.framer = LabelFrame(self.win, bd = 2, bg = "white", relief = 'ridge', text = 'Student Details', font = ("times now roman", 12, "bold"))
		self.framer.place(x = 750, y = 20, width = 730, height = 540)

		self.search_studen = LabelFrame(self.framer, bd = 2, bg = 'white', relief = 'ridge', text = 'Search Students', font = ("times now roman", 12, "bold"))
		self.search_studen.place(x = 5, y = 5, width = 720, height = 70)

		self.search_by = Label(self.search_studen, text = 'Search By', font = ("times now roman", 12, "bold"), bg = "red", fg = 'white', width = 8)
		self.search_by.grid(row = 0, column = 0, padx = (10, 0), pady = 5, sticky = 'W')

		self.search_box = ttk.Combobox(self.search_studen, font = ("times now roman", 12, "bold"), width = 17, state = 'readonly')
		self.search_box['values'] =('Select', 'Roll No', 'Phone')
		self.search_box.current(0)
		self.search_box.grid(row = 0, column = 1, pady = 5)

		self.search_para = ttk.Entry(self.search_studen, font = ("times now roman", 12, "bold"), width = 18)
		self.search_para.grid(row = 0, column = 2, padx = (0,10), pady = 5)

		self.search_button = Button(self.search_studen, width = 12, text = "Search", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue")
		self.search_button.grid(row = 0, column = 3, pady = 5)

		self.show_button = Button(self.search_studen, width = 12, text = "Show All", font = ("times now roman", 12, "bold"), fg = "white", bg = "blue")
		self.show_button.grid(row = 0, column = 4, pady = 5)


		#-----Text Frame-----
		self.text_frame = Frame(self.framer, bd = 2, bg = "white", relief = 'ridge')
		self.text_frame.place(x = 5, y = 75, width = 720, height = 440)

		self.scrollx = ttk.Scrollbar(self.text_frame, orient = HORIZONTAL)
		self.scrolly = ttk.Scrollbar(self.text_frame, orient = VERTICAL)

		self.student_table = ttk.Treeview(self.text_frame, column = ("dep", "course", "year", "sem", "id", "name", "email", "phone", "div", "roll no", "gender", "dob", "address", "teacher", "photo"), xscrollcommand = self.scrollx.set, yscrollcommand = self.scrolly.set)

		self.scrollx.pack(side = BOTTOM, fill = X)
		self.scrolly.pack(side = RIGHT, fill = Y)
		self.scrollx.config(command = self.student_table.xview)
		self.scrolly.config(command = self.student_table.yview)

		self.student_table.heading("dep", text = "Department")
		self.student_table.heading("course", text = "Course")
		self.student_table.heading("year", text = "Year")
		self.student_table.heading("sem", text = "Semester")
		self.student_table.heading("id", text = "ID")
		self.student_table.heading("name", text = "Name")
		self.student_table.heading("email", text = "E-mail")
		self.student_table.heading("phone", text = "Phone")
		self.student_table.heading("div", text = "Division")
		self.student_table.heading("roll no", text = "Roll no")
		self.student_table.heading("gender", text = "Gender")
		self.student_table.heading("dob", text = "DOB")
		self.student_table.heading("address", text = "Address")
		self.student_table.heading("teacher", text = "Teacher")
		self.student_table.heading("photo", text = "Photo")
		self.student_table['show'] = 'headings'

		self.student_table.column('dep', width = 100)
		self.student_table.column('course', width = 100)
		self.student_table.column('year', width = 100)
		self.student_table.column('sem', width = 100)
		self.student_table.column('id', width = 100)
		self.student_table.column('name', width = 150)
		self.student_table.column('email', width = 200)
		self.student_table.column('phone', width = 100)
		self.student_table.column('div', width = 100)
		self.student_table.column('roll no', width = 100)
		self.student_table.column('gender', width = 100)
		self.student_table.column('dob', width = 100)
		self.student_table.column('address', width = 100)
		self.student_table.column('teacher', width = 100)
		self.student_table.column('photo', width = 100)

		self.student_table.pack(fill = BOTH, expand = 1)
		self.student_table.bind("<ButtonRelease>", self.get_cursor)
		self.fetch_data()
		self.win.mainloop()

	def add_student_data(self):
		if self.var_dep.get() == "Select" or self.var_year.get() == "Select" or self.var_semester.get() == "Select" or self.var_course.get() == "Select" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_teacher.get() == "" or self.var_address.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "" or self.var_division.get() == "" or self.var_roll.get() == "":
			messagebox.showerror("Error!","All fields are requires A", parent = self.win)
		else:
			try:
				conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
				mycursor = conn.cursor()
				mycursor.execute('INSERT INTO student_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
																													self.var_dep.get(),
																													self.var_course.get(),
																													self.var_year.get(),
																													self.var_semester.get(),
																													self.var_id.get(),
																													self.var_name.get(),
																													self.var_email.get(),
																													self.var_phone.get(),
																													self.var_division.get(),
																													self.var_roll.get(),
																													self.var_gender.get(),
																													self.var_dob.get(),
																													self.var_address.get(),
																													self.var_teacher.get(),
																													self.var_photo.get()
																													))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Success!","Student details has been added successfully", parent = self.win)
			except Exception as es:
				messagebox.showerror("Error!",f"Due to :{str(es)}", parent = self.win)

	def fetch_data(self):
		conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
		mycursor = conn.cursor()
		mycursor.execute("SELECT * FROM student_data")
		data = mycursor.fetchall()

		if len(data) != 0:
			self.student_table.delete(*self.student_table.get_children())
			for i in data:
				self.student_table.insert("", END, values = i)
			conn.commit()
		conn.close()

	def get_cursor(self, event = ""):
		cursor_focus = self.student_table.focus()
		content = self.student_table.item(cursor_focus)
		data = content['values']

		self.var_dep.set(data[0]),
		self.var_course.set(data[1]),
		self.var_year.set(data[2]),
		self.var_semester.set(data[3]),
		self.var_id.set(data[4]),
		self.var_name.set(data[5]),
		self.var_email.set(data[6]),
		self.var_phone.set(data[7]),
		self.var_division.set(data[8]),
		self.var_roll.set(data[9]),
		self.var_gender.set(data[10]),
		self.var_dob.set(data[11]),
		self.var_address.set(data[12]),
		self.var_teacher.set(data[13]),
		self.var_radio1.set(data[14]),

	def update_data(self):
		if self.var_dep.get() == "Select" or self.var_year.get() == "Select" or self.var_semester.get() == "Select" or self.var_course.get() == "Select" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_teacher.get() == "" or self.var_address.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "" or self.var_division.get() == "" or self.var_roll.get() == "":
			messagebox.showerror("Error!","All fields are requires.", parent = self.win)
		else:
			try:
				update_prompt = messagebox.askyesno("Update?", "Do you want to update this student's details", parent = self.win)
				if update_prompt > 0:
					conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
					mycursor = conn.cursor()
					mycursor.execute("UPDATE student_data SET department = %s, course = %s, curr_year = %s, semester = %s, student_name = %s, email = %s, phone = %s, division = %s, roll_no = %s, gender = %s, dob = %s, address = %s, teacher = %s, photo = %s WHERE id = %s",(
																																																																				self.var_dep.get(),
																																																																				self.var_course.get(),
																																																																				self.var_year.get(),
																																																																				self.var_semester.get(),																																																																		
																																																																				self.var_name.get(),
																																																																				self.var_email.get(),
																																																																				self.var_phone.get(),
																																																																				self.var_division.get(),
																																																																				self.var_roll.get(),
																																																																				self.var_gender.get(),
																																																																				self.var_dob.get(),
																																																																				self.var_address.get(),
																																																																				self.var_teacher.get(),
																																																																				self.var_photo.get(),
																																																																				self.var_id.get()
																																																																				))
				else:
					if not update_prompt:
						return
				messagebox.showinfo("Success","Details updated successfully", parent = self.win)
				conn.commit()
				self.fetch_data()
				conn.close()
			except Exception as es:
				messagebox.showerror("Error",f"Due to: {str(es)}", parent = self.win)

	def delete_data(self):
		if self.var_id.get() == "":
			messagebox.showerror("Error", "Student ID is neccessary!", parent = self.win)
		else:
			try:
				delete = messagebox.askyesno("Delete!", "Do you want to delete the details?", parent = self.win)
				if delete > 0:
					conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
					mycursor = conn.cursor()
					#mycursor.execute("SET SQL_SAFE_UPDATES = 0;")
					mycursor.execute("DELETE FROM student_data WHERE id = %s ",(self.var_id.get(),))
				else:
					if not delete:
						return
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Deleted!", "Student Details removed", parent = self.win)
			except Exception as es:
				messagebox.showerror("Error",f"Due to: {str(es)}")

	def reset_data(self):
		self.var_dep.set('Select'),
		self.var_course.set('Select'),
		self.var_year.set('Select'),
		self.var_semester.set('Select'),
		self.var_id.set(""),
		self.var_name.set(""),
		self.var_email.set(""),
		self.var_phone.set(""),
		self.var_division.set(""),
		self.var_roll.set(""),
		self.var_gender.set(""),
		self.var_dob.set(""),
		self.var_address.set(""),
		self.var_teacher.set(""),
		self.var_radio1.set(""),
		self.var_radio2.set(""),

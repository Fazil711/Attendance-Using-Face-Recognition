from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from student import Student
import os
from train import Train
from teacher_data import Teacher_data
from face_detect import Face_Detect
from attendance import Attendance_data
from Developer import Developer_data

class dashboard:
	def __init__(self):
		self.win = Tk()
		self.canvas = Canvas(self.win, width=1000, height=600, bg='#e9ff45')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 1000/2)
		y = int(height/2 - 700/2)
		self.win.geometry("1000x600+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Dashboard")
		
	def addframe1(self):
		self.frame = Frame(self.win, height = 580, width = 960, bg = '#f9ffcc')
		self.frame.place(x = 20, y = 10)
		#-----Menu------
		self.menu = Menu(self.win)
		self.win.config(menu = self.menu)

		self.students = Menu(self.menu, tearoff = 0,)
		self.students.add_command(label = 'Student Photo', command = self.student_photos)
		self.menu.add_cascade(label = 'Photos', menu = self.students)
		
		self.calender = Menu(self.menu, tearoff = 0)
		self.menu.add_cascade(label = 'Calender', menu = self.calender)
		self.database = Menu(self.menu, tearoff = 0)
		self.database.add_command(label = 'Train', command = self.train_set)
		self.menu.add_cascade(label = 'Database', menu = self.database)
		
		self.attendence = Menu(self.menu, tearoff = 0)
		#self.attendence.add_command(label = 'Help')
		self.menu.add_cascade(label = 'Help', menu = self.attendence)
		#-----****------
		self.label21 = Label(self.frame, text = "Welcome to the Dashboard", font = ("times new roman", 20, "bold"), fg = "black", bg = "#f9ffcc").place(x = 20, y = 20)
		#-----Button 1-----
		self.img = Image.open('photos/students.png').resize((100, 100), Image.ANTIALIAS)
		self.ph = ImageTk.PhotoImage(self.img)
		self.button1 = Button(self.frame, image = self.ph, bg = '#f9ffcc', relief = 'flat', command = self.student_details)
		self.button1.place(x = 60, y = 120)
		self.button1a = Button(self.frame, text = "Student Detail", font = ("times new roman", 12, "bold"), fg = "black", bg = "#f9ffcc", relief = "flat").place(x = 60, y = 220)
		#-----Button 2-----
		self.img1 = Image.open('photos/face_img.png').resize((100, 100), Image.ANTIALIAS)
		self.ph1 = ImageTk.PhotoImage(self.img1)
		self.button2 = Button(self.frame, image = self.ph1, bg = '#f9ffcc', relief = 'flat', command = self.face_detection)
		self.button2.place(x = 320, y = 120)
		self.button2a = Button(self.frame, text = "Face Detect", font = ("times new roman", 11, "bold"), fg = "black", bg = "#f9ffcc", relief = "flat", width = 11).place(x = 320, y = 220)
		#-----Button 3-----
		self.img2 = Image.open('photos/attendance_img.png').resize((100, 100), Image.ANTIALIAS)
		self.ph2 = ImageTk.PhotoImage(self.img2)
		self.button3 = Button(self.frame, image = self.ph2, bg = '#f9ffcc', relief = 'flat', command = self.attendence_func)
		self.button3.place(x = 560, y = 120)
		self.button3a = Button(self.frame, text = "Attendence", font = ("times new roman", 12, "bold"), fg = "black", bg = "#f9ffcc", relief = "flat", width = 11).place(x = 560, y = 220)
		#-----Button 4-----
		self.img3 = Image.open('photos/teacher_img.png').resize((100, 100), Image.ANTIALIAS)
		self.ph3 = ImageTk.PhotoImage(self.img3)
		self.button4 = Button(self.frame, image = self.ph3, bg = '#f9ffcc', relief = 'flat', command = self.teacher_set)
		self.button4.place(x = 800, y = 120)
		self.button4a = Button(self.frame, text = "Teacher", font = ("times new roman", 12, "bold"), fg = "black", bg = "#f9ffcc", relief = "flat", width = 11).place(x = 800, y = 220)

		self.img4 = Image.open('photos/developer_img.jpg').resize((100, 100), Image.ANTIALIAS)
		self.ph4 = ImageTk.PhotoImage(self.img4)
		self.button5 = Button(self.frame, image = self.ph4, bg = '#f9ffcc', relief = 'flat', command = self.developer_details)
		self.button5.place(x = 450, y = 300)
		self.button5a = Button(self.frame, text = "Developer", font = ("times new roman", 12, "bold"), fg = "black", bg = "#f9ffcc", relief = "flat", width = 11).place(x = 450, y = 400)
		self.win.mainloop()

	def student_photos(self):
		os.startfile('data')

	def student_details(self):
		self.new_window = Toplevel(self.win)
		self.app = Student(self.new_window)
		self.app.addframe2()

	def train_set(self):
		self.new_window = Toplevel(self.win)
		self.app = Train(self.new_window)
		self.app.add_frame3()

	def teacher_set(self):
		self.new_window = Toplevel(self.win)
		self.app = Teacher_data(self.new_window)
		self.app.add_frame4()

	def face_detection(self):
		self.new_window = Toplevel(self.win)
		self.app = Face_Detect(self.new_window)
		self.app.add_frame5()

	def attendence_func(self):
		self.new_window = Toplevel(self.win)
		self.app = Attendance_data(self.new_window)
		self.app.add_frame6()

	def developer_details(self):
		self.new_window = Toplevel(self.win)
		self.app = Developer_data(self.new_window)
		self.app.add_frame7()

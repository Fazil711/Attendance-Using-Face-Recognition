from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class Developer_data:
	def __init__(self, root):
		self.win = root
		self.canvas = Canvas(self.win, width=1000, height=440, bg='#0202c9')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 1000/2)
		y = int(height/2 - 540/2)
		self.win.geometry("1000x440+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Developer")

	def add_frame7(self):
		self.frame = Frame(self.win, height=420, width=960, bg = "#0051ff")
		self.frame.place(x = 20, y = 10)

		self.img = Image.open('photos/floppa.jpg').resize((300, 250), Image.ANTIALIAS)
		self.ph = ImageTk.PhotoImage(self.img)
		self.image_dev = Label(self.frame, image = self.ph, bg = '#0051ff', relief = 'flat')
		self.image_dev.place(x = 20, y = 10)

		self.name_dev = Label(self.frame, text = 'Fazil Floppa', fg = '#00ed9e', bg = '#0051ff', font = ('times now roman', 25, 'bold'))
		self.name_dev.place(x = 340, y = 10)

		self.dev_details = Text(self.frame, fg = 'white', bg = '#0051ff', height = 15, width = 75, relief = 'flat')
		self.dev_details.place(x = 340, y = 70)
		self.dev_details.insert(END, 'This Software Application is Developed by Mr. Fazil who is persuing for BE in Mumbai University in sem 5\nThis Application is designed for teachers to take attendence of student_id using Face Recognition \nThis Application is made using Python and its libarary Open_CV and we have used algorithm of \nhaarcascade_frontal_face to detect image & mark present in a csv file that can manage by teachers')
		self.dev_details.config(state = 'disabled')
		self.win.mainloop()

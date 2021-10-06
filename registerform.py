from tkinter import *
import os
import databasetest as dt
from tkinter import messagebox
import dashboard as dh

countries = []


world = open("countires_name.txt")
for count in world:
	count = count.rstrip('\n')
	countries.append(count)


class registerwin:
	def __init__(self):
		self.win = Tk()
		self.canvas = Canvas(self.win, width=600, height=500, bg='#12b0b5')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 600/2)
		y = int(height/2 - 500/2)
		self.win.geometry("600x500+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Registeration Form")

	def addframe(self):
		self.frame = Frame(self.win, height = 480, width = 560, bg = "#e3f4ff")
		self.frame.place(x = 20, y = 10)
		self.label11 = Label(self.frame, text = "Name: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 20)
		self.label12 = Label(self.frame, text = "Email: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 60)
		self.label13 = Label(self.frame, text = "Age: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 100)
		self.label14 = Label(self.frame, text = "Roll No: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 140)
		self.label15 = Label(self.frame, text = "Phone: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 180)
		self.label16 = Label(self.frame, text = "Address: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 220)
		self.label17 = Label(self.frame, text = "Country: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 260)
		self.label18 = Label(self.frame, text = "Password: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 300)
		self.label19 = Label(self.frame, text = "Confirm: ", font = ("times new roman", 20, "bold"), fg = "#124eb5", bg = "#e3f4ff").place(x = 20, y = 340)

		self.entry11 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry11.place(x = 230, y = 20)
		self.entry12 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry12.place(x = 230, y = 60)
		self.entry13 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry13.place(x = 230, y = 100)
		self.entry14 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry14.place(x = 230, y = 140)
		self.entry15 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry15.place(x = 230, y = 180)
		self.entry16 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry16.place(x = 230, y = 220)
		self.variable = StringVar(self.win)
		self.variable.set("Countries")
		self.entry17 = OptionMenu(self.frame, self.variable, *countries)
		#self.entry7 = Combobox(self.frame, self.variable, *countries)
		self.entry17.place(x = 237, y = 260)
		self.entry17.config(font = ("times now roman", 14, "bold"), height = 1, bg = "white", fg = "#124eb5", width = 23, relief = "flat")
		self.entry17["menu"].config(fg = "#124eb5", bg = "#e3f4ff")
		self.entry18 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry18.place(x = 230, y = 300)
		self.entry19 = Entry(self.frame, font = ("times now roman", 20, "bold"), fg = "#124eb5", relief = "flat")
		self.entry19.place(x = 230, y = 340)

		self.button = Button(self.frame, text = "Register", font = ("times new roman", 20, "bold"), fg = "white", bg = "#124eb5", width = 30, relief = "flat", command = self.register_user).place(x = 35, y = 400)
		self.win.mainloop()

	def register_user(self):
		data = (
			self.entry11.get(),
			self.entry12.get(),
			self.entry13.get(),
			self.entry14.get(),
			self.entry15.get(),
			self.entry16.get(),
			self.variable.get(),
			self.entry19.get()
		)
		if self.entry11.get() == "" or self.entry12.get() == "" or self.entry13.get() == "" or self.entry14.get() == "" or self.entry15.get() == "" or self.entry16.get() == "" or self.entry19.get() == "":
			messagebox.showinfo("Alert!","All fields are required")

		elif self.variable.get() == "Countries":
			messagebox.showinfo("Alert!", "Enter the Country name")

		elif self.entry19.get() != self.entry18.get():
			messagebox.showinfo("Alert!","Passwords don't match")

		else:
			dt.register_user(data)
			messagebox.showinfo("Message", "Registered Successfully!")
			self.win.destroy()
			redd = dh.dashboard()
			redd.addframe1()

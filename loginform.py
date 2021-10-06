from tkinter import *
from PIL import ImageTk, Image
import os
import registerform as rg
from tkinter import messagebox
import databasetest as dt
import dashboard as dh

class loginwin:
	def __init__(self):
		self.win = Tk()
		self.canvas = Canvas(self.win, width=600, height=400, bg='#e31486')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 600/2)
		y = int(height/2 - 400/2)
		self.win.geometry("600x400+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Login Form")

	def add_frame(self):
		self.frame = Frame(self.win, height=380, width=560, bg = "#ffccf1")
		self.frame.place(x = 20, y = 10)
		self.label1 = Label(self.frame, text = "Username: ", font = ("times new roman", 20, "bold"), fg = "red", bg = "#ffccf1").place(x = 140, y = 20)
		self.label2 = Label(self.frame, text = "Password: ", font = ("times new roman", 20, "bold"), fg = "red", bg = "#ffccf1").place(x = 140, y = 80)
		self.img = Image.open('photos/login_img.png').resize((100, 110), Image.ANTIALIAS)
		self.ph = ImageTk.PhotoImage(self.img)
		self.label3 = Label(self.frame, image = self.ph)
		self.label3.place(x = 20, y = 20)
		self.label3.config(bg = "#ffccf1")
		self.entry1 = Entry(self.frame, font = ("times new roman", 20, "bold"), fg = "red", width = 18, relief = "flat")
		self.entry1.place(x = 280, y = 20)
		self.entry2 = Entry(self.frame, show = "*", font = ("times new roman", 20, "bold"), fg = "red", width = 18, relief = "flat")
		self.entry2.place(x = 280, y = 80)
		self.button1 = Button(self.frame, text = "new user?", font = ("times new roman", 20, "bold"), fg = "blue", relief = "flat", command = self.newregister, bg = "#ffccf1").place(x = 400, y = 120)
		self.button2 = Button(self.frame, text = "Login", font = ("times new roman", 20, "bold"), fg = "white", bg = "red", width = 20, relief = "flat", command = self.login_check).place(x = 110, y = 300)
		self.win.mainloop()

	def newregister(self):
		self.win.destroy()
		reg = rg.registerwin()
		reg.addframe()

	def login_check(self):
		data = (
			self.entry1.get(),
			self.entry2.get()
		)

		if self.entry1.get() == "":
			messagebox.showinfo("Alert!","Enter the Username")
		elif self.entry2.get() == "":
			messagebox.showinfo("Alert!", "Enter the Password")
		else:
			res = dt.login_user(data)
			if res:
				messagebox.showinfo("Message", "Logged in Successfully!")
				self.win.destroy()
				xy = dh.dashboard()
				xy.addframe1()
			else:
				messagebox.showinfo("Alert!", "Wrong Data Given!")

if __name__ == "__main__":
	x = loginwin()
	x.add_frame()

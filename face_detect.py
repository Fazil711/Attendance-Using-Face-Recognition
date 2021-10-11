from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from student import Student
from time import strftime
import os
import mysql.connector
import cv2
from datetime import datetime
import numpy as np
from tkinter import messagebox

class Face_Detect:
	def __init__(self, root):
		self.win = root
		self.canvas = Canvas(self.win, width=1000, height=600, bg='#aa0ff7')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 1000/2)
		y = int(height/2 - 700/2)
		self.win.geometry("1000x600+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Face Detection")

	def add_frame5(self):
		self.frame = Frame(self.win, width = 940, height = 580, bg = '#edbdfc')
		self.frame.place(x = 30, y = 10)

		self.label = Label(self.frame, text = "Face Detection", font = ("times now roman", 20, "bold"), fg = "white", bg = '#ff0866')
		self.label.place(x = 0, y = 0, width = 940, height = 50)

		self.button = Button(self.frame, text = "Detect Now", font = ("times now roman", 20, "bold"), bg = '#ff0866', width = 20, command = self.face_rec)
		self.button.place(x = 10, y = 60)
		self.win.mainloop()

	def mark_attendance(self, i, r, n, d):
		with open('fazil.csv', "r+", newline = '\n') as f:
			mydatalist = f.readlines()
			name_list = []
			for line in mydatalist:
				entry = line.split(",")
				name_list.append(entry[0])
			if( (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
				now = datetime.now()
				d1 = strftime("%d/%m/%Y")
				dtstring = now.strftime('%H:%M:%S')
				f.writelines(f"\n{i}, {r}, {n}, {d}, {dtstring}, {d1}, Present")

	def face_rec(self):

		def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):

			gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

			cord = []

			for (x, y, w, h) in features:
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
				id_a, predict = clf.predict(gray_image[y:y + h, x:x + w])
				confidence = int((100*(1 - predict/300)))

				conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fazil@@621311', database ='testregister')
				mycursor = conn.cursor()

				mycursor.execute("SELECT student_name from student_data WHERE id="+str(id_a))
				n = mycursor.fetchone()
				n = "+".join(n)

				mycursor.execute("SELECT roll_no from student_data WHERE id="+str(id_a))
				r = mycursor.fetchone()
				r = "+".join(r)

				mycursor.execute("SELECT department from student_data WHERE id="+str(id_a))
				d = mycursor.fetchone()
				d = "+".join(d)

				mycursor.execute("SELECT id from student_data WHERE id="+str(id_a))
				i = mycursor.fetchone()
				i = "+".join(i)

				if confidence > 77:
					cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
					cv2.putText(img, f"Roll No: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
					cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
					cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
					self.mark_attendance(i, r, n, d)
				else:
					cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
					cv2.putText(img,"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

				cord = [x, y, w, h]

			return cord

		def recognize(img, clf, faceCascade):
			cord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
			return img

		faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		clf = cv2.face.LBPHFaceRecognizer_create()
		clf.read("classifier.xml")

		video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

		while True:
			ret, img = video_cap.read()
			img = recognize(img, clf, faceCascade)
			cv2.imshow("Welcome to face detection", img)

			if cv2.waitKey(1) == 13:
				break

		video_cap.release()
		cv2.destroyAllWindows()

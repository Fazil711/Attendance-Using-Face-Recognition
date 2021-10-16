import mysql.connector 

con = mysql.connector.connect(host = "localhost",
							  user = "name",
							  passwd = "password",
							  database = "testregister")

cur = con.cursor()

def login_user(tup):
	try:
		cur.execute("SELECT * FROM registeration WHERE user_name = %s AND passwd = %s;", tup)
		return(cur.fetchone())
	except:
		return False

def register_user(tup):
	try:
		cur.execute("INSERT INTO registeration (user_name, email_id, age, roll_no, phone_no, address, country, passwd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", tup)
		return(con.commit())
	except:
		return False

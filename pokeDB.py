import MySQLdb as sql
import pokemon
import _mysql_exceptions


class PokeDB():
	def create_Table(self):
		conn = sql.connect(host="localhost", user = 'testuser', passwd = 'test123', db = "testdb")
		cur = conn.cursor()
		try: 
			cur.execute ("CREATE TABLE Pokemon (ID INT PRIMARY KEY, name VARCHAR(255), Type1 VARCHAR(255), Type2 VARCHAR(255))")
		except _mysql_exceptions.OperationalError:
			print("Pokemon was already created")
		return cur, conn

	def get(self,id, cur):
		cur.execute("SELECT * FROM Pokemon WHERE ID = %s"%str(id))
		row = cur.fetchone()
		return row 

	def put(self,Pokemon,cur):
		try: 
			cur.execute('''INSERT INTO Pokemon (ID, name, Type1, Type2) VALUES (%s, %s, %s, %s)''',(Pokemon.id, Pokemon.name, Pokemon.prim, Pokemon.sec))
		except _mysql_exceptions.IntegrityError:
			print("That is a duplicate entry!")
			return False
		return True

	def update(sef,Pokemon, id,cur):
		try:
			cur.execute('''UPDATE Pokemon SET ID = %s, name = %s, Type1 = %s, Type2 = %s WHERE ID = %s''',(Pokemon.id, Pokemon.name, Pokemon.prim, Pokemon.sec, id))
		except _mysql_exceptions.IntegrityError:
			print("That is a duplicate entry!")
			return False
		return True
	def delete(self,Pokemon,cur):
		cur.execute('''DELETE FROM Pokemon where ID = %s''', (Pokemon.id))


import MySQLdb as sql
import pokemon
from _mysql_exceptions import OperationalError


class PokeDB():
	def create_Table(self):
		conn = sql.connect(host="localhost", user = 'testuser', passwd = 'test123', db = "testdb")
		cur = conn.cursor()
		try: 
			cur.execute ("CREATE TABLE Pokemon (ID INT PRIMARY KEY, name VARCHAR(255), Type1 VARCHAR(255), Type2 VARCHAR(255))")
		except OperationalError:
			print("Pokemon was already created")
		return cur

	def get(self,id,cur):
		cur.execute("SELECT * FROM Pokemon WHERE ID = %s"%str(id))
		row = cur.fetchone()
		return row

	def put(self,Pokemon,cur):
		cur.execute("INSERT INTO Pokemon (ID, name, Type1, Type2) VALUES (Pokemon.id, Pokemon.name, Pokemon.prim, Pokemon.sec)")

	def update(sef,Pokemon, id,cur):
		cur.execute("UPDATE Pokemon SET name = Pokemon.name, Type1 = Pokemon.prim, Type2 = Pokemon.sec WHERE ID = Pokemon.id")

	def delete(self,Pokemon,cur):
		cur.execute("DELETE FROM Pokemon where ID = Pokemon.id")

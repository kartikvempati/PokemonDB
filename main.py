import MySQLdb as sql
import pokemon
import pokeDB

db = pokeDB.PokeDB()
cur, conn = db.create_Table()

bulbasaur = pokemon.Pokemon(1, 'Bulbasaur', 'Grass', 'Poison')

charmander = pokemon.Pokemon(5, "Charmander", "Fire")
charmander.set_ID(4)

squirtle = pokemon.Pokemon(7, "Squirtles", "Water", "Ground")
squirtle.set_Secondary()



db.put(bulbasaur, cur)
db.put(charmander, cur)
db.put(squirtle, cur)

charmander.set_ID(6)
charmander.set_Name('Charizard')
charmander.set_Secondary('Flying')

db.update(charmander, 4, cur)

cur.execute('''SELECT * FROM Pokemon''')
row = cur.fetchall()
print(row)






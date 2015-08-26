import MySQLdb as sql
import pokemon
import pokeDB

db = pokeDB.PokeDB()
cur = db.create_Table()

bulbasaur = pokemon.Pokemon(1, "Bulbasaur", "Grass", "Poison")
print(bulbasaur.prim)
charmander = pokemon.Pokemon(5, "Charmander", "Fire")
print(charmander.sec)
charmander.set_ID(4)
squirtle = pokemon.Pokemon(7, "Squirtles", "Water", "Ground")
squirtle.set_Secondary()

print(squirtle.as_dict())


db.put(bulbasaur,cur)
# db.put(charmander,cur)






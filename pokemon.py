class Pokemon():
	def __init__(self, id, name, prim, sec = None):
		self.id = id
		self.name = name
		self.prim = prim
		self.sec = sec

	def as_dict(self):
		dict = {"poke_number": self.id, "name": self.name, "primary_type": self.prim, "secondary_type": self.sec}
		return dict

	def get_ID(self):
		return self.id

	def set_ID(self, id):
		self.id = id
		return True

	def get_Name(self):
		return self.name

	def set_Name(self, name):
		self.name = name
		return True

	def get_Primary(self):
		return self.prim

	def set_Primary(self, prim):
		self.prim = prim
		return True

	def get_Secondary(self):
		return self.sec

	def set_Secondary(self, sec=None):
		self.sec = sec
		return True







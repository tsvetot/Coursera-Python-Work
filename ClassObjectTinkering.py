class PartyAnimal:
	x = 0
	name = ""
	def_init_(self, nam):
		self.name = nam
		print self.name, "constructed"

def party(self):
	self.x = self.x + 1
	print self.name, "party.count",self.x

class BaseballFan(PartyAnimal):
	points = 0
	def strikes(self):
		self.points = self.points + 10
		self.party()
		print self.name, "points", self.points

q = BaseballFan("Quinn")
q.party()
q.strikes()

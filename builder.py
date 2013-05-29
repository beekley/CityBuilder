import random

WealthAvg = 1000
WealthDist = 500
Population = 10
Width = 10
Height = 10

CitList = []
Grid = []

# empty plot


class Citizen():
  def __init__(self):
		self.wealth = round(abs(random.gauss(WealthAvg, WealthDist)))

class Plot():
	def __init__(self, xcoor, ycoor):
		self.occupant = Citizen()
		self.occupant.wealth = 0
		self.occupied = False
		self.x = xcoor
		self.y = ycoor
		self.value = 0
		self.evaluate()
		
	def populate(self, populant):
		self.occupant = populant
		self.occupied = True
		self.evaluate()
		if self.value > 50:
			self.UpdateAdjacent()
		
	def evaluate(self):
		sidecount = 0
		totalvalue = 0
		initialvalue = self.value
		
		try:
			totalvalue = Grid[self.y+1][self.x].value
		except IndexError:
			sidecount += 1
		try:
			totalvalue += Grid[self.y][self.x+1].value
		except IndexError:
			sidecount += 1
		try:
			totalvalue += Grid[self.y-1][self.x].value
		except IndexError:
			sidecount += 1
		try:
			totalvalue += Grid[self.y][self.x-1].value
		except IndexError:
			sidecount += 1
		
		if sidecount < 4:
			self.value = ( 2 * self.occupant.wealth + totalvalue) / (6-sidecount)
			
		if self.value > 50 and abs(initialvalue - self.value) > 50:
			self.UpdateAdjacent()
			
	def UpdateAdjacent(self):
		try:
			Grid[self.y+1][self.x].evaluate()
		except IndexError:
			pass
		try:
			Grid[self.y][self.x+1].evaluate()
		except IndexError:
			pass
		try:
			Grid[self.y-1][self.x].evaluate()
		except IndexError:
			pass
		try:
			Grid[self.y][self.x-1].evaluate()
		except IndexError:
			pass
		
def AddCitizens():
	for i in range(Population):
		NewCitizen = Citizen()
		CitList.append(NewCitizen)
		
def BuildGrid():
	for i in range(Height):
		Grid.append([])
		for j in range(Width):
			NewPlot = Plot(j,i)
			Grid[i].append(NewPlot)

def RefreshValues():
	for i in range(Height):
		for j in range(Width):
			Grid[i][j].evaluate()
			
def PrintGrid():
	for i in range(Width):
		Line = '|'
		for j in range(Width):
			Line = Line + str(int(Grid[i][j].value)).zfill(4) + '|'
		print(str(Width-i).zfill(2) + Line)
	print('\n')
	
BuildGrid()
Guy = Citizen()

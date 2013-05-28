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
		
	def evaluate(self):
		sidecount = 0
		totalvalue = 0
		
		try:
			totalvalue = Grid[self.y+1][self.x].occupant.wealth
		except IndexError:
			sidecount += 1
		try:
			totalvalue += Grid[self.y][self.x+1].occupant.wealth
		except IndexError:
			sidecount += 1
		try:
			totalvalue += Grid[self.y-1][self.x].occupant.wealth
		except IndexError:
			sidecount += 1
		try:
			totalvalue += Grid[self.y][self.x-1].occupant.wealth
		except IndexError:
			sidecount += 1
		
		if sidecount < 4:
			self.value = totalvalue / (4-sidecount)
		
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
			Line = Line + str(Grid[i][j].occupant.wealth) + '|'
		print(str(Width-i) + Line)
	print('\n')

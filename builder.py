import random

WealthAvg = 1000
WealthDist = 500
Population = 10
Width = 10
Height = 10

CitList = []
Grid = [] 

class Citizen():
  def __init__(self):
		self.wealth = round(abs(random.gauss(WealthAvg, WealthDist)))

class Plot():
	def __init__(self, x, y):
		self.occupant = None
		self.xcoor = x
		self.ycoor = y
		self.value = 0
		
	def evaluate(self):
		totalvalue = Grid[self.y+1][self.x].occupant.wealth
		totalvalue += Grid[self.y][self.x+1].occupant.wealth
		totalvalue += Grid[self.y-1][self.x].occupant.wealth
		totalvalue += Grid[self.y][self.x-1].occupant.wealth
		self.value = totalvalue / 4
		
def BuildGrid():
	for i in range(Height):
		Grid.append([])
		for j in range(Width):
			NewPlot = Plot(j,i)
			Grid[i].append(NewPlot)

def AddCitizens():
	for i in range(Population):
		NewCitizen = Citizen()
		CitList.append(NewCitizen)
		

import random

# City Parameters
WealthAvg = 10000
WealthDist = 5000
Population = 50
Width = 3
Height = 50
BaseValue = 100

# Initialize Arrays
CitList = []
Grid = []
ProbVals = []

# Citizen class that has a random wealth around an average
class Citizen():
	def __init__(self):
		self.wealth = round(abs(random.gauss(WealthAvg, WealthDist)))
		self.x = None
		self.y = None

# Plot class that has initial "citizen" with no value		
class Plot():
	def __init__(self, xcoor, ycoor):
		self.occupant = Citizen()
		self.occupant.wealth = 0
		self.occupied = False
		self.x = xcoor
		self.y = ycoor
		self.value = 0
		self.evaluate()
	
	# Bookkeeping for adding a citizen	
	def populate(self, populant):
		self.occupant = populant
		self.occupant.x = self.x
		self.occupant.y = self.y
		self.occupied = True
		self.evaluate()
		if self.value > 50:
			self.UpdateAdjacent()
	
	# Booking for removing a citizen
	def depopulate(self, update=0):
		self.occupant.x = None
		self.occupant.y = None
		self.occupant = Citizen()
		self.occupant.wealth = 0
		self.occupied = False
		self.evaluate()
		if self.value > 50 and update > 0:
			self.UpdateAdjacent()
	
	# Calculates value based on wealth of surrounding plots
	def evaluate(self):
		sidecount = 0
		totalvalue = 0
		initialvalue = self.value
		
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
			self.value = BaseValue + ((2*self.occupant.wealth) + totalvalue) / (6-sidecount)
			
		if self.value > (BaseValue + 50) and abs(initialvalue - self.value) > 50:
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
			

def PrintWealths():
	for i in range(Height):
		Line = '|'
		for j in range(Width):
			Line = Line + str(int(Grid[i][j].occupant.wealth)).zfill(4) + '|'
		print(str(i).zfill(2) + Line)
	print('\n')

def PrintValues():
	for i in range(Height):
		Line = '|'
		for j in range(Width):
			Line = Line + str(int(Grid[i][j].value)).zfill(4) + '|'
		print(str(i).zfill(2) + Line)
	print('\n')
	
def SetProbs():
	ProbCount = 0
	for i in range(Height):
		for j in range(Width):
			ProbCount += Grid[i][j].value
			ProbVals.append([ProbCount, [i,j] ])
	return ProbCount

def CitPop(Cit, max):
	
	while True:
		DiceRoll = random.uniform(0,max)
		for k in range(len(ProbVals)):
			if DiceRoll <= ProbVals[k][0]:
				PopPlot = ProbVals[k][1]
				break
				
		if Grid[PopPlot[0]][PopPlot[1]].occupied == False:
			Grid[PopPlot[0]][PopPlot[1]].populate(Cit)
			return PopPlot
	
def ListPop(List):
	ProbMax = SetProbs()
	for i in range(len(List)):
		if List[i].y != None or List[i].x != None:
			Grid[List[i].y][List[i].x].depopulate()
			
		Location = CitPop(List[i], ProbMax)
		List[i].x =	Location[1]
		List[i].y = Location[0]
	
BuildGrid()
AddCitizens()
ListPop(CitList)

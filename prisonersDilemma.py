import os
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#Graphs constructed with MatplotLib
#Learned for this assignment using
#tutorial found at this link:
# https://python-graph-gallery.com/11-grouped-barplot/



n = 100
m = 5
k = 20
p = .50




p1PayoffRow1 = [3, 0]
p1PayoffRow2 = [5, 1]
p1Payoffs = [p1PayoffRow1, p1PayoffRow2]

p2PayoffRow1 = [3,5]
p2PayoffRow2 = [0,1]
p2Payoffs = [p2PayoffRow1, p2PayoffRow2]



class Strategy:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        
    def getNextMove(self, selfLastPlayedStrat, oppLastPlayedStrat):
        
        if self.index == 1:
            return oppLastPlayedStrat
        
        if self.index == 2:
            if selfLastPlayedStrat == 0:
                if oppLastPlayedStrat == 0:
                    return 0
            
                    
            return 1
        
        if self.index == 3:
            #code
            return 0
        
        if self.index == 4:
            #code
            return 1
        
    
    
 

class Player:
    def __init__(self, type):
        self.type = type
        self.payoff = 0
    def getNextMove(self, selfLastPlayedStrat, oppLastPlayedStrat):
        
        return self.type.getNextMove(selfLastPlayedStrat, oppLastPlayedStrat)
        
class Game:
    def __init__(self, rounds, p1, p2):
        self.rounds = rounds
        self.p1 = p1
        self.p2 = p2
        
    def updatePayoffs(self, p1Strat, p2Strat):
        self.p1.payoff += p1Payoffs[p1Strat][p2Strat]
        self.p2.payoff += p2Payoffs[p1Strat][p2Strat]
    
    def runGame(self):
        
        
        p1Strat = self.p1.getNextMove(0,0)
        p2Strat = self.p2.getNextMove(0,0)
        self.updatePayoffs(p1Strat, p2Strat)
        roundsPlayed = 1
        while(roundsPlayed < self.rounds):
            lastP1Strat = p1Strat
            lastP2Strat = p2Strat
            p1Strat = self.p1.getNextMove(lastP1Strat, lastP2Strat)
            p2Strat = self.p2.getNextMove(lastP1Strat, lastP2Strat)
            self.updatePayoffs(p1Strat, p2Strat)
            roundsPlayed += 1
    
        
def sortFunc(pl):
    return pl.payoff

#create strategy objects
TitForTat = Strategy(1, "TitForTat")
Grudger = Strategy(2, "Grudger")
AlwaysCoop = Strategy(3, "Always Coop")
AlwaysDefect = Strategy(4, "Always Defect")

player1 = Player(TitForTat)
player2 = Player(Grudger)
player3 = Player(AlwaysCoop)
player4 = Player(AlwaysDefect)

playerList = []

while len(playerList) < n:
    if(len(playerList) % 4 == 0):
        newPlayer = Player(TitForTat)
    if(len(playerList) % 4 == 1):
        newPlayer = Player(Grudger)
    if(len(playerList) % 4 == 2):
        newPlayer = Player(AlwaysCoop)
    if(len(playerList) % 4 == 3):
        newPlayer = Player(AlwaysDefect)
    playerList.append(newPlayer)


trialsRun = 0

n_groups = k
percentPopT4T = []
percentPopG = []
percentPopAC = []
percentPopAD = []

totalPayoffT4T = []
totalPayoffG = []
totalPayoffAC = []
totalPayoffAD = []

averagePayoffT4T = []
averagePayoffG = []
averagePayoffAC = []
averagePayoffAD = []

while(trialsRun < k):
    for x in playerList:
        x.payoff = 0
    
    for i in range(len(playerList)):
        focusPlayer = playerList[i]
        for y in range((i+1), len(playerList), 1):
            curGame = Game(m, focusPlayer, playerList[y])
            curGame.runGame()
    playerList.sort(reverse=False, key=sortFunc)
    
    toRemove = p * len(playerList)
    
    
    T4TCount = 0
    GCount = 0
    ACCount = 0
    ADCount = 0
    
    T4TPayoffTotal = 0
    GPayoffTotal = 0
    ACPayoffTotal = 0
    ADPayoffTotal = 0
    
    for x in playerList:
        if(x.type == TitForTat):
            T4TCount += 1
            T4TPayoffTotal += x.payoff
        if(x.type == Grudger):
            GCount += 1
            GPayoffTotal += x.payoff
        if(x.type == AlwaysCoop):
            ACCount += 1
            ACPayoffTotal += x.payoff
        if(x.type == AlwaysDefect):
            ADCount += 1
            ADPayoffTotal += x.payoff
    totalPayoff = T4TPayoffTotal + GPayoffTotal + ACPayoffTotal + ADPayoffTotal
    
    
    print("Gen " + str(trialsRun + 1) + ": T4T:" + str(int((T4TCount/len(playerList))*100))+"%    G:"
          +str(int((GCount/len(playerList))*100))+"%    AC:"+str(int((ACCount/len(playerList))*100))+"%    AD:"
          +str(int((ADCount/len(playerList))*100))+"%")
    
    
    
    print("Gen " + str(trialsRun + 1) + ": T4T:" + str(T4TPayoffTotal)+"    G:"
          +str(GPayoffTotal)+"    AC:"+str(ACPayoffTotal)+"    AD:"
          +str(ADPayoffTotal)+"    Total: " + str(totalPayoff))
    totalPayoffT4T.append(T4TPayoffTotal)
    totalPayoffG.append(GPayoffTotal)
    totalPayoffAC.append(ACPayoffTotal)
    totalPayoffAD.append(ADPayoffTotal)
    
    if(T4TCount > 0):
        toPrintT4T = int(T4TPayoffTotal/T4TCount)
    else:
        toPrintT4T = 0
    if(GCount > 0):
        toPrintG = int(GPayoffTotal/GCount)
    else:
        toPrintG = 0
    if(ACCount>0):
        toPrintAC = int(ACPayoffTotal/ACCount)
    else:
        toPrintAC = 0
    if(ADCount):
        
        toPrintAD = int(int(ADPayoffTotal/ADCount))
    else:
        toPrintAD = 0
    
    print("Gen " + str(trialsRun + 1) + ": T4T:" + str(toPrintT4T)+"    G:"
          +str(toPrintG)+"    AC:"+str(toPrintAC)+"    AD:"
          +str(toPrintAD) )
    print("\n")
    
    averagePayoffT4T.append(toPrintT4T)
    averagePayoffG.append(toPrintG)
    averagePayoffAC.append(toPrintAC)
    averagePayoffAD.append(toPrintAD)
    
    
    #graph preparation stuff
    percentPopT4T.append(int((T4TCount/len(playerList))*100))
    percentPopG.append(int((GCount/len(playerList))*100))
    percentPopAC.append(int((ACCount/len(playerList))*100))
    percentPopAD.append(int((ADCount/len(playerList))*100))
    
    for i in range(int(toRemove)):
        del playerList[0]
    
    trialsRun += 1

barWidth = 0.25
 
# Set position of bar on X axis
r1 = np.arange(len(percentPopT4T))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

 
# Make the plot
plt.bar(r1, percentPopT4T, color='#0066ff', width=barWidth, edgecolor='white', label='T4T')
plt.bar(r2, percentPopG, color= '#e6e600', width=barWidth, edgecolor='white', label='Grudger')
plt.bar(r3, percentPopAC, color='#009933', width=barWidth, edgecolor='white', label='Coop')
plt.bar(r4, percentPopAD, color='#ff0000', width=barWidth, edgecolor='white', label='Defect')
 
# Add xticks on the middle of the group bars
plt.xlabel('Generations')
plt.ylabel('Percent of Population')
plt.xticks([r + barWidth for r in range(len(percentPopT4T))], [])
 
# Create legend & Show graphic
plt.legend()
plt.savefig('q3_3PercentPopulation.png')

plt.clf()
#Chart 2

barWidth = 0.25
 
# Set position of bar on X axis
r1 = np.arange(len(totalPayoffT4T))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

 
# Make the plot
plt.bar(r1, totalPayoffT4T, color='#0066ff', width=barWidth, edgecolor='white', label='T4T')
plt.bar(r2, totalPayoffG, color= '#e6e600', width=barWidth, edgecolor='white', label='Grudger')
plt.bar(r3, totalPayoffAC, color='#009933', width=barWidth, edgecolor='white', label='Coop')
plt.bar(r4, totalPayoffAD, color='#ff0000', width=barWidth, edgecolor='white', label='Defect')
 
# Add xticks on the middle of the group bars
plt.xlabel('Generations')
plt.ylabel('Total Payoff by Strategy' )
plt.xticks([r + barWidth for r in range(len(totalPayoffT4T))], [])
 
# Create legend & Show graphic
plt.legend()
plt.savefig('q3_3TotalPayoff.png')
plt.clf()
#Chart 3

barWidth = 0.25
 
# Set position of bar on X axis
r1 = np.arange(len(totalPayoffT4T))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

 
# Make the plot
plt.bar(r1, averagePayoffT4T, color='#0066ff', width=barWidth, edgecolor='white', label='T4T')
plt.bar(r2, averagePayoffG, color= '#e6e600', width=barWidth, edgecolor='white', label='Grudger')
plt.bar(r3, averagePayoffAC, color='#009933', width=barWidth, edgecolor='white', label='Coop')
plt.bar(r4, averagePayoffAD, color='#ff0000', width=barWidth, edgecolor='white', label='Defect')
 
# Add xticks on the middle of the group bars
plt.xlabel('Generations')
plt.ylabel('Average Payoff by Strategy' )
plt.xticks([r + barWidth for r in range(len(totalPayoffT4T))], [])
 
# Create legend & Show graphic
plt.legend()
plt.savefig('q3_3AveragePayoff.png')

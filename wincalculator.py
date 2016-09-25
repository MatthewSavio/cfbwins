# open init-cfb-file.txt
# import (team, cumul-2010-wins, cumul-2010-losses, cumul-2010-ties) for each team
import math
from decimal import Decimal #We use Decimal to ensure rounding accuracy

# function CalWinPerc takes the team list as input CFBlist = [team, wins, losses, ties] and returns WinPerc (a float number with 5 decimal places)
def CalWinPerc(cfbList):
  if len(cfbList) == 4:
    cfbTeam = cfbList[0]
    cfbWins = int(cfbList[1])
    cfbLoss = int(cfbList[2])
    cfbTies = int(cfbList[3])
    WinPerc = (Decimal(cfbWins) + (Decimal(cfbTies)/2)) / Decimal(cfbWins+cfbLoss+cfbTies)
    return WinPerc
  else:
    print "Error in CalWinPerc Argument!"
    return
  
  
  
def RoundWinPerc(WinPerc):
  RoundWinPerc = 

# (notes)
# take cfbteam as inputs
# take cfbuntil2010wins as input
# using BeautifulSoup and tweepy and math
# grab wins since 2011 from "http://www.sports-reference.com/cfb/schools/" + cfbteam + "/"
# confirm that latest year = current year
# add up wins 
# add up losses
# add up ties (no adding needed)
# # calculate winning % = ( total wins + total losses / 2 ) / num all games 
# find next 100 win milestone (int(math.ceil(x/100.0))*100)
# winsleft to milestone = milestone - totalwins
# return winsleft to milestone
# predict when will pass next 100 win milestone (= winsleft / winning %) = num-games-to-play


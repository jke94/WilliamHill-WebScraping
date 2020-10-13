import sys
import os
import csv
import pandas as pd

class FootballMatchEvent:
    
    def __init__(self, urlMatchEvent, teamOfMatchs, localTeamGoals, visitantTeamGoals, matchTimeInstant):
        self.UrlFootballMatchEvent = urlMatchEvent
        self.IdFootballMatchEvent = self.GetIdFootballMatchEvent(urlMatchEvent)
        self.LocalTeamName = teamOfMatchs.split(' v ')[0]
        self.VisitantTeamName = teamOfMatchs.split(' v ')[1]
        self.PathDataFileEvent = self.CreateFileMatchFootballEvent('.././data/' + self.IdFootballMatchEvent + '.csv')
        self.LocalTeamGoals = localTeamGoals
        self.VisitantTeamGoals = visitantTeamGoals
        self.MatchTimeInstant = matchTimeInstant
        

    def GetIdFootballMatchEvent(self, urlMatchEvent):

        auxElements = urlMatchEvent.split('/')

        element = ''

        for item in auxElements:
            if "OB_" in item:
                element = item
                break

        return element

    def CreateFileMatchFootballEvent(self, pathCSVFile):
        
        if not os.path.exists(pathCSVFile):
            
            if not os.path.exists('.././data/'):
                os.mkdir('.././data/')
            
            with open(pathCSVFile, 'a', newline='\n') as f:

                writer = csv.writer(f)               

                df = pd.DataFrame(columns=[ 'TimeStamp','MatchTime' 
                                            'LocalTeamName', 'VisitantTeamName', 
                                            'LocalTeamGoals','VisitantTeamGoals',
                                            'LocalBet','DrawBet','VisitantBet'
                                            ])

                df.to_csv(pathCSVFile, index=False, header=True)
                f.close()

        return pathCSVFile
'''

    AUTOR: Javier Carracedo
    Github User: jke94
    File: FootballMatchEvent.py
    Date: 13/10/2020 

    Class used in SeleniumSpyder.py scrpit file to get info about each football match in
        'https://sports.williamhill.es/betting/es-es/en-directo/fútbol" 
    web page.

'''

from datetime import datetime
import csv
import logging
import pandas as pd
import os
import sys

class FootballMatchEvent:
    """ FootballMatchEvent to store and managed info about a match in William Web Page.
        
        The main purpouse of this class is store and managed information to print on csv file.
        Each object FootballMatchEvent can print atributes as info in csv file. This class originaly
        was created to be used in SeleniumSpyder.py script file.

        Attributes:

        UrlFootballMatchEvent: str
            The URL of a match.

        IdFootballMatchEvent: str
            The ID for a football match. Used to created the csv file to stored the info from URL

        LocalTeamName: str
            The local team name of the football match. For example 'Bucovina Radauti'.
        
        VisitantTeamName : str
            The away team name of the football match. For example 'Pascani'.
        
        PathDataFileEvent: str
            CSV Relative file path. For example '.././data/OB_EV18745122.csv'.

        LocalTeamGoals: str
            The number of goals of the home team. For example '2'.
        
        VisitantTeamGoals: str
            The number of goals of the away team. For example '1'
        
        MatchTimeInstant: str
            The instance time for the match. For example '85:50'.

        
    """

    def __init__(self, urlMatchEvent, teamOfMatchs, localTeamGoals, visitantTeamGoals, matchTimeInstant):
        ''' Initialize atributes of the object.
            
            Args:

            urlMatchEvent: str
                The URL of a match.

            teamOfMatchs: str
                The string returned by the scrapping to split and get
                the home team and away team. For example 'Bucovina Radauti v Pascani'
            
            localTeamGoals: str
                The number of goals of the home team. For example '2'

            visitantTeamGoals : str
                The number of goals of the away team. For example '1'

            matchTimeInstant : str
                The instance time for the match. For example '85:50'.
        '''

        self.UrlFootballMatchEvent = str(urlMatchEvent)
        self.IdFootballMatchEvent = str(self.GetIdFootballMatchEvent(urlMatchEvent))
        self.LocalTeamName = str(teamOfMatchs.split(' v ')[0])
        self.VisitantTeamName = str(teamOfMatchs.split(' v ')[1])
        self.PathDataFileEvent = self.CreateFileMatchFootballEvent('.././data/' + self.IdFootballMatchEvent + '.csv')
        self.LocalTeamGoals = str(localTeamGoals)
        self.VisitantTeamGoals = str(visitantTeamGoals)
        self.MatchTimeInstant = str(matchTimeInstant)
        
    def GetIdFootballMatchEvent(self, urlMatchEvent):
        ''' Get the id for the match from match URL.
            
            Args:

            urlMatchEvent: str
                The URL of a match.

            Returns: str
                The ID of a football match.  
        '''

        auxElements = urlMatchEvent.split('/')

        element = ''

        for item in auxElements:
            if "OB_" in item:
                element = item
                break

        return element

    def CreateFileMatchFootballEvent(self, pathCSVFile):
        ''' If not exists the file, create a file for store data about a match .
            
            Args:

            pathCSVFile: str
                Relative path with the name of the file.

            Returns: str
                The relative path with the name of the file.  
        '''
        
        if not os.path.exists(pathCSVFile):
            
            if not os.path.exists('.././data/'):
                os.mkdir('.././data/')
            
            with open(pathCSVFile, 'a', newline='\n') as f:

                writer = csv.writer(f)               

                df = pd.DataFrame(columns=[ 'TimeStamp',            # Values for example as '13/10/2020 16:54:28'
                                            'MatchTime'             # Values for example as '85:50'
                                            'LocalTeamName',        # Values for example as 'Bucovina Radauti'
                                            'VisitantTeamName',     # Values for example as 'Pascani'
                                            'LocalTeamGoals',       # Values for example as '2'
                                            'VisitantTeamGoals',    # Values for example as '1'
        #TODO: Implement on the nexts steps 'LocalBet',             # Values for example as ???
        #TODO: Implement on the nexts steps 'DrawBet',              # Values for example as ???
        #TODO: Implement on the nexts steps 'VisitantBet'           # Values for example as ???
                                            ])

                df.to_csv(pathCSVFile, index=False, header=True)
                f.close()

                logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '|| ' + 
                                'Created file ' + self.IdFootballMatchEvent + '.csv for: ' 
                                + self.LocalTeamName + ' VS ' + self.VisitantTeamName)

        return pathCSVFile
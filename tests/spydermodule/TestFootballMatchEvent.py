import unittest
from src.spydermodule.FootballMatchEvent import FootballMatchEvent

class TestFootballMatchEvent(unittest.TestCase):

    def setUp(self):
        
        self.MyFootballMatchEvent = FootballMatchEvent(  'https://www.python.org/OB_EV18745122',
                                                            'Spain v Portugal',
                                                            '3','1','67:30')
        self.OtherFootballMatchEventInstance = FootballMatchEvent(  'https://www.python.org/OB_EV18745122',
                                                    'Spain v Portugal',
                                                    '4','1','67:35')

    def testConstructor(self):
        
        self.assertEqual(self.MyFootballMatchEvent.UrlFootballMatchEvent,   'https://www.python.org/OB_EV18745122')
        self.assertEqual(self.MyFootballMatchEvent.IdFootballMatchEvent,    'OB_EV18745122')
        self.assertEqual(self.MyFootballMatchEvent.LocalTeamName,           'Spain')
        self.assertEqual(self.MyFootballMatchEvent.VisitantTeamName,        'Portugal')
        self.assertEqual(self.MyFootballMatchEvent.PathDataFileEvent,       '.././data/OB_EV18745122.csv')
        self.assertEqual(self.MyFootballMatchEvent.LocalTeamGoals,          '3')
        self.assertEqual(self.MyFootballMatchEvent.VisitantTeamGoals,       '1')
        self.assertEqual(self.MyFootballMatchEvent.MatchTimeInstant,        '67:30')

    def testFileMatchFootballEvent(self):
        
        self.assertEqual(   self.MyFootballMatchEvent.PathDataFileEvent, 
                            self.OtherFootballMatchEventInstance.PathDataFileEvent)

if __name__ == '__main__':
    unittest.main()
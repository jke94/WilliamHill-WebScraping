'''

    AUTOR: Javier Carracedo
    Date: 08/10/2020 

    WilliamHillURLs class to managed info about William Hill web pages.

'''

import requests 
from bs4 import BeautifulSoup
from urlvalidator import validate_url, ValidationError

class WilliamHillURLs:
    """Auxiliar class with data about William Hill Web to scraping data.

    Returns:
        WilliamHillURLs: An object with data and auxiliar functions.

    Attributes
    ----------
    
    BaseURL : str
        William Hill URL base web page.

    URL_FootballOnDirect : str
        Football matches URL in direct on William Hill web page.

    URL_TenisOnDirect : str
        Tenis matches URL in direct on William Hill web page.

    URL_BasketOnDirect : str
        Basket matches URL in direct on William Hill web page.

    """

    BaseURL = 'https://sports.williamhill.es/'

    URL_FootballOnDirect = 'https://sports.williamhill.es/betting/es-es/en-directo/f%C3%BAtbol'

    URL_TenisOnDirect = 'https://sports.williamhill.es/betting/es-es/en-directo/tenis'

    URL_BasketOnDirect = 'https://sports.williamhill.es/betting/es-es/en-directo/baloncesto'

    
    def GetAllUrlMatches(self, urlSport=URL_FootballOnDirect):

        """Get all url matchs from a sport (by default foorball urls.). Validate each URL if it´s a URL valid.

        Args:
            urlSport (str, optional): Football mathes on direct URL William Hill  . Defaults to "https://sports.williamhill.es/betting/es-es/en-directo/f%C3%BAtbol".

        Returns:
            list: List with all URL matches.
        """

        req = requests.get(urlSport)
        soup = BeautifulSoup(req.content.decode('utf-8','ignore'), "html.parser")

        aux = soup.findAll("a", {"class": ['btmarket__name btmarket__name--featured']})
        
        auxList = []

        for item in aux:
            try:
                theUrl = (self.BaseURL + item['href']).replace("//","/").replace("https:/","https://")
                validate_url(theUrl)
                auxList.append(theUrl)
            except ValidationError:
                raise ValidationError(theUrl)

        return auxList

    def GetAllMatchsPlayedActually(self, urlSport=URL_FootballOnDirect):
        """Get all sport matches played in the actuall moment.

        Args:
            urlSport (str, optional): A William Hill URL sport. Defaults to URL_FootballOnDirect.

        Returns:
            list: List with all matches and its bets.
        """
        req = requests.get(urlSport)
        soup = BeautifulSoup(req.content.decode('utf-8','ignore'), "lxml")

        matches = soup.findAll("div", {"class": "btmarket__link-name btmarket__link-name--ellipsis show-for-desktop-medium"})
        listaApuestas = soup.findAll("div", {"class": "btmarket__selection"})

        matchList = []
        
        for item in matches:
            var = item.text + ': ' + listaApuestas[0].text + ' | ' +  listaApuestas[1].text + ' | ' +  listaApuestas[2].text
            matchList.append(var)

        return matchList

    def ConvertFractionalBetToDecimalBet(self, theBet):
        """Convert a fraccioanl bet str to 

        Args:
            theBet (str): A fractional bet.

        Returns:
            [str]: A decimal bet.
        """
        bet = 0.0
        aux = str(theBet).split('/')
        bet = (int(aux[0], 10) / int(aux[1], 10) ) + 1
        
        return str(round(bet, 2))

    def GetAllBetsFromURLMatch(self, url):
        """Get all bets actually from a match. 

        Args:
            url (str): Match URL

        Returns:
            [type]: A list with the diferents bets availables.
        """
        allBetsList = []

        req = requests.get(url)
        soup = BeautifulSoup(req.content.decode('utf-8','ignore'), "html.parser")

        aux = soup.findAll("h2", {"class" : ['fl']})

        # print('Number of diferent bets: ', len(aux), ', Match URL: ', url)

        for item in aux:
            allBetsList.append(item.text)
            # print(item.text,'|',type(item.text), item['class'])

        return allBetsList
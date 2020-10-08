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
        soup = BeautifulSoup(req.text, "html.parser")

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
        soup = BeautifulSoup(req.text, "lxml")

        matches = soup.findAll("div", {"class": "btmarket__link-name btmarket__link-name--ellipsis show-for-desktop-medium"})
        listaApuestas = soup.findAll("div", {"class": "btmarket__selection"})

        matchList = []
        
        for item in matches:
            var = item.text + ': ' + listaApuestas[0].text + ' | ' +  listaApuestas[1].text + ' | ' +  listaApuestas[2].text
            matchList.append(var)

        return matchList
'''
    Get all football match on direct
'''
import requests 
from bs4 import BeautifulSoup
from urlvalidator import validate_url, ValidationError
from src import WilliamHillURLs  as whurls
import pandas as pd
import csv
import os


if __name__ == "__main__":

# --------------------------------------------------------------------------------------------------------------
    # myVariable = whurls.WilliamHillURLs()

    # #   0 - List all matches availables
    # ListURLs = myVariable.GetAllUrlMatches(urlSport=myVariable.URL_FootballOnDirect)

    # # for i in myVariable.GetAllUrlMatches(urlSport=myVariable.URL_FootballOnDirect):
    # #     print(i)

    # #   1 - Chose the first URL for example.
    # URL = ListURLs[1]

    # #   2 - Get web page and extract it.
    # req = requests.get(URL)
    # soup = BeautifulSoup(req.content.decode('utf-8','ignore'), "html.parser")

    # #   3 - Extract bet and the tittle.
    # aux = soup.findAll("button", {"class": ['btn betbutton oddsbutton']})

    # print(URL.encode())
    
    # #   4 - Print all bets and 
    # for i in aux:
    #     print(myVariable.ConvertFractionalBetToDecimalBet(i.text), ' ', i['data-name'])
# --------------------------------------------------------------------------------------------------------------
    import sys
    import time
    from datetime import datetime
    from requests_html import HTMLSession

    count = 0
    
    while( count < 1):

        myVariable = whurls.WilliamHillURLs()
        URL = myVariable.GetAllUrlMatches(myVariable.URL_FootballOnDirect)[0]

        req = requests.get(URL)
        soup = BeautifulSoup(req.content.decode('utf-8','ignore'), "html.parser")

        print('Count: ', count, ' - URL: ', URL)

        aux = soup.find('h2', {'class' : ['css-qbolbz']})
        allBets = soup.findAll("button", {"class": ['btn betbutton oddsbutton']})
        

        #result = soup.find_all(class_='tableCellMiddle mainScoreBox')
        result = soup.findAll('span', attrs={"class":"betbutton__odds"})
        print(result)

        # create an HTML Session object
        session = HTMLSession()
        
        # Use the object above to connect to needed webpage
        resp = session.get(URL)
        
        # Run JavaScript code on webpage
        resp.html.render()

        
        print(resp.html.find('span'))
        '''
        # for i in allBets:
        #     print(myVariable.ConvertFractionalBetToDecimalBet(i.text), ' ', i['data-name'])

        # print(aux)
        # print(len(aux))
        # print(aux.text)
        
        CSVFileName = aux.text.replace(' ','') + '.csv'
        
        pathCSVFile = '.././data/' + CSVFileName
        print(pathCSVFile)

        if not os.path.exists(pathCSVFile):
            
            if not os.path.exists('.././data/'):
                os.mkdir('.././data/')
            
            with open(pathCSVFile, 'a', newline='\n') as f:
                writer = csv.writer(f)
                f.close()
            df = pd.read_csv(pathCSVFile, header=0, names=['TimeStamp', 'LocalVictory', 'Draw', 'VisitanVictory','Result'])
            df.to_csv(pathCSVFile)

        now = datetime.now()

        fields=[now.strftime("%d/%m/%Y %H:%M:%S"), myVariable.ConvertFractionalBetToDecimalBet(allBets[0].text),
                    myVariable.ConvertFractionalBetToDecimalBet(allBets[1].text), 
                    myVariable.ConvertFractionalBetToDecimalBet(allBets[2].text),
                    result.text]
        
        with open(pathCSVFile, 'a', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            f.close()

        '''
        time.sleep(5) # Sleep 5 seconds
        
        count += 1
       
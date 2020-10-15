'''

    AUTOR: Javier Carracedo
    Github User: jke94
    File: SeleniumSpyder.py
    Date: 13/10/2020 

    SeleniumSpyder scrpit to get info about each football match in
        'https://sports.williamhill.es/betting/es-es/en-directo/fútbol" 
    web page.

    For each football match displayed in the web page, the script create a csv file
    to store info about:

        -   Time Stamp
        -   Match Time stamp 
        -   Local Team name 
        -   Visitant Team name
        -   Local Team Goals
        -   Visitant Team Goals

'''

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from time import sleep
from urllib.parse import unquote
from urlvalidator import validate_url, ValidationError
import csv
from spydermoduler.FootballMatchEvent import FootballMatchEvent

# Path of Chrome Web Driver
PATH = "../tools/chromedriver.exe"

# William Hill url with matchs footballs on direct.
URL_BASE = "https://sports.williamhill.es/betting/es-es/en-directo/fútbol"

# Number of seconds that program is paused until again execution (Variable that can be modified by the user)
SLEEP_SECONDS = 1

# Number of web shots are captured by match and printed in csv file with the information (Variable that can be modified by the user).
NUMBER_OF_WEB_SHOTS = 10

# Script main
if __name__ == "__main__":

    now = datetime.now()
    logFileName = './../logs/sypderLog.log'
    logging.basicConfig(filename=logFileName, level=logging.INFO)
    logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '|| ' + 'SPYDER START.')


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
    logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '|| ' + 'Created Chrome Web driver instance.')

    driver.get(URL_BASE)

    try:

        count = 0

        while (count < NUMBER_OF_WEB_SHOTS):

            footballMatchsEventsList = []

            # Get from URL_BASE time, actual result, match name and url match.

            matches = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@class='btmarket__name btmarket__name--featured']"))
            )

            resultsTeamA = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[@class='btmarket__livescore-item team-a']"))
            )

            resultsTeamB = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[@class='btmarket__livescore-item team-b']"))
            )

            timeMatches = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//label[@class='wh-label btmarket__live go area-livescore event__status']"))
            )
            
            localVisitantsTeamsNames = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='btmarket__link-name btmarket__link-name--ellipsis show-for-desktop-medium']"))
            )

            matchTimeList = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//label[@class='wh-label btmarket__live go area-livescore event__status']"))
            )

            betList = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[@class='betbutton__odds']"))
            )
            
            zipedLists = zip(matches, resultsTeamA, resultsTeamB, timeMatches, localVisitantsTeamsNames, matchTimeList)

            logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '|| ' + 'Number of matches played on direct: ' + str(len(matches)))

            for item in zipedLists:

                url = unquote((item[0].get_attribute("href")))
                
                footballMatchsEventsList.append(FootballMatchEvent(url, item[0].text, item[1].text, item[2].text, item[5].text))

            for item in footballMatchsEventsList:
                
                now = datetime.now()

                fields=[str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")), 
                        item.MatchTimeInstant, 
                        item.LocalTeamName, item.VisitantTeamName, 
                        item.LocalTeamGoals, item.VisitantTeamGoals,
                        'N/A', 'N/A', 'N/A'] # TODO: Added the bets.
                                       
                with open(item.PathDataFileEvent, 'a', newline='\n') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
                    f.close()

            matches.clear()
            resultsTeamA.clear()
            resultsTeamB.clear()
            timeMatches.clear()
            localVisitantsTeamsNames.clear()
            matchTimeList.clear()
            footballMatchsEventsList.clear()

            count += 1
            logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '|| ' + 'Created new data shot.')

            sleep(SLEEP_SECONDS)

    except Exception as e:
        print("ERROR", str(e))
        logging.error("ERROR", str(e))
        driver.quit()

    # Closed driver.
    driver.quit()
    logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '|| ' + 'SPYDER FINISHED')
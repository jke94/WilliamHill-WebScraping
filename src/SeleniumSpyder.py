'''

    AUTOR: Javier Carracedo
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
from time import sleep
from urllib.parse import unquote
from urlvalidator import validate_url, ValidationError
import csv
import FootballMatchEvent

# Path of Chrome Web Driver
PATH = "../Tools/chromedriver.exe"

# William Hill url with matchs footballs on direct.
URL_BASE = "https://sports.williamhill.es/betting/es-es/en-directo/fútbol"

# Number of seconds that program is paused until again execution (Variable that can be modified by the user)
SLEEP_SECONDS = 1

# Number of web shots are captured by match and printed in csv file with the information (Variable that can be modified by the user).
NUMBER_OF_WEB_SHOTS = 10

# Script main
if __name__ == "__main__":

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

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

            for (item, itemResultTeamA, itemResultTeamB, itemTimeMatches, itemlocalVisitantsTeamsNames, itemMatchTimeList) in zip(matches, resultsTeamA, resultsTeamB, timeMatches, localVisitantsTeamsNames, matchTimeList):

                url = unquote((item.get_attribute("href")))
                
                footballMatchsEventsList.append(FootballMatchEvent.FootballMatchEvent(url, item.text,itemResultTeamA.text, itemResultTeamB.text, itemMatchTimeList.text))

            for item in footballMatchsEventsList:
                
                now = datetime.now()

                fields=[    now.strftime(   "%d/%m/%Y %H:%M:%S"), item.MatchTimeInstant, 
                                            item.LocalTeamName, item.VisitantTeamName, 
                                            item.LocalTeamGoals, item.VisitantTeamGoals,
                                            'N/A', 'N/A', 'N/A',
                        ]
                
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

            sleep(SLEEP_SECONDS)

    except Exception as e:
        print("ERROR", str(e))
        driver.quit()

    # Closed driver.
    driver.quit()

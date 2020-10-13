#_*_coding: utf-8_*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urlvalidator import validate_url, ValidationError
from datetime import datetime
from time import sleep
from urllib.parse import unquote
import csv
import FootballMatchEvent
 
PATH = "../Tools/chromedriver.exe"
URL_BASE = "https://sports.williamhill.es/betting/es-es/en-directo/fútbol"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

driver.get(URL_BASE)

try:

    count = 0

    while (count < 5):

        footballMatchsEventsList = []

        # Get from URL_BASE time, actual result, match name and url match.

        # matches = driver.find_elements_by_xpath("//a[@class='btmarket__name btmarket__name--featured']")

        matches = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@class='btmarket__name btmarket__name--featured']"))
        )

        # resultsTeamA = driver.find_elements_by_xpath("//span[@class='btmarket__livescore-item team-a']")

        resultsTeamA = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@class='btmarket__livescore-item team-a']"))
        )

        # resultsTeamB = driver.find_elements_by_xpath("//span[@class='btmarket__livescore-item team-b']")

        resultsTeamB = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@class='btmarket__livescore-item team-b']"))
        )

        # timeMatches =  driver.find_elements_by_xpath("//label[@class='wh-label btmarket__live go area-livescore event__status']")

        timeMatches = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//label[@class='wh-label btmarket__live go area-livescore event__status']"))
        )
        
        # localVisitantsTeamsNames = driver.find_elements_by_xpath("//div[@class='btmarket__link-name btmarket__link-name--ellipsis show-for-desktop-medium']")

        localVisitantsTeamsNames = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='btmarket__link-name btmarket__link-name--ellipsis show-for-desktop-medium']"))
        )

        # matchTimeList = driver.find_elements_by_xpath("//label[@class='wh-label btmarket__live go area-livescore event__status']")

        matchTimeList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//label[@class='wh-label btmarket__live go area-livescore event__status']"))
        )

        # betList = driver.find_elements_by_xpath("//span[@class='betbutton__odds']") # len = Number of matches * 3

        betList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@class='betbutton__odds']"))
        )

        for (item, itemResultTeamA, itemResultTeamB, itemTimeMatches, itemlocalVisitantsTeamsNames, itemMatchTimeList) in zip(matches, resultsTeamA, resultsTeamB, timeMatches, localVisitantsTeamsNames, matchTimeList):

            url = unquote((item.get_attribute("href")))
            
            footballMatchsEventsList.append(FootballMatchEvent.FootballMatchEvent(url, item.text,itemResultTeamA.text, itemResultTeamB.text, itemMatchTimeList.text))

        for item in footballMatchsEventsList:
            
            now = datetime.now()

            fields=[now.strftime(   "%d/%m/%Y %H:%M:%S"), item.MatchTimeInstant, 
                                    item.LocalTeamName, item.VisitantTeamName, 
                                    item.LocalTeamGoals, item.VisitantTeamGoals]
            
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

        sleep(1) # Sleep 5 seconds

except Exception as e:
    print("ERROR", str(e))
    driver.quit()



# Close.
driver.quit()

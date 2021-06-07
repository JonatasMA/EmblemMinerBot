import pygetwindow as gw
import pyautogui as pg, PIL.ImageGrab
from time import sleep

leagueClient = gw.getWindowsWithTitle('League of Legends')[0]
leagueClient.minimize()
leagueClient.restore()

xAcceptButton = leagueClient.left + 640
yAcceptButton = leagueClient.top + 557

def getPixelColor(x, y):
    return PIL.ImageGrab.grab().load()[x, y]


defaultPixelColor = getPixelColor(xAcceptButton, yAcceptButton)
acceptButtonColor = (30, 37, 42)
pingBallColor = (38, 78, 52)
mapCenterColor = (17, 53, 50)


def arrayFilter(haystack, needle):
    for x in haystack:
        if (x == needle):
            return True
    return False

def moveAndClick(x, y):
    pg.moveTo(x, y, 1)
    pg.mouseDown()
    sleep(0.2)
    pg.mouseUp()

def clickOnAcceptButton():
    xFindQueue = leagueClient.left + 539
    yFindQueue = leagueClient.top + 678
    pg.moveTo(xFindQueue, yFindQueue, 1)
    pg.click()

def clickOnAcceptGame():
    pg.moveTo(xAcceptButton, yAcceptButton, 1)
    pg.click()

def checkGameExists():
    allWindows = gw.getAllTitles()
    arrayFilter(allWindows, 'League of Legends (TM) Client')


while True:
    clickOnAcceptButton()

    while (True):
        if (getPixelColor(xAcceptButton, yAcceptButton) == acceptButtonColor):
            clickOnAcceptGame()
            sleep(10)
            break

    while (True):
        if (checkGameExists()):
            leagueGameClient = gw.getWindowsWithTitle('League of Legends (TM) Client')[0]
            sleep(5)
            xPingBall = leagueGameClient.left + 25
            yPingBall = leagueGameClient.top + 42
            if (getPixelColor(xPingBall, yPingBall) == pingBallColor):
                break
    
    levelColor = (240, 230, 210)
    xLevel = leagueGameClient.left + 237
    yLevel = leagueGameClient.top + 767

    secondsLeft = 900
    while (secondsLeft > 0):
        secondsLeft = secondsLeft - 1
        sleep(1)

        if (getPixelColor(xLevel, yLevel) == levelColor):
            championsRow = leagueGameClient.top + 852
            firstChampion = leagueGameClient.left + 479

            def buyChampion(position):
                pixelsBetweenChampions = 170
                champion = firstChampion + ((position - 1) * pixelsBetweenChampions)
                moveAndClick(champion, championsRow)

            def buyXp():
                yXp = leagueGameClient.top + 830
                xXp = leagueGameClient.left + 307
                moveAndClick(xXp, yXp)

            if (secondsLeft == 830):
                buyChampion(1)
                buyChampion(4)

            if (secondsLeft == 775):
                buyChampion(2)

            if (secondsLeft == 709):
                buyChampion(1)
                buyXp()

            if (secondsLeft == 660):
                buyChampion(3)

            if (secondsLeft == 590):
                buyChampion(2)

            if (secondsLeft == 320):
                buyChampion(2)
                buyXp()

            if (secondsLeft == 260):
                buyXp()
                buyChampion(1)
                buyChampion(4)

            if (secondsLeft == 60):
                buyXp()
    break

# xPingBall = leagueGameClient.left + 41
# yPingBall = leagueGameClient.top + 25
# xMapWhiteCorner =  leagueGameClient.left + 838
# xMapCenterCorner = leagueGameClient.left + 841
# yMapCenterCorner = leagueGameClient.top + 1515
# print(leagueClient.width)
# print(leagueClient.height)
# print(leagueClient.top)
# print(leagueClient.left)

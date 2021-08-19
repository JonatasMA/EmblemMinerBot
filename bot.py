import pygetwindow as gw
import pyautogui as pg
import PIL.ImageGrab
from time import sleep
import random

# Um comentário desnecessário

leagueClient = gw.getWindowsWithTitle('League of Legends')[0]
lastChampionPosition = 1


def randomChampionPosition():
    global lastChampionPosition
    newChampionPosition = random.randint(1, 5)
    if (newChampionPosition != lastChampionPosition):
        lastChampionPosition = newChampionPosition
        return newChampionPosition
    else:
        return randomChampionPosition()


def bringClientToTop():
    leagueClient.minimize()
    leagueClient.restore()


bringClientToTop()

xAcceptButton = leagueClient.left + 640
yAcceptButton = leagueClient.top + 557


def getPixelColor(xAxis, yAxis):
    return PIL.ImageGrab.grab().load()[xAxis, yAxis]


defaultPixelColor = getPixelColor(xAcceptButton, yAcceptButton)
acceptButtonColor = (30, 37, 42)
pingBallColor = (38, 82, 55)
mapCenterColor = (17, 53, 50)


def arrayFilter(haystack, needle):
    for x in haystack:
        if (x == needle):
            return True
    return False


def moveAndClick(xAxis, yAxis):
    pg.moveTo(xAxis, yAxis, 1)
    pg.mouseDown()
    sleep(0.5)
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
    return arrayFilter(allWindows, 'League of Legends (TM) Client')


def buyChampion(position):
    pixelsBetweenChampions = 170
    champion = firstChampion + ((position - 1) * pixelsBetweenChampions)
    moveAndClick(champion, championsRow)


def buyXp():
    yXp = leagueGameClient.top + 830
    xXp = leagueGameClient.left + 307
    moveAndClick(xXp, yXp)


def checkEndGameLose():
    defaulCloseGameColor = (200, 155, 60)
    closeGameColor = getPixelColor(xCloseGame, yCloseGame)
    print(defaulCloseGameColor, closeGameColor)
    return defaulCloseGameColor == closeGameColor


def checkEndGameVictory():
    defaulCloseGameColorVictory = (186, 23, 18)
    closeGameColorVictory = getPixelColor(xCloseGameVictory, yCloseGameVictory)
    return defaulCloseGameColorVictory == closeGameColorVictory


while True:
    clickOnAcceptButton()
    print('encontrar partida')

    while (True):
        if (getPixelColor(xAcceptButton, yAcceptButton) == acceptButtonColor):
            clickOnAcceptGame()
            print('aceitar partida')
            sleep(5)
            # if (getPixelColor(xAcceptButton, yAcceptButton) == acceptButtonColor):
            break

    leagueGameClient = gw.getWindowsWithTitle(
        'League of Legends (TM) Client')[0]
    while (True):
        if (checkGameExists()):
            leagueGameClient = gw.getWindowsWithTitle(
                'League of Legends (TM) Client')[0]
            sleep(5)
            xPingBall = leagueGameClient.left + 25
            yPingBall = leagueGameClient.top + 42
            if (getPixelColor(xPingBall, yPingBall) == pingBallColor):
                print('partida iniciada')
                break

    levelColor = (240, 230, 210)
    xLevel = leagueGameClient.left + 237
    yLevel = leagueGameClient.top + 767
    xDefeatedGame = leagueGameClient.left + 812
    yDefeatedGame = leagueGameClient.top + 356
    xCloseGame = leagueGameClient.left + 690
    yCloseGame = leagueGameClient.top + 485
    xCloseGameVictory = leagueGameClient.left + 810
    yCloseGameVictory = leagueGameClient.top + 554

    while (True):
        sleep(5)

        if (getPixelColor(xLevel, yLevel) == levelColor):
            championsRow = leagueGameClient.top + 852
            firstChampion = leagueGameClient.left + 479

            randomValue = randomChampionPosition()
            if (randomValue == 1):
                buyChampion(randomChampionPosition())
                buyChampion(randomChampionPosition())

            if (randomValue == 2):
                buyChampion(randomChampionPosition())

            if (randomValue == 3):
                buyChampion(randomChampionPosition())
                buyXp()

            if (randomValue == 4):
                buyXp()
                buyChampion(randomChampionPosition())
                buyChampion(randomChampionPosition())

            if (randomValue == 5):
                buyXp()

            print('ação tomada')

        if (checkEndGameLose()):
            moveAndClick(xCloseGame, yCloseGame)
            print('derrota')
            sleep(20)
            bringClientToTop()
            clickOnAcceptButton()
            break

        if (checkEndGameVictory()):
            moveAndClick(xCloseGameVictory, yCloseGameVictory)
            print('vitória')
            sleep(20)
            bringClientToTop()
            clickOnAcceptButton()
            break

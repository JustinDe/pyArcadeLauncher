import pygame as pg
from pygame.locals import *
import pygame.gfxdraw
from gameToolBelt import randColor 
import webbrowser
import json

with open('manifest.json') as gameList:
	gl = json.load(gameList)

pg.init()
pg.display.set_caption("Strangelet-Studios")
screen = pg.display.set_mode((800,600))
#screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

resolution = screen.get_size()
w_height = resolution[1]
w_width = resolution[0] 

x_drawLoc = 0
polyLocs = []
def drawOptions():
	global x_drawLoc
	global polyLocs
	polyLocs = []
	x_drawLoc = 0
	for game in gl['Games']:
		commonPoly = (
			(((w_width*.02)+x_drawLoc), (w_height*.05)),
			(((w_width*.70)/len(gl['Games'])+x_drawLoc), (w_height*.05)),
			(((w_width*.70)/len(gl['Games']))+((w_width*.70)/len(gl['Games']))+x_drawLoc, (w_height*.95)),
			(((w_width*.70)/len(gl['Games']))+(w_width*.02)+x_drawLoc, (w_height*.95))
			)

		pygame.gfxdraw.textured_polygon(screen, commonPoly, pg.image.load(game['Image']), 0, 0)
		polyLocs.append(commonPoly)

		x_drawLoc += (((w_width*.03)/len(gl['Games']))+((w_width*.70)/len(gl['Games'])))+((w_width*.02)/len(gl['Games']))

drawOptions()

#this needs to be majorly refactored
count = 1
curColor = randColor()
nextColor = randColor()
lastcolor = randColor()
def redrawSelectBorder():	
	global count
	global curColor
	global nextColor
	global lastcolor

	if count == 4:
		for x in range(0,len(polyLocs)):
			pg.draw.line(screen, curColor, polyLocs[x][0], polyLocs[x][1], 5)
			pg.draw.line(screen, curColor, polyLocs[x][1], polyLocs[x][2], 5)
			pg.draw.line(screen, curColor, polyLocs[x][2], polyLocs[x][3], 5)
			pg.draw.line(screen, curColor, polyLocs[x][3], polyLocs[x][0], 5)
		count = 0

	if count == 3:
		for x in range(0,len(polyLocs)):
			pg.draw.line(screen, curColor, polyLocs[x][0], polyLocs[x][1], 5)
			pg.draw.line(screen, curColor, polyLocs[x][1], polyLocs[x][2], 5)
			pg.draw.line(screen, curColor, polyLocs[x][2], polyLocs[x][3], 5)
			pg.draw.line(screen, lastcolor, polyLocs[x][3], polyLocs[x][0], 5)
		count += 1
	
	if count == 2:
		for x in range(0,len(polyLocs)):
			pg.draw.line(screen, curColor, polyLocs[x][0], polyLocs[x][1], 5)
			pg.draw.line(screen, curColor, polyLocs[x][1], polyLocs[x][2], 5)
			pg.draw.line(screen, lastcolor, polyLocs[x][2], polyLocs[x][3], 5)
			pg.draw.line(screen, lastcolor, polyLocs[x][3], polyLocs[x][0], 5)
		count += 1

	if count == 1:
		for x in range(0,len(polyLocs)):
			pg.draw.line(screen, curColor, polyLocs[x][0], polyLocs[x][1], 5)
			pg.draw.line(screen, lastcolor, polyLocs[x][1], polyLocs[x][2], 5)
			pg.draw.line(screen, lastcolor, polyLocs[x][2], polyLocs[x][3], 5)
			pg.draw.line(screen, lastcolor, polyLocs[x][3], polyLocs[x][0], 5)
		count += 1
	
	if count == 0:
		count = 1
		lastcolor = curColor
		curColor = randColor()
		
pg.time.set_timer(USEREVENT + 1, 50)

selectedGame = 0

def gameSelection(selectedGame):
	pygame.gfxdraw.filled_polygon(screen, polyLocs[selectedGame], (77,121,255,100))

gameSelection(selectedGame)

def wipeScreen():
	screen.fill
	screen.set_alpha(255)

active = True
while active:
    for event in pg.event.get():
    	if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selectedGame -= 1
                if selectedGame <= 0:
                	selectedGame = 0
                wipeScreen
                drawOptions()
                gameSelection(selectedGame)
            if event.key == pygame.K_RIGHT:
            	selectedGame += 1
            	if selectedGame >= len(gl['Games'])-1:
            		selectedGame = len(gl['Games'])-1
            	wipeScreen
            	drawOptions()
            	gameSelection(selectedGame)
    	if event.type == USEREVENT + 1:
    		redrawSelectBorder()
        if event.type == pg.QUIT:
            active = False
    pg.display.update()
pg.quit()
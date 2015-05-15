#x_drawLoc = 0
#for game in gl['Games']:
#
#	pg.draw.rect(screen,(255,255,255),(
#		((w_width*.05)+x_drawLoc),    #x loc
#		(w_height*.05),    #y loc
#		((w_width*.80)/len(gl['Games'])),  #width
#		(w_height*.90)  #height
#		))
#	x_drawLoc += (((w_width*.10)/len(gl['Games']))+((w_width*.80)/len(gl['Games'])))+((w_width*.05)/len(gl['Games']))
#	print x_drawLoc
#
#	#screen.blit(pg.image.load("Test.jpg"),(0,0))
#
#import json
#
#with open('manifest.json') as gameList:
#	gl = json.load(gameList)
#
#print gl['Games']
#
#myfont = pg.font.SysFont("monospace", 40)
#selectedGameLabel = myfont.render(gl['Games'][0]['Title'], 1, (255,255,255))
#screen.blit(selectedGameLabel, (w_width*.30, w_height*.85))
# importiert pygame und random
import pygame
import random
# inintialisiert pygame
pygame.init()
width = 600
height = 600

# erstellt eine 'surface' (Oberfläche) und setzt die Höhe und Breite
window = pygame.display.set_mode((width, height))


pygame.display.set_caption("Snek") # setzt die Überschrift des Programmes

x = width / 2 - 13 # position spieler
y = height / 2 # position spieler
charWidth = 25 # spielergroesse
charHeight = 25 # spielergroesse
speed = 5 # geschwindigkeit der Hindernisse
xEnemy1 = width 						# startposition der enemies
yEnemy1 = random.randint(0, height)	# --
xEnemy2 = random.randint(0, width)	# --
yEnemy2 = -50						# --
xEnemy3 = width						# --
yEnemy3 = random.randint(0, height)	# --
xEnemy4 = random.randint(0, width)	# --
yEnemy4 = -50						# --
enemyWidth1 = 180					# groesse enemies
enemyHeight1 = 10					# --
enemyHeight2 = 180					# --
enemyWidth2 = 10					# --
enemyWidth3 = 180					# --
enemyHeight3 = 10					# --
enemyHeight4 = 50					# --
enemyWidth4 = 50					# --
r = 0								# farbe enemies
g = 255								# --
b = 0								# --
run = True
wonnn = False
verloren = False						# 'main' Schleife wird auf 'True' gesetzt
cc = 0								# zähler, zählt score, farbänderung etc.
pSpeed = 5							# geschwindikeit 'player'
score = cc / 10						# score wird berechnet
black = (255, 255, 255)				# farbe Schwarz
font = pygame.font.SysFont(None, 25) # schriftart und groesse wird definiert
win = pygame.font.SysFont(None, 40)
text = font.render("Score: "+ str(score), True, black)	# renderung des textes
adrian = font.render("by Adrian Qehaja", True, black)	# --

counters = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 15000]	# liste mit Zahlen wo eine Erhöhung der Geschwindigkeit stattfindet





while (run):	# 'main' schleife wird gestartet
	pygame.time.delay(15)	# 'fps' werden gesetzt 
	keys = pygame.key.get_pressed() # varibale 'keys' wird definiert (alle tasten die gedrueckt werden)
	

	for event in pygame.event.get(): # for schleife welches events einsammelt
		if event.type == pygame.QUIT:	# abfrage ob event typ 'fenster schliessen' entspricht
			run = False					# wenn ja -> schleife beendet

	if keys[pygame.K_LEFT] and x > pSpeed:						#	Bewegung des Charakters mit komplizierteren IF- Abfragen
		x -= pSpeed												#			|-------------------|
																#			|xy0			x500|
	if keys[pygame.K_RIGHT] and x < width - charWidth - pSpeed:	#			|					|
		x += pSpeed												#			|					|
																#			|					|
	if keys[pygame.K_UP] and y > pSpeed:						#			|					|
		y -= pSpeed												#			|					|
																#			|					|
	if keys[pygame.K_DOWN] and y < height - charHeight - pSpeed:#	 		|y500		   xy500|
		y += pSpeed												#			|-------------------|



	
	enemy1 = pygame.draw.rect(window, (r, g, b), (xEnemy1, yEnemy1, enemyWidth1, enemyHeight1 ))	# alle objekte werden erstellt
	enemy2 = pygame.draw.rect(window, (r, g, b), (xEnemy2, yEnemy2, enemyWidth2, enemyHeight2 ))	# --
	enemy3 = pygame.draw.rect(window, (r, g, b), (xEnemy3, yEnemy3, enemyWidth3, enemyHeight3 ))	# --
	enemy4 = pygame.draw.rect(window, (r, g, b), (xEnemy4, yEnemy4, enemyWidth4, enemyHeight4 ))	# --
																									# --
	rect1 = pygame.draw.rect(window, (255, 255, 255), (x, y, charWidth, charHeight))				# --
	

	if rect1.colliderect(enemy1) or rect1.colliderect(enemy2) or rect1.colliderect(enemy3) or rect1.colliderect(enemy4): # ueberprueft auf kollisionen                
		verloren = True
		run = False		# wenn bedingung zutrifft, main schleife beendet
		print("Game Over")	# konsolenausgabe


	if xEnemy1 < 0:												# kurz gefasst, wird bei jedem enemy überprüft ob dieser
		xEnemy1 = random.randint(width, width + 200)						# noch innerhalb des spielfeldes ist. falls nicht wird dieser
		yEnemy1 = random.randint(0, height)						# wieder auf die andere seite des spielfeldes gebracht	
		r = random.randint(0, 255)								# --
		g = random.randint(0, 255)								# --
		b = random.randint(0, 255)								# --
																# --
	if yEnemy2 > height:										# --
		yEnemy2 = random.randint(-200, -50)						# --
		xEnemy2 = random.randint(0, width)						# --
		r = random.randint(0, 255)								# --
		g = random.randint(0, 255)								# --
		b = random.randint(0, 255)								# --
																# --
	if xEnemy3 < 0:												# --
		xEnemy3 = random.randint(width, width + 200)			# --
		yEnemy3 = random.randint(0, height)						# --
		r = random.randint(0, 255)								# --
		g = random.randint(0, 255)								# --
		b = random.randint(0, 255)								# --
																# --
	if yEnemy4 > height:										# --
		xEnemy4 = random.randint(0, width)						# --
		yEnemy4 = -50											# --
		r = random.randint(0, 255)								# --
		g = random.randint(0, 255)								# --
		b = random.randint(0, 255)								# --
		
	if cc in counters:					# ueberpruefung ob aktueller count in der liste counters ist 
		speed += 1						# wenn bedingung zutrifft wird die geschwindigkeit erhoeht


	if cc > 500:						# wenn count über 500 ist kommen die herunterfallenden blöcke ins spiel
		yEnemy4 += speed   				# --

	yEnemy2 += speed					# bewegung der gegner
	xEnemy1 -= speed 					# --
	xEnemy3 -= speed 					# --
	yEnemy3 += speed 					# --

	window.blit(text, (2,2))			# text wird angezeigt
	window.blit(adrian, (width - 150, height - 20))
	text = font.render("Score: "+ str(score), True, black)
	pygame.display.update()				# screen wird geupdated
	window.fill((0, 0, 0))				# hintergrundfarbe spiel

	cc += 1								# counter zählt hoch
	score = cc / 10						# score wird berechnet


if verloren == True:
	lost = win.render("YOU HAVE LOST!", True, black)
	window.blit(lost, (width / 2 - 110, height / 2))
	pygame.display.update()
	pygame.time.delay(2000)
										
print("You have reached a score of", score, "points!")
pygame.quit()							# wenn schleife auf false gesetzt wird wird das spiel beendet

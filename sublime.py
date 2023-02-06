from pygame import *

init()

win = display.set_mode((1366, 768))

display.set_mode("Названия приложения")

x = 60
y = 706
wight = 40
height = 40
speed = 5

isJump = False
jumpCount = 10

while True:
	for event in event.get():
		if event.type == QUIT:
			quit()

	keys = key.get_pressed()
	if keys[K_LEFT] and x > 20:
		x-= speed
	if keys[K_RIGHT] and 1366 - wight - 20:
		x+= speed
	if not(isJump):
		if keys[K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 4
			else:
				y -= (jumpCount ** 2) / 4
			jumpCount -= 1
		else:
		    isJump = False
		    jumpCount = 10

	win.fill(("#00C0C6FF"))
	draw.rect(win, (0, 0, 255), (x, y, wight, height))
	draw.rect(win, (0, 255, 0), (0, 748, 1366, 20))
	draw.rect(win, (90, 90, 90), (0, 0, 20, 746))
	draw.rect(win, (90, 90, 90), (1346, 0, 20, 746))
	draw.rect(win, (90, 90, 90), (20, 0, 1326, 20))
	
	clock.tick(60)
	display.update()

quit()	

	
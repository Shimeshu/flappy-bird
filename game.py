import pygame

pygame.init()
pygame.mixer.init()

musicfile = "audio/point.wav"
win = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird")

bg_day = pygame.image.load("sprites/background-day.png")

bird = [pygame.image.load("sprites/yellowbird-midflap.png"), pygame.image.load("sprites/yellowbird-downflap.png"),
pygame.image.load("sprites/yellowbird-upflap.png")]

pipes = [pygame.image.load("sprites/pipe-green.png"),
pygame.image.load("sprites/pipe-green.png")]

base = [pygame.image.load("sprites/base.png")]

icon = pygame.image.load("favicon.ico")
pygame.display.set_icon(icon)

game_over = pygame.image.load("sprites/gameover.png")

clock = pygame.time.Clock()


run = True

class Bird:
	def __init__(self, x, y, vel) -> None:
		self.x = x
		self.y = y
		self.vel = vel
		self.checkGroundTouch = False
		self.checkBirdDirection = ""


	def draw_and_move(self, win):
		win.blit(bg_day, (0, 0))
		win.blit(base[0], (0, 450))
		if self.checkBirdDirection == "up":
			win.blit(bird[2], (self.x, self.y))
		if self.checkBirdDirection == "down":
			win.blit(bird[1], (self.x, self.y))

	def checkGround(self):
		if self.y >= 512 - 78 - self.vel:
			win.fill((0,0,0))
			win.blit(bg_day, (0,0))
			self.y = 1000000
			win.blit(game_over, (50, 200))

class Pipes():
	def __init__(self, x, x1, y, y1, vel):
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.vel = vel
		self.newpipe = False
		self.jcount = 1


	def draw(self, win):
		if self.x1 >= - 40:
			win.blit(pipes[0], (self.x, self.y))
			win.blit(pygame.transform.flip(pipes[1], True, True), (self.x1, self.y1))
			self.x -= 5
			self.x1 -= 5
		elif self.x1 >= -45:
				if self.jcount <= 2:
					self.x = 380
					self.y += 5 * 15
					self.jcount += 1
					self.x1 = 380
					self.y1 += 5 * 15
				else:
					self.x = 380
					self.y = 200
					self.y1 = -240
					self.x1 = 380
					self.jcount -= 2
		win.blit(base[0], (0, 450))


class ScoringSystem():
	def __init__(self):
		self.scorecount = 0

	def countscore(self):
		if obstaclepipes.x == 35 and not(flappybird.y >= 512 - 78 - flappybird.vel):
			file = open("Score.txt", "r+")
			self.scorecount += 1
			pygame.mixer.music.load(musicfile)
			pygame.mixer.music.play(1)
			file.write("Recent Score = " + str(self.scorecount))
			print("Score = ", self.scorecount)
			file.close()


flappybird = Bird(20, 220, 5)
obstaclepipes = Pipes(380, 380, 220, -220, 4)
score = ScoringSystem()


def drawOnScreen():
	win.fill((0, 0, 0))
	flappybird.draw_and_move(win)
	obstaclepipes.draw(win)
	score.countscore()
	flappybird.checkGround()
	pygame.display.update()

def showstartScreen():
	key = pygame.key.get_pressed()
	start = [pygame.image.load("sprites/message.png")]
	win.blit(bg_day, (0, 0))
	win.blit(start[0], (60, 100))


while run:
	clock.tick(35)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()

	if key[pygame.K_UP]:
		flappybird.checkBirdDirection = "up"
		flappybird.y -= flappybird.vel
		flappybird.y -= 6
	else:
		flappybird.checkBirdDirection = "down"
		flappybird.y += 5
	drawOnScreen()


pygame.quit()
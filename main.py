import pgzrun
import random

WIDTH = 800
HEIGHT = 800

shooter = Actor('player')
shooter.x = WIDTH//2
shooter.y = HEIGHT-250


lasers = []

enemies = []

for x in range(8):
  enemies.append(Actor('alien1'))
  enemies[-1].x = 100 + 90*x
  enemies[-1].y = 80


score = 0
direction = 1

def drawScore():
  screen.draw.text(str(score),(50,30))


def on_key_down(key):
  if key == keys.SPACE:
    lasers.append(Actor('laser1'))
    lasers[-1].x = shooter.x
    lasers[-1].y = shooter.y

def update():
  global score
  global direction
  if keyboard.left:
    shooter.x -= 5
  elif keyboard.right:
    shooter.x += 5
  if keyboard.space:
  

   
    for laser in lasers:
      if laser.y < 20:
        lasers.remove(laser)
      else:
        laser.y -= 10
  
    for enemy in enemies:
      enemy.y += 10
      if enemy.y > HEIGHT + 60:
        enemy.y = 100
        enemy.x = random.randint(40,WIDTH-40)
    
      for laser in lasers:
        if enemy.colliderect(laser):
          score += 150
          lasers.remove(laser)
          enemies.remove(enemy)



def draw():
  screen.clear()
  shooter.draw()
  for laser in lasers:
    laser.draw()
  for enemy in enemies:
    enemy.draw()
  drawScore()
  

pgzrun.go()
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

shooter = Actor('player')
shooter.x = WIDTH//2
shooter.y = HEIGHT-250
ship.dead = False


lasers = []

enemies = []

for x in range(8):
  for y in range(4):
    enemies.append(Actor('alien1'))
    enemies[-1].x = 100 + 90*x
    enemies[-1].y = 80 + 80*y


score = 0
direction = 1

def drawScore():
  screen.draw.text(str(score),(50,30))


def on_key_down(key):
  if shooter.dead == False:
    if key == keys.SPACE:
      lasers.append(Actor('laser1'))
      lasers[-1].x = shooter.x
      lasers[-1].y = shooter.y

def update():
  global score
  global direction
  if shooter.dead == False:
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
  moveDown = False
  if len(enemies)>0 and (enemies[-1].x > WIDTH-80 or enemies[0].x < 50):
    if enemies[-1].x > WIDTH-80:
      moveDown = True
    direction = direction*-1

    for enemy in enemies:
      enemy.y += 5*direction
      if moveDown == True:
        enemy.y += 1
      
      for laser in lasers:
        if enemy.colliderect(laser):
          score += 150
          lasers.remove(laser)
          enemies.remove(enemy)
      if enemy.colliderect(shooter):
        shooter.dead = True
        


def draw():
  screen.clear()
  if shooter.dead = False:
    shooter.draw()
  for laser in lasers:
    laser.draw()
  for enemy in enemies:
    enemy.draw()
  drawScore()
  

pgzrun.go()
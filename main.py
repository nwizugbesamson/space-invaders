from turtle import Screen
from player import Player
from enemies import Enemies
from scoreboard import ScoreBoard
import time
import random



# SLEEP TIME CONSTANT
SLEEP_TIME = 0.2

# RANDOM LIST TO CONTROL ENEMY BULLET ACTION
PICKER = range(1, 400)


# CREATE AND CONFIGURE SCREEN OBJECT
screen = Screen()
screen.title("SPACE INVADERS")
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=None, starty=0)

# STOP SCREEN UPDATE(ALLOWS FOR FRAME-RATE EFFECT WHEN USED WITH UPDATE METHOD AND TIME MODULE)
screen.tracer(0)

# INITIIALIZE ALL TURTLE OBJECTS BEFORE SCREEN UPDATE
player = Player()
enemies = Enemies()
scoreboard = ScoreBoard()


# LISTEN METHOD FOR KEYBOARD BINDS
# ALLOWS PROGRAM TO INTERACT WITH KEYBOARD
screen.listen()

# LOOP CONTOLLING BOOLEAN
gameplay = True

while gameplay:
    time.sleep(SLEEP_TIME)
    screen.update()

    

    # CHECK KILLS
    if player.bullet_turtle:
        for squad in enemies.enemy_battalion:
            # BOOLEAN TO BREAK NESTED FOR LOOP
            sq_loop_must_break = False
            for soldier in squad:
                if player.bullet_turtle.distance(soldier) <= 20:
                    player.bullet_kill()
                    enemies.kill_enemy(soldier)
                    scoreboard.score += 20
                    scoreboard.update_score()
                    sq_loop_must_break = True
                    break
            if sq_loop_must_break:
                break

    
    # CHECK DEATHS
    if len(enemies.bullets) > 1:
        for bul in enemies.bullets:
            if player.distance(bul) <= 20:
                enemies.kill_bullets(bul)
                scoreboard.life -= 1
                scoreboard.update_score()
                player.start()


    # CHECK GAMEOVER
    if scoreboard.life <= 0:
        scoreboard.game_over()
        gameplay = False

    # ENEMY MOVEMENT ACTION
    enemies.change_move()
    enemies.move()

    # PLAYER BULLET ACTION
    if player.has_shot:
        if player.bullet_turtle.ycor() >= 290:
            player.bullet_kill()
        else:
            player.bullet_turtle.fd(20)


    # ENEMY BULLET ACTION
    for squad in enemies.enemy_battalion:
        for soldier in squad:
            choice = random.choice(PICKER)
            if soldier not in enemies.active_soldiers and choice == 1:
                enemies.enemy_bullet(soldier)


    # ENEMY BULLET MOTION
    if len(enemies.bullets) > 1:
        for bul in enemies.bullets:
            if bul.ycor() <= -290:
                enemies.kill_bullets(bul)
            bul.bk(20)










    # BIND FUNCTIONS TO KEYS
    screen.onkeypress(key="Left", fun=player.move_left)
    screen.onkeypress(key="Right", fun=player.move_right)
    screen.onkeypress(key="a", fun=player.bullet)


# LOOP THAT KEEPS SCREEN ACTIVE UNTIL CLICK
screen.exitonclick()
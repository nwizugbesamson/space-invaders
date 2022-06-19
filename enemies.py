from turtle import Turtle
import random

class Enemies:

    def __init__(self):
        self.enemy_battalion = []
        self.create_battalion()
        self.bullets = []
        self.active_soldiers = []
        self.new_x = -10


    def create_soldier(self, color, x, y):
        soldier = Turtle(shape="turtle")
        soldier.penup()
        soldier.setheading(270)
        soldier.color(color)
        soldier.goto( x, y)
        return soldier

    def create_squad(self, color, y):
        squad_list = []
        x = -200
        for i in range(0, 10):
            soldier = self.create_soldier(color, x, y)
            x += 40
            squad_list.append(soldier)
        return squad_list


    def create_battalion(self):
        batt_dict = {
            "red": 170,
            "blue": 210,
            "green": 250,
            
        }
        for key, value in batt_dict.items():
            squad = self.create_squad(color=key, y=value)
            self.enemy_battalion.append(squad)


    # MOVEMENT METHOD FOR BATTALION
    def change_move(self):
        # distance = 40
        for squad in self.enemy_battalion:
            if self.new_x > 0:
                # reverses list to change wall location for each soldier
                squad = squad[::-1]
                start_wall = 370
                for  soldier in squad:
                    if soldier.xcor() >= start_wall:
                        self.reverse()
                        break
                   
            else:
                start_wall = -370
                for soldier in squad:
                    if soldier.xcor() <= start_wall:
                        self.reverse()
                        break
                  



    def move(self):
        for squad in self.enemy_battalion:
            for soldier in squad:
                soldier.goto(soldier.xcor()+self.new_x, soldier.ycor())
    

    def reverse(self):
        self.new_x *= -1
        


    def enemy_bullet(self, soldier):
        bullet = Turtle()
        bullet.penup()
        bullet.setheading(90)
        bullet.shape("square")
        bullet.color("orange")
        bullet.shapesize(stretch_len=0.5, stretch_wid=0.3)
        x, y = soldier.pos()
        bullet.goto(x, y=y-15)
        self.bullets.append(bullet)
        self.active_soldiers.append(soldier)


    def kill_bullets(self, bul):
        bul.goto(1000, 1000)
        index = self.bullets.index(bul)
        self.bullets.remove(bul)
        del self.active_soldiers[index]

    def kill_enemy(self, soldier):
        for squad in self.enemy_battalion:
            if soldier in squad:
                soldier.goto(1000, 1000)
                squad.remove(soldier)
            
         
            
        
                    
from turtle import Turtle
START_POSITION = (0, -270)


class Player(Turtle):
    
    def __init__(self) -> Turtle:
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.start()
        self.has_shot = False
        self.bullet_turtle = None 



    # PLAYER MOVEMENT TO THE LEFT
    # CALLS GOTO METHOD 10 PIXELS LESS THAN CURRENT PLAYER LOCATION ON XAXIS
    def move_left(self):
        if self.xcor() >= -370:
            x, y = self.pos()
            self.goto(x-20, y)


    # PLAYER MOVEMENT TO THE RIGHT
    # CALLS GOTO METHOD 10 PIXELS GREATER THAN CURRENT PLAYER LOCATION ON XAXIS
    def move_right(self):
        if self.xcor() <= 370:
            x, y = self.pos()
            self.goto(x + 20, y)


    # BULLET OBJECT AS TURTLE OBJECT
    def bullet(self) -> Turtle:
        # CHECKS IF PLAYER HAS SHOT BEFORE CREATING NEW BULLET
        if not self.has_shot:    
            bullet = Turtle()
            bullet.penup()
            bullet.setheading(90)
            bullet.shape("square")
            bullet.color("white")
            bullet.shapesize(stretch_len=0.5, stretch_wid=0.3)
            x, y = self.pos()
            bullet.goto(x=x, y=y+15)
            self.has_shot = True
            self.bullet_turtle = bullet

    # REMOVES BULLET FROM SCREEN AND SETS HAS_SHOT TO FALSE ALLOWING PLAYER SHOOT AGAIN
    def bullet_kill(self):
        self.bullet_turtle.goto(1000, 1000)
        self.bullet_turtle = 0
        self.has_shot = False


    def start(self):
        self.goto(START_POSITION)
        

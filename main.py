from turtle import *


class Sprite(Turtle):
    def __init__(self, x, y, step = 10, shape = 'circle', color = 'black'):
        super(). __init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step )
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor() )
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self. y_start)
        
    
    
    
t4 = Turtle()
t4.speed(0)
t4.color('black')
t4.width(3)
t4.shape('turtle')
t4.penup()
t4.goto(-200, 200)
t4.pendown()
for i  in range(4):
    t4.forward(400)
    t4.right(90)
t4.hideturtle()
t5  = Turtle()
t5.color('black')
t5.speed(0)
t5.width(1)
t5.shape('turtle')
t5.penup()
t5.goto(-200, 185)
t5.pendown()
t5.points = 0
t5.write(f'Счет: {t5.points}', font= ('Arial', 13, 'normal'))
t5.hideturtle()
player = Sprite(0, -150, 10, 'circle', 'orange')
target = Sprite(0, 175, 0, 'triangle', 'green' )
enemy1 = Sprite( -200, -50 , 10, 'square', 'red' )
enemy1.set_move(-200, -50, 200, -50)
enemy2 = Sprite(200, 50 , 10, 'square', 'red' )
enemy2.set_move(200, 50, -200, 50)
scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_down, 'Down')



total_score = 0

while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()
    if player.is_collide(target):
        player.goto(0, -150)
        total_score += 1
        t5.points += 1
        t5.clear()
        t5.write(f'Счет: {t5.points}', font= ('Arial', 13, 'normal'))
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        target.hideturtle()
        t5.penup()
        t5.goto(0,0)
        t5.pendown()
        t5.write('Ты проиграл!', font=('Arial', 20, 'normal'))
        break
if total_score >= 3:
    t5.penup()
    t5.goto(0,0)
    t5.pendown()
    t5.write('Ты выиграл!', font=('Arial', 20, 'normal'))
enemy1.hideturtle()
enemy2.hideturtle()





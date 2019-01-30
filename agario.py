import turtle
import time
import random 
import math
from ball import Ball
from turtle import *
turtle.tracer(0)
turtle.hideturtle()

turtle.bgpic("pp.gif")


# Game over set-up
turtle.register_shape("tenor.gif")
gameOverTurtle = turtle.Turtle()
gameOverTurtle.pu()
gameOverTurtle.hideturtle()
gameOverTurtle.goto(0,150)
gameOverTurtle.shape("tenor.gif")
##################


running = True 

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
my_ball = Ball(0,8,7,7,57,"green")
number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

BALLS =[]

for i in range (number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx , maximum_ball_dx)
	dy = random.randint(minimum_ball_dy , minimum_ball_dy)
	r = random.randint(minimum_ball_radius , maximum_ball_radius)
	color = (random.random() , random.random() , random.random())
	ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(ball)

def move_all_balls():
	for i in BALLS:
		i.move(screen_width,screen_height)

def collide (ball_a , ball_b):
	if ball_a == ball_b :
		return False
	distance = math.sqrt((math.pow(ball_b.pos()[0] - ball_a.pos()[0] , 2) + math.pow(ball_b.pos()[1] - ball_a.pos()[1],2)))
	radii = ball_a.r + ball_b.r
	if distance <= radii:
		return True
	else:
		return False	
		



def check_all_balls_collision():
        global running
        all_balls=[]
        all_balls.append(my_ball)
        for ball in BALLS:
                all_balls.append(ball)

        for ball_a in all_balls:
                for  ball_b in all_balls:
                        
                        if collide(ball_a,ball_b):
                                r1 = ball_a.r
                                r2 = ball_b.r
                                x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
                                y  = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
                                dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                                while dx == 0:
                                        dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                                dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                                while dy == 0:
                                        dy = random.randint(minimum_ball_dy , maximum_ball_dy)

                                r = random.randint(minimum_ball_radius , minimum_ball_radius)
                                color = (random.random() , random.random() , random.random())
                                if r1 >= r2:
                                        if ball_b == my_ball:
                                                running = False
                                                gameOverTurtle.showturtle()	
                                                print ("game over!")
                                        else:	
                                                ball_b.new_ball(x,y,dx,dy,r,color)
                                                ball_a.r = ball_a.r + 1
                                                ball_a.shapesize(ball_a.r/10)
                                else:
                                        if ball_a == my_ball:
                                                running = False
                                                gameOverTurtle.showturtle()	
                                                print ("game over!")
                                        else:
                                                ball_a.new_ball(x,y,dx,dy,r,color)
                                                ball_b.r = ball_b.r + 1
                                                ball_b.shapesize(ball_b.r/10)
def movearound(screen_width, screen_height):
	X_coordinate = turtle.getcanvas().winfo_pointerx() - screen_width
	Y_coordinate = screen_height - turtle.getcanvas().winfo_pointery()
	my_ball.goto(X_coordinate , Y_coordinate)

while running == True :
	if (screen_width != (turtle.getcanvas().winfo_width()/2)) or (screen_height!=(turtle.getcanvas().winfo_height()/2)):
		screen_width = turtle.getcanvas().winfo_width()/2
		screen_height = turtle.getcanvas().winfo_height()/2
	movearound(screen_width, screen_height) 
	move_all_balls()
	check_all_balls_collision()
	turtle.update()
	time.sleep(0.1)




turtle.mainloop()


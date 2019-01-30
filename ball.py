from turtle import *
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__ (self)
        self.x= x
        self.y= y
        self.dx= dx
        self.dy= dy
        self.r= r
        self.pu()
        self.goto(x,y)
        self.shape("circle")
        self.shapesize(self.r/10)
        self.color(color)
    def move(self, screen_width, screen_height):
        current_x= self.pos()[0]
        new_x= current_x + self.dx
        current_y= self.pos()[1]
        new_y= current_y + self.dy
        right_side_ball= new_x + (self.r/10)
        left_side_ball= new_x - (self.r/10)
        up_side_ball= new_y + (self.r/10)
        down_side_ball= new_y - (self.r/10)
        self.goto(new_x , new_y)
        if (left_side_ball <= -screen_width):
            self.dx = -self.dx
        if (right_side_ball >= screen_width):
            self.dx = -self.dx
        if (up_side_ball >= screen_height):
            self.dy = -self.dy
        if (down_side_ball <= -screen_height):
            self.dy = -self.dy
    def new_ball(self , x , y , dx , dy , r, color):
        self.x= x
        self.y= y
        self.dx= dx
        self.dy= dy
        self.r= r
        self.pu()
        self.goto(x,y)
        self.shape("circle")
        self.shapesize(self.r/10)
        self.color= (color)
            
            
            
            






        
    
    
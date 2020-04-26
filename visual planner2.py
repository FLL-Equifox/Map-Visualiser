#hit F5 or shift + f5 to start
#visual planner
import turtle
from turtle import Turtle,Screen

turtle.register_shape("robothead.gif")

intoOrbit = "map2.gif"
CityShaper = "City.gif"
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic(intoOrbit)
wn.title("equinox map of glory")
#wn.window_width = 4000
#wn.window_height = 2159

#instructions
text = turtle.Turtle()
text.turtlesize(1)
text.pu()
text.setposition(-680,-320)
text.ht()
text.write("number pad to move, c to clear, r to reset robot",font=("Arial", 23, "normal"))

#the robot
robot = turtle.Turtle()
robot.shape("robothead.gif")
robot.width(10)
robot.pu()
robot.goto(-600,-220)
robot.pd()

def dragging(x, y):
    robot.ondrag(None)
    robot.setheading(robot.towards(x, y))
    robot.goto(x, y)
    robot.ondrag(dragging)

def north():
    y=robot.ycor()+10
    robot.sety(y)
def south():
    y=robot.ycor()-10
    robot.sety(y)
def east():
    x=robot.xcor()+10
    robot.setx(x)
def west():
    x=robot.xcor()-10
    robot.setx(x)
def north_east():
    x=robot.xcor()+5
    robot.setx(x)
    y=robot.ycor()+5
    robot.sety(y)
def south_east():
    y=robot.ycor()-5    
    x=robot.xcor()+5
    robot.setx(x)
    robot.sety(y)
def south_west():
    y=robot.ycor()-5    
    x=robot.xcor()-5
    robot.setx(x)
    robot.sety(y)
def north_west():
    y=robot.ycor()+5    
    x=robot.xcor()-5
    robot.setx(x)
    robot.sety(y)
def clear():
    robot.clear()
def reset():
    robot.pu()
    robot.goto(-600,-220)
    robot.pd()
def coords():
    print(robot.xcor())
    print(robot.ycor())

turtle.listen()
turtle.onkeypress(north, "8")
turtle.onkeyrelease(north, "8")
turtle.onkeypress(south, "2")
turtle.onkeyrelease(south, "2")
turtle.onkeypress(east, "6")
turtle.onkeyrelease(east, "6")
turtle.onkeypress(west, "4")
turtle.onkeyrelease(west, "4")
turtle.onkeypress(north_east, "9")
turtle.onkeyrelease(north_east, "9")
turtle.onkeypress(south_east, "3")
turtle.onkeyrelease(south_east, "3")
turtle.onkeypress(south_west, "1")
turtle.onkeyrelease(south_west, "1")
turtle.onkeypress(north_west, "7")
turtle.onkeyrelease(north_west, "7")
turtle.onkey(clear, "c")
turtle.onkey(reset, "r")
turtle.onkey(coords, "5")




robot.ondrag(dragging)

wn.mainloop()




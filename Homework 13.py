import turtle

screen = turtle.Screen()
screen.title("Square using Turtle")

pen = turtle.Turtle()
pen.speed(3)

for _ in range(4):
    pen.forward(100)   # length of each side
    pen.right(90)      # turn 90 degrees

turtle.done()

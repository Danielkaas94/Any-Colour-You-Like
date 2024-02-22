import turtle

# Create a turtle object
heart = turtle.Turtle()

# Set the speed of the turtleS
heart.speed(2)

# Move the turtle to starting position
heart.penup()
heart.goto(0, -200)
heart.pendown()

# Draw the heart shape
heart.begin_fill()
heart.fillcolor('red')
heart.left(140)
heart.forward(224)
for i in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for i in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()

# Hide the turtle
heart.hideturtle()

# Keep the window open
turtle.done()

import turtle
turtle.tracer(1, 0)  # Makes the turtle draw faster.
for i in range(360):
    turtle.forward(i)
    turtle.left(59)
turtle.exitonclick()  # Pause until user clicks in the window.

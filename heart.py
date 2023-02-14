import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting point
t.up()
t.goto(0, -100)
t.down()

# Draw the heart shape
t.begin_fill()
t.color("red")
t.left(45)
t.forward(150)
t.circle(75, 180)
t.right(90)
t.circle(75, 180)
t.forward(150)
t.end_fill()

# Move the turtle to the text position
t.up()
t.goto(0, 20)
t.down()

# Write the text
t.color("white")
t.write("I love you Komal Ushire", align="center", font=("Arial", 16, "bold"))

# Hide the turtle cursor
t.hideturtle()

# Display the final result
turtle.done()

import turtle

t = turtle.Turtle()
t.speed('fast')

### YOUR CODE STARTS HERE
# This line change the background color.
turtle.bgcolor('pink')
# This line change the shape of the arrow.
t.shape("turtle")
# This line hold on pen.
t.penup()
# The turtle moves in (-300, 250).
t.goto(-300,250)
# This line prints my name.
t.write("Name: Yeji Song")
# The turtle moves in (-300, 235).
t.goto(-300, 235)
# This line prints my student number.
t.write("Student number: 22100396")

# The turtle moves in (-300, 200).
t.goto(-300, 200)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 50.
t.forward(50)

# This line put the pen down.
t.pendown()
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 250.
t.forward(250)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 250.
t.forward(250)

# This line hold on pen.
t.penup()
# The turtle moves in (-20, 10).
t.goto(-20, 10)

# This line put the pen down.
t.pendown()
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 40.
t.forward(40)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 20.
t.forward(20)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 40.
t.forward(40)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 100.
t.forward(100)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 200.
t.forward(200)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 140.
t.forward(140)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 50.
t.forward(50)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 80.
t.forward(80)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 60.
t.forward(60)

# This line hold on pen.
t.penup()
# The turtle moves in (150, 150).
t.goto(150, 150)

# This line put the pen down.
t.pendown()
# The turtle moves forward by 260.
t.forward(260)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 150.
t.forward(150)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 260.
t.forward(260)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 40.
t.forward(40)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 220.
t.forward(220)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 70.
t.forward(70)
# The turtle turns 90 degrees to the right.
t.right(90)
# The turtle moves forward by 220.
t.forward(220)
# The turtle turns 90 degrees to the left.
t.left(90)
# The turtle moves forward by 40.
t.forward(40)

# This line hold on pen.
t.penup()
# The turtle moves in (-5, -40).
t.goto(-5,-40)

# This line put the pen down.
t.pendown()
# It line is for loop for drawing stars.
for i in range(5):
    # The turtle moves forward by 50.
    t.forward(50)
    # The turtle turns 360/5*2 degrees to the right.
    t.right(360/5*2)





### YOUR CODE ENDS HERE

ts = turtle.getscreen()
ts.getcanvas().postscript(file="my-drawing.eps")

t.screen.mainloop()
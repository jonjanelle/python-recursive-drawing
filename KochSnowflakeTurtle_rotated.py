import turtle
turtle.setup( width = 1000, height = 600, startx = None, starty = None)
def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)



#t1.tracer(nNone, delay=None)
t1 = turtle.Turtle()
t1.tracer(-1,delay=None)
t1.shape("turtle")
t1.speed(0)
t1.penup()
t1.goto(-400, 50)
t1.pendown()
flakeSize = 400
complexity = 4
sides = 5
angle = 216 #216=pentagon, 120=snowflake, 

for i in range(sides):
    koch(t1, complexity, flakeSize)
    t1.right(angle)


'''
for j in range(4):
    for i in range(5):
        koch(t1, complexity, flakeSize)
        t1.right(216)
    t1.penup()
    t1.forward(flakeSize)
    t1.pendown()
'''

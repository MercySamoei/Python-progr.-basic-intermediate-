import turtle
t = turtle.Pen()
  
def mysquare(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)

mysquare(50)
mysquare(75)
t.begin_fill()
mysquare(100)
mysquare(125)
t.end_fill()
mysquare(150)
mysquare(175)


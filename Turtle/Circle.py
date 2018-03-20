import turtle

def ring(rangeNum, move, turn):
  for x in range(rangeNum):
    t.pencolor(colors[x%6])
    t.circle(50)
    t.forward(move)
    t.right(turn)

def jump(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
t = turtle.Turtle()
t.speed(0)

jump(0, 285)
ring(360, 5, 1)

jump(0, 185)

ring(450, 2.6, 0.80)

jump(0, 85)

ring(500, 1.2, 0.75)

t.penup()
t.goto(0, 85)
t.pendown()

turtle.mainloop()

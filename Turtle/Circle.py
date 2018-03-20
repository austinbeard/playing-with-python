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
turtle.bgcolor('black')
t.speed(0)

# 1st ring
jump(0, 285)
ring(360, 5, 1.00)

# 2nd ring
jump(0, 185)
ring(450, 2.6, 0.80)

# 3rd ring
jump(0, 85)
ring(450, 1.2, 0.80)

turtle.mainloop()

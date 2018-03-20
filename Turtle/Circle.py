import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
t = turtle.Pen()
t.penup()
t.speed(0)
t.goto(0, 285)
t.pendown()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.circle(50)
	t.forward(5)
	t.right(1)

t.penup()
t.goto(0, 185)
t.pendown()

for y in range(450):
	t.pencolor(colors[y%6])
	t.circle(50)
	t.forward(2.6)
	t.right(.80)

t.penup()
t.goto(0, 85)
t.pendown()
# Fix this ring still overlaping on bottom
for z in range(540):
	t.pencolor(colors[z%6])
	t.circle(50)
	t.forward(1.3)
	t.right(.75)

turtle.mainloop()
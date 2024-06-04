import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_shape(size, angle, shift, shape):
    turtle.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
         turtle.circle(size)
         next_shape = 'square'
    elif shape == 'square':
          for i in range(4):
         turtle.forward(size * 2)
         turtle.left(90)
     next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
            draw_shape(size + 5, angle + 1, shift + 1, next_shape)

t.bgcolor('black')
t.speed("fast")
t.pensize(35)
draw_shape(30, 0, 1, "circle")

t.pencolor("red")
t.circle(30)

def draw_circle(size, angle, shift):
    t.bgcolor(next(colors))
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

t.bgcolor("black")
t.speed("fast")
t.pensize(4)
draw_circle(30, o. 1)


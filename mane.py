# Case1


import turtle


def gohome():
    turtle.penup()
    turtle.home()
    turtle.pendown()


def square(x, y, size, color, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()


def trangle(x, y, colour, size, angle, degrees, size2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(colour)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(degrees)
    turtle.forward(size2)
    turtle.right(180 - degrees + angle)
    turtle.goto(x, y)
    turtle.end_fill()


def rhombus(x, y, size, degrees, angle, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)  # Цвет
    turtle.right(angle)  # повернуть курсор
    turtle.forward(size)  # задать размер стороны
    turtle.right(180 - degrees)  # второй угол
    turtle.forward(size)  # сторона
    turtle.right(degrees)  # третий угол
    turtle.forward(size)  # сторона
    turtle.right(180 - degrees)  # четвертый угол
    turtle.forward(size)  # последняя сторона
    turtle.end_fill()
    turtle.penup()


turtle.speed(10)


def rabbit(x, y, scale):
    gohome()
    square(x, y, 50 * scale, 'orange', 0)
    rhombus(x + 25 * scale, y, 50 * scale, 135, 45, 'purple')
    trangle(x + 50 * scale, y, 'red', 100 * scale, -90, -90, 100 * scale)
    trangle(x + 50 * scale, y - 100 * scale, 'blue', 100 * scale, 180, 90, 100 * scale)
    trangle(x + 150 * scale, y - 200 * scale, 'black', 60 * scale, 180, 90, 60 * scale)
    trangle(x + 90 * scale, y - 200 * scale, 'yellow', 42 * scale, 45, 90, 42 * scale)
    trangle(x + 50 * scale, y - 130 * scale, 'green', 42 * scale, 135, 90, 42 * scale)


rabbit(-150, 380, 1)


def fish(x,y,scale):
  gohome()
  trangle(x,y,'orange',80 * scale, 45, 90, 80 * scale)
  trangle(x, y - 70 * scale, 'red', 100 * scale, 180, 90, 100 * scale)
  trangle(x - 100 * scale, y + 30 * scale, 'green', 100 * scale, 270, 90, 100 * scale )
  square(x, y - 70 * scale, 60 * scale, 'blue', 45)
  rhombus(x - 80 * scale, y - 70 * scale, 50 * scale, 110, 40,'yellow')
  rhombus(x - 80 * scale, y - 70 * scale,50 * scale,110,220,'orange')

fish(0,80,0.7)


def squirrel(x, y, scale):
    gohome()
    rhombus(x, y, 80 * scale, 100, 0, 'green')
    gohome()
    trangle(x, y, 'red', 30 * scale, 260, 60, 30 * scale)
    gohome()
    square(x - 55 * scale, y - 80 * scale, 120 * scale, 'pink', 0)
    gohome()
    trangle(x - 5 * scale, y - 90 * scale, 'blue', 35 * scale, 0, 65, 60 * scale)
    gohome()
    square(x + 45 * scale, y - 100 * scale, 20 * scale, 'purple', 0)
    gohome()
    trangle(x - 55 * scale, y, 'yellow', 120 * scale, 90, 90, 100 * scale)
    gohome()
    rhombus(x - 85 * scale, y - 200 * scale, 40 * scale, 60, 0, 'black')


squirrel(0, -100, 0.6)


def human(x, y, scale):
    head = 42 * scale
    head = 42 * scale
    square(x + 50 * scale, y, 30 * scale, 'orange', 45)
    trangle(x, y - head, 'green', 50 * scale, 0, 90, 50 * scale)
    trangle(x + 100 * scale, y - head, 'yellow', 50 * scale, 180, -90, 50 * scale)
    trangle(x + 50 * scale, y - 50 * scale - head, 'blue', 35 * scale, 135, -90, 35 * scale)
    trangle(x + 85 * scale, y - 85 * scale - head, 'black', 20 * scale, -45, 120, 20 * scale)
    rhombus(x + 50 * scale, y - 50 * scale - head, 30 * scale, 140, -28, 'red')
    trangle(x + 16 * scale, y - 95 * scale - head, 'black', 20 * scale, 90, 120, 20 * scale)


 human(-400, 400, 1.5)


def human2(x, y, scale):
  gohome()
  square(x, y, 100 * scale, 'orange', 225)
  trangle(x, y, 'red', 160 * scale, 315, 90, 140 * scale)
  trangle(x, y, 'green', 140 * scale, 190, 90, 160 * scale)
  rhombus(x - 45 * scale,y - 170 * scale, 80 * scale, 120, 39,'blue')
  rhombus(x - 140 * scale, y - 270 * scale, 40 * scale, 120, 180, 'black')
  trangle(x + 20 * scale, y - 160 * scale, 'yellow', 60 * scale, 55, 90, 60 * scale)
  rhombus(x + 20 * scale, y - 180 * scale, 40 * scale, 120, 0, 'black')
    
human2(-300,100,0.55)

def rocket(x, y, scale):
    gohome()
    square(x, y, 100 * scale, 'light grey', 0)
    gohome()
    trangle(x + 100 * scale, y, 'slate blue', 100 * scale, 180, 120, 100 * scale)
    gohome()
    square(x + 25 * scale, y - 100 * scale, 50 * scale, 'chocolate', 0)
    gohome()
    rhombus(x + 25 * scale, y - 100 * scale, 50 * scale, 120, 90, 'royal blue')
    gohome()
    rhombus(x + 75 * scale, y - 100 * scale, 50 * scale, 120, 30, 'light blue')
    gohome()
    trangle(x + 35 * scale, y - 30 * scale, 'plum', 30 * scale, 0, 120, 30 * scale)


rocket(-300, -150, 0.7)
turtle.exitonclick()

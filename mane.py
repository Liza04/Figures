# Case1


import turtle


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
    turtle.penup()
    turtle.home()


def triangle(x, y, colour, size, angle, degrees, size2):
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
    turtle.penup()
    turtle.home()


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
    turtle.home()


turtle.speed(10)


def rabbit(x, y, scale):
    square(x, y, 50 * scale, 'orange', 0)
    rhombus(x + 25 * scale, y, 50 * scale, 135, 315, 'purple')
    triangle(x + 50 * scale, y, 'red', 100 * scale, 90, -90, 100 * scale)
    triangle(x + 50 * scale, y - 100 * scale, 'blue', 100 * scale, 360, 90, 100 * scale)
    triangle(x + 150 * scale, y - 200 * scale, 'black', 60 * scale, 180, 90, 60 * scale)
    triangle(x + 90 * scale, y - 200 * scale, 'yellow', 42 * scale, 225, 90, 42 * scale)
    triangle(x + 50 * scale, y - 130 * scale, 'green', 42 * scale, 225, 90, 42 * scale)


rabbit(-150, 350, 1)


def fish(x,y,scale):
    triangle(x,y,'orange',80 * scale, 45, 90, 80 * scale)
    triangle(x, y - 70 * scale, 'red', 100 * scale, 90, 90, 100 * scale)
    triangle(x - 100 * scale, y + 30 * scale, 'green', 100 * scale, 0, 90, 100 * scale )
    square(x, y - 70 * scale, 60 * scale, 'blue', 135)
    rhombus(x - 85 * scale, y - 70 * scale, 50 * scale, 110, 90,'yellow')
    rhombus(x - 85 * scale, y - 70 * scale,50 * scale,110,220,'orange')

    
fish(250, 350, 1)


def squirrel(x, y, scale):
    rhombus(x, y, 80 * scale, 100, 0, 'green')
    triangle(x, y, 'red', 30 * scale, 260, 60, 30 * scale)
    square(x - 55 * scale, y - 80 * scale, 120 * scale, 'pink', 0)
    triangle(x - 5 * scale, y - 90 * scale, 'blue', 35 * scale, 0, 65, 60 * scale)
    square(x + 45 * scale, y - 100 * scale, 20 * scale, 'purple', 0)
    triangle(x - 55 * scale, y, 'yellow', 120 * scale, 90, 90, 100 * scale)
    rhombus(x - 85 * scale, y - 200 * scale, 40 * scale, 60, 0, 'black')


squirrel(0, -150, 0.9)


def human(x, y, scale):
    head = 42 * scale
    square(x + 50 * scale, y, 30 * scale, 'orange', 45)
    triangle(x, y - head, 'green', 50 * scale, 0, 90, 50 * scale)
    triangle(x + 100 * scale, y - head, 'yellow', 50 * scale, 180, -90, 50 * scale)
    triangle(x + 50 * scale, y - 50 * scale - head, 'blue', 40 * scale, 165, -90, 35 * scale)
    triangle(x + 96 * scale, y - 107 * scale - head, 'black', 20 * scale, 45, 120, 20 * scale)
    rhombus(x + 50 * scale, y - 50 * scale - head, 40 * scale, 137, 30, 'red')
    triangle(x + 21 * scale, y - 94 * scale - head, 'black', 20 * scale, 60, 120, 20 * scale)


human(-400, 400, 1.5)


def human2(x, y, scale):
  square(x, y, 100 * scale, 'orange', 225)
  triangle(x, y, 'red', 160 * scale, 90, 90, 140 * scale)
  triangle(x, y, 'green', 140 * scale, 40, 90, 160 * scale)
  rhombus(x, y - 170 * scale, 80 * scale, 120, 90,'blue')
  rhombus(x - 65 * scale, y - 290 * scale, 40 * scale, 120, 180, 'black')
  triangle(x + 70 * scale, y - 140 * scale, 'yellow', 60 * scale, 85, 90, 60 * scale)
  rhombus(x + 80 * scale, y - 200 * scale, 40 * scale, 120, 0, 'black')


human2(-300, -150, 0.55)

def rocket(x, y, scale):
    square(x, y, 100 * scale, 'light grey', 0)
    triangle(x + 100 * scale, y, 'slate blue', 100 * scale, 180, 120, 100 * scale)
    square(x + 25 * scale, y - 100 * scale, 50 * scale, 'chocolate', 0)
    rhombus(x + 25 * scale, y - 100 * scale, 50 * scale, 120, 90, 'royal blue')
    rhombus(x + 75 * scale, y - 100 * scale, 50 * scale, 120, 30, 'light blue')
    triangle(x + 35 * scale, y - 30 * scale, 'plum', 30 * scale, 0, 120, 30 * scale)


rocket(250, -150, 0.8)
turtle.exitonclick()

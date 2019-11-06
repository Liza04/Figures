#Case1


import turtle


def square(x, y, size, color, angle):
  # TODO:(Anya)
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
  # TODO:(Sasha)
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
  turtle.color(color) #Цвет
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

#(Anya) rabbit

#(Sasha) fish
#trangle(20,60,'red',40,70,90,40)

#(Liza) squirrel
def squirrel(x, y, scale):
    rhombus(x, y, 80 * scale, 100, 0, 'green')
    trangle(x, y, 'red', 30 * scale, 260, 60, 30 * scale)
    square(x - 55 * scale, y - 80 * scale, 120 * scale, 'pink', 0)
    trangle(x - 5 * scale, y - 90 * scale, 'blue', 35 * scale, 0, 65, 60 * scale)
    square(x + 45 * scale, y - 100 * scale, 20 * scale, 'purple', 0)
    trangle(x - 55 * scale, y, 'yellow', 120*scale, 90, 90, 100 * scale)
    rhombus(x - 85 * scale, y - 200 * scale, 40 * scale, 60, 0, 'black')


squirrel(10, 10, 2)

#(Anya) human
# square(0, 150, 150, 'blue', 30)
def human(x, y, scale):
    head = 42 * scale
    square(x + 50 * scale, y, 30 * scale, 'orange', 45)
    trangle(x, y - head, 'green', 50 * scale, 45, 90, 50 * scale)
    trangle(x + 100 * scale, y - head, 'yellow', 50 * scale, -45, -90, 50 * scale)
    trangle(x + 50 * scale, y - 50 * scale - head, 'blue', 35 * scale, 135, -90, 35 * scale)
    trangle(x + 85 * scale, y - 85 * scale - head, 'black', 20 * scale, -45, 120, 20 * scale)
    rhombus(x + 50 * scale, y - 50 * scale - head, 30 * scale, 160, -35, 'red')
    trangle(x + 18 * scale, y - 92 * scale - head, 'black', 20 * scale, 90, 120, 20 * scale)

human(-400, 400, 4)
square(0, 0, 2, 'blue', 30)

#(Sasha) human2

#(Liza) rocket
def rocket(x, y, scale):
    square(x, y, 100 * scale, 'light grey',0)
    trangle(x + 100 * scale, y, 'slate blue', 100 * scale, 180, 120, 100 * scale)
    square(x + 25 * scale, y - 100 * scale, 50 * scale, 'chocolate', 0)
    rhombus(x + 25 * scale, y - 100 * scale, 50 * scale, 120, 90, 'royal blue')
    rhombus(x + 75 * scale, y - 100 * scale, 50 * scale, 120, 30, 'light blue')
    trangle(x + 35 * scale, y - 30 * scale, 'plum', 30 * scale, 0, 120, 30 * scale)


rocket(10, 10, 2)


turtle.exitonclick()
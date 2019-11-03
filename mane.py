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

def rhombus(x,y,size,degrees,angle,color):
 #TODO:(Liza)
 turtle.penup()
 turtle.goto(x, y)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(color) #Цвет
 turtle.right(angle)  # повернуть курсор
 turtle.forward(size)  # задать размер стороны
 turtle.right(180 - degrees-angle)  # второй угол
 turtle.forward(size)  # сторона
 turtle.right(degrees+angle)  # третий угол
 turtle.forward(size)  # сторона
 turtle.right(180 - degrees-angle)  # четвертый угол
 turtle.forward(size)  # последняя сторона
 turtle.end_fill()
#(Anya) rabbit

#(Sasha) fish
trangle(20,60,'red',40,70,90,40)

#(Liza) squirrel
rhombus(100,100,300,80,30,'green')

#(Anya) human
square(0, 150, 150, 'blue', 30)

#(Sasha) human2

#(Liza) rocket

turtle.exitonclick()
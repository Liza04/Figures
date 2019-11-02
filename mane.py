#Case1


import turtle
def square(x,y,size,colour,angle):
 #TODO:(Anya) 
  pass
def trangle(x,y,size,colour,angle):
 #TODO:(Sasha)
  pass
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

#(Liza) squirrel
rhombus(100,100,300,80,30,'green')

#(Anya) human

#(Sasha) human2

#(Liza) rocket


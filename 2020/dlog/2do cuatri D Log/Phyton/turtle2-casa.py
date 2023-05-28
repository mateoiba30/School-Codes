from turtle import *

setup(450, 200, 0, 0)
screensize(300, 150)
title("tp 2")
hideturtle()
colormode(255)

##pared
pensize(1)
fillcolor(210, 105, 30)
begin_fill()
goto(100, 0)
goto(100, -40)
goto(0, -40)
goto(0, 0)
end_fill()

##techo
fillcolor(47, 79, 79)
begin_fill()
goto(-15, 0)
goto(0, 15)
goto(100, 15)
goto(115, 0)
end_fill()

##chimenea
fillcolor(210, 105, 30)
penup()
goto(80, 15)
pendown()
begin_fill()
goto(80, 35)
goto(70, 35)
goto(70, 15)
end_fill()

##puerta
fillcolor(178, 34, 34)
penup()
goto(60, -40)
begin_fill()
pendown()
goto(60, -10)
goto(80, -10)
goto(80, -40)
end_fill()

##manija
penup()
goto(78, -30)
dot(3, 255, 215, 0)

##ventanal
goto(5, -5)
pendown()
dot(1, 0, 0, 0)
fillcolor(135, 206, 250)
begin_fill()
goto(50, -5)
goto(50, -30)
goto(5, -30)
goto(5, -5)
end_fill()

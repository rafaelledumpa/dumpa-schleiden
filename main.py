from turtle import *

speed(1.2)
bgcolor('black')
penup()
goto(-50,60)
pendown()
color('cyan')
begin_fill()
goto (100,100)
goto (100,-100)

#Draw the windows logo
goto(-50,-60)
goto(-50,60)
end_fill()
color('black')
goto(15,100)

#cut into 2 equal parts
color('black')
width(7)
goto (15,-100)
penup()
goto(100,0)
pendown()
goto(-100,0)

done()
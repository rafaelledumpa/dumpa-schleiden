import turtle

#Colors and Preferences 
t = turtle.Turtle()
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

#Draw Rainbow Star
for x in range(50):
    t.pencolor(colors[x % 7])
    t.forward(x * 10)
    t.right(144)
    t.speed(6.9)

turtle.done()

#Rafa Skibidi Toilet (Turtle Project Done)

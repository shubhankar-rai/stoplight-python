import turtle

wn = turtle.Screen()
wn.title("Stoplights")
wn.bgcolor("black")

# Main Stoplight Box
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

wn.mainloop()
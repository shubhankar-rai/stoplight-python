import turtle
import time

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

# Red Light
redLight = turtle.Turtle()
redLight.shape("circle")
redLight.color("grey")
redLight.penup()
redLight.goto(0, 40)

# Yellow Light
yellowLight = turtle.Turtle()
yellowLight.shape("circle")
yellowLight.color("grey")
yellowLight.penup()

# Red Light
greenLight = turtle.Turtle()
greenLight.shape("circle")
greenLight.color("grey")
greenLight.penup()
greenLight.goto(0, -40)

# Sequence of Changing Light from Green To Red
def switchToRed():
    greenLight.color("grey")
    yellowLight.color("yellow")
    time.sleep(2)
    yellowLight.color("grey")
    redLight.color("red")
    time.sleep(3)

# Sequence of Changing Light from Red To Green
def switchToGreen():
    yellowLight.color("yellow")
    time.sleep(2)
    redLight.color("grey")
    yellowLight.color("grey")
    greenLight.color("green")
    time.sleep(3)

wn.mainloop()
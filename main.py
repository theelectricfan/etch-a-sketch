import turtle
from turtle import Vec2D

paintbrush = turtle.Turtle()

canvas = turtle.Screen()


def move_forward():
    paintbrush.forward(50)


def move_backward():
    paintbrush.backward(50)


def rotate_right():
    paintbrush.right(20)


def rotate_left():
    paintbrush.left(20)


def clear_canvas():
    canvas.resetscreen()


canvas.listen()
canvas.onkey(key="w", fun=move_forward)
canvas.onkey(key="s", fun=move_backward)
canvas.onkey(key="d", fun=rotate_right)
canvas.onkey(key="a", fun=rotate_left)
canvas.onkey(key="c", fun=clear_canvas)

canvas.exitonclick()

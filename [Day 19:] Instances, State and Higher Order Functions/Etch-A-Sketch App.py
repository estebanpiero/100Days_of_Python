from turtle import Turtle, Screen


arrow = Turtle()
Screen = Screen()   

def move_forward():
    arrow.forward(10)

def move_backward():
    arrow.backward(10)

def turn_left():
    arrow.left(10)  

def turn_right():
    arrow.right(10)

def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()

Screen.listen()
Screen.onkey(key="w", fun=move_forward)
Screen.onkey(key="s", fun=move_backward)
Screen.onkey(key="a", fun=turn_left)
Screen.onkey(key="d", fun=turn_right)

Screen.exitonclick()    

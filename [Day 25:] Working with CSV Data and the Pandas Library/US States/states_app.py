# States Game and Map Location

from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

#def get_mouse_click_coor(x, y):
#    print(x, y)
#screen.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

#-------------------------------- Data Processing with Pandas --------------------------------
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()

        # Get the state coordinates

        state_data = data[data.state == answer_state]
        
        # Move the turtle to that coordinates

        t.goto(int(state_data.x), int(state_data.y))
        
        # Write the state name on the map
        t.write(answer_state)



turtle.screen.mainloop()

# screen.exitonclick()
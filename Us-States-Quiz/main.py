import turtle
from turtle import Screen , Turtle
import pandas

screen = Screen()
screen.title("U.S State Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

states_to_learn = []

while len(guessed_states) < 50:

    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                   prompt="What's another state's name?").title()
    if user_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        screen.bye()
        break
    if user_answer not in guessed_states:
        if user_answer in all_states:
            guessed_states.append(user_answer)
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == user_answer]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(user_answer)



turtle.mainloop()
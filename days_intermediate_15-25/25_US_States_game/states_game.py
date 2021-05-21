import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.tracer(0)

data = pandas.read_csv("50_states.csv")
states_lst = data["state"].to_list()

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = turtle.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        break

    if answer_state in states_lst:
        answer_data = data[data.state == answer_state]
        turtle.setposition(x=int(answer_data.x), y=int(answer_data.y))
        turtle.write(answer_state, align="center", font=("Courier", 10, "normal"))
        turtle.goto(0, 0)
        correct_guesses.append(answer_state)


states_to_learn_lst = []
for state in states_lst:
    if state not in correct_guesses:
        states_to_learn_lst.append(state)

states_to_learn_dct = {
    "States to learn": states_to_learn_lst
}

states_to_learn_pd = pandas.DataFrame(states_to_learn_dct)
states_to_learn_pd.to_csv("states_to_learn.csv")






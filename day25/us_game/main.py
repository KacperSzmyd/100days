import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
states = df.state.to_list()

t1 = turtle.Turtle()
t1.ht()


def write_answer(turtle, answer, x, y):
    turtle.teleport(x, y)
    turtle.write(f"{answer}", False, align="center")


def to_learn(correct_guesses, df):
    states_to_learn = []
    for state in df.state:
        if state not in correct_guesses:
            states_to_learn.append(state)
        else:
            continue
    pd.DataFrame(states_to_learn, columns=["state"]).to_csv("states_to_learn.csv")


while len(correct_guesses) < 50:
    answer_state = screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct",
        prompt="What's another state name?",
    ).title()

    if answer_state == "Exit":
        break

    if answer_state in states:
        correct_guesses.append(answer_state)
        data = df[df.state == answer_state].values[0]
        write_answer(t1, data[0], data[1], data[2])


turtle.mainloop()
to_learn(correct_guesses=correct_guesses, df=df)

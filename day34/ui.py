from tkinter import Tk, Canvas, Button, PhotoImage, Label
from quiz_brain import QuizBrain
from data import parameters

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.canvas = Canvas()
        self.score = 0
        self.score_label = Label()
        self.q_text = self.canvas.create_text(150, 125)
        self.true_button = Button()
        self.true_button_img = PhotoImage(file="images/true.png")
        self.false_button = Button()
        self.false_button_img = PhotoImage(file="images/false.png")
        self.setup_ui()

        self.get_next_question()
        self.window.mainloop()

    def setup_ui(self):
        self.window.title("Quizzlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas.config(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label.config(
            text=f"Score: {self.score}/{parameters['amount']}",
            fg="white",
            bg=THEME_COLOR,
        )
        self.score_label.grid(column=1, row=0)

        self.canvas.itemconfig(
            self.q_text,
            text="Lorem Ipsum",
            width=280,
            fill="black",
            font=("Arial", 20, "italic"),
        )

        self.true_button.config(
            image=self.true_button_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.answer_true,
        )
        self.true_button.grid(column=0, row=2)

        self.false_button.config(
            image=self.false_button_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.answer_false,
        )
        self.false_button.grid(column=1, row=2)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            new_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.q_text, text=new_question)
        else:
            self.canvas.itemconfig(
                self.q_text, text="Congratulations!\nYou reached end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz_brain.check_answer("True")
        if is_right:
            self.score = self.quiz_brain.score
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz_brain.check_answer("False")
        if is_right:
            self.score = self.quiz_brain.score
        self.give_feedback(is_right)

    def give_feedback(self, is_answer_right: bool):
        self.score_label.config(text=f"Score: {self.score}/{parameters['amount']}")
        if is_answer_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

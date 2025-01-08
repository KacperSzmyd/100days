from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔️"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 1
work_reps = 0


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(
    text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, "bold")
)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=300, height=265, bg=YELLOW, highlightthickness=0)

pomodoro_image = PhotoImage(file="tomato.png")

canvas.create_image(150, 133, image=pomodoro_image)
timer_text = canvas.create_text(
    150, 133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

check_label = Label(background=YELLOW, foreground=GREEN)
check_label.grid(column=1, row=3)


def start_timer():
    global reps
    global work_reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        timer_label.config(text="Work", fg=GREEN)
        work_reps += 1


def count_down(count):
    global reps
    global timer
    global work_reps

    minutes = count // 60
    if minutes < 10:
        minutes = f"0{str(minutes)}"

    seconds = count % 60
    if seconds < 10:
        seconds = f"0{str(seconds)}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        reps += 1
        check_label.config(text=CHECK_MARK * work_reps)
        start_timer()


def reset_timer():
    global timer
    global reps
    global work_reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 1
    work_reps = 0


start_button = Button(
    text="Start", highlightthickness=0, background=YELLOW, command=start_timer
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset", highlightthickness=0, background=YELLOW, command=reset_timer
)
reset_button.grid(column=2, row=2)


window.mainloop()

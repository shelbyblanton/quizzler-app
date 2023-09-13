from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:
    """The Interface class uses the Tkinter and Canvas libraries to create the game UI
    and contains the true / false user interaction, and answer checking functionality.
    """

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create Graphic Interface with Tkinter
        # Main theme color comes from THEME)COLOR global variable stated above
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Keep track of the score
        # Score will be displayed at top right
        self.score = Label(text=f"Score: {self.quiz.score}", font=("Arial", 14, "roman"), padx=20, pady=20, background=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        # User Canvas to add text, graphics and buttons to the interface
        # Align various elements using the grid() function
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125,
            text="Text here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_click)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        # Function used to advance the quiz game to the next question
        self.get_next_question()

        # User mainloop() to keep the app running until the game has ended.
        self.window.mainloop()

    def get_next_question(self):
        """
        If the quiz still has questions for the user to answer, change the UI text to the
        next question. If the quiz is out of questions, change the UI text to "You have
        reached the end" and disable the true and false buttons.
        :return:
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        """
        The user clicks the 'true' button, we then check to see if the answer is
        true or not.
        :return:
        """
        self.feedback(self.quiz.check_answer("True"))

    def false_click(self):
        """
        The user clicks the 'false' button, we then check to see if the answer is
        false or not.
        :return:
        """
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_correct):
        """
        If the statement is correct, flash green in the text field to signal a correct answer,
        and then add the score.
        If the statement is incorrect, flash red in the text field to signale an incorrect answer,
        and then trigger the next question.
        :param is_correct:
        :return:
        """
        if is_correct:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




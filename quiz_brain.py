import html


class QuizBrain:
    """The QuizBrain class is initialized with the q_list (question list) variable and houses three functions:
        still_has_questions(self)
        next_question(self)
        check_answer(self, (bool) user_answer)
    """

    def __init__(self, q_list):
        """`q_list` is question data pulled from API via the `data` file and formatted prior to submission
        in `main.py`
        :param q_list:
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Check that the game still has questions remaining in the question bank
        :return:
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Advance the app to the next question
        :return:
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def check_answer(self, user_answer):
        """Check if the user correctly guessed true or false for the quizzler question.
        If true, add to score.
        :param user_answer:
        :return:
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

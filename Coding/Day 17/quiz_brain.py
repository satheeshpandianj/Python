class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.
        += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ? : ")
        self.check_answer(answer,current_question.answer)

    def check_answer(self,user_input, q_answer):
        if user_input.lower() == q_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong")
        print(f"The correct answer was {q_answer.lower()}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# question_bank = [
#     Question(q1,a1),
#     Question(q2,a2),
# ]

question_bank = []
# for item in range(len(question_data)):
for item in question_data:
    # question = Question(question_data[item]['text'],question_data[item]['answer'])
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

# print(question_bank[0].answer)
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've have completed the quiz. Your final score was : {quiz_brain.score}/{quiz_brain.question_number}")

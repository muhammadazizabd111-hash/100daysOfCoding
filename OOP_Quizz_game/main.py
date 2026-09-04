from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [] #list of question objects

for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))

quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question() #next_question checks the user answer

print('You have completed the quizz!!!')
print(f"Your final score is {quizz.score}/{quizz.question_number}")

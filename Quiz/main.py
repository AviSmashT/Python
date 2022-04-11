from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []  # Creating questions DB:
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)  # Initialize object

while quiz.still_has_questions():  # Run loop as long as still_has_questions return true
    quiz.next_question()

# End of quiz:
print(f"You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# Start the quiz loop
while quiz.still_has_questions():
    # Ask the next question
    quiz.next_question()

# Display the final score
quiz.final_score()
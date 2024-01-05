from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

question_bank = []
for question in question_data:   #loop question_data bo'yicha aylani oziga faqat savol va javobni saqlab oladi
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) #bu qatorda saqlangan savol va javobni qusetion_modelga jo'natib oziniki qilib oladi
    question_bank.append(new_question)  #ularni list qilib saqlab oladi


quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)



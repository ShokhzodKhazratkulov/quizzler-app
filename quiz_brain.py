import html
class QuizBrain:

    def __init__(self, q_list):  #question bank degan listga saqlangan savol, javoblarni input sifatida oladi
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):  #bu method savol bor yoki yo'qligini tekshiradi agar listni uzunligidan savol
        return self.question_number < len(self.question_list)  #raqami oshib ketsa maindagi while loopi to'xtaydi

    def next_question(self): #javob berilgandan keyin yangi savol tashkil qilinadi
        self.current_question = self.question_list[self.question_number] #boshlanishiga savol indexi bo'yicha ketadi listdagi index bo'yicha
        self.question_number += 1 #boya savol raqami 0 edi endi u bittaga oshirilib boriladi
        q_text = html.unescape(self.current_question.text) #html.unescape() functionni savol textidagi harxil typolarni olib tashlaydi
        return f"Q.{self.question_number}: {q_text}"
        #user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        #

    def check_answer(self, user_answer): #savolni tekshiradigan method, correct_answer degan o'zgaruvchiga hozirgi savolni answer
        correct_answer = self.current_question.answer    #qismini saqlab oladi va uni userniki bilan solishtiradi
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False



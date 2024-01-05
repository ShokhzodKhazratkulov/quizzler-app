from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Ariel", 15, "italic"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill="black",
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, padx=20, pady=20, highlightthickness=0,
                                  command=self.true_answer)
        self.true_button.grid(column=0, row=3)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, padx=20, pady=20, highlightthickness=0,
                                   command=self.false_answer)
        self.false_button.grid(column=1, row=3)

        self.get_next_quest()  #next question uchun method mainloop() tan tashqarida chaqirilmasligi kerak

        self.window.mainloop()

    def get_next_quest(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions(): #bu savol bor yoki yo'qligiga tekshiradi bor bo'lsa yangi savol beradi
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quest_text = self.quiz.next_question()  # quest_text o'zgaruvchiga quiz braindagi next question() methodi beriladi
            self.canvas.itemconfig(self.question_text, text=quest_text)  # va bu savolni canvasga uzatiladi
        else:  #still_has_question() methodi false qaytarsa buttonlar disabled bop qoladi va savol yo'qligini aytadi
            self.canvas.itemconfig(self.question_text, text="You have reached end of the questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):  #savolni tekshirish uchun method check_answer() methodi input olishi kerak shunga
        t_answer = "True"   #input sifatida  ozgaruvchi berilgan
        is_right = self.quiz.check_answer(t_answer)
        self.give_feedback(is_right)

    def false_answer(self):
        f_answer = "False"
        self.give_feedback(self.quiz.check_answer(f_answer))

    def give_feedback(self, is_right): #bu method javobni to'gti notogriligiga qarab o'zgartirishlar kiritadi
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_quest)  #1 sekundan keyin yangi savol beriladi


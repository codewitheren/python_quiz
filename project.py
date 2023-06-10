import random

class Question:
    def __init__(self, question, answer) -> None:
         self.question = question
         self.answer = answer
    
    def answerControl(self):
        if self.answer.lower() == input(f"{self.question} : ").lower():
            return True
        else:
            return False

    
class Quiz:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.score = 0
    
    def getQuestion(self):
        return self.questions[random.randint(0, len(self.questions)-1)]
    


q1 = Question("car", "araba")
q2 = Question("sald", "tuz")
q3 = Question("pencil", "kalem")
q4 = Question("fruit", "meyve")
q5 = Question("money", "para")
q6 = Question("house", "ev")
q7 = Question("tree", "ağaç")
q8 = Question("book", "kitap")
q9 = Question("computer", "bilgisayar")
q10 = Question("school", "okul")
q11 = Question("dog", "köpek")
q12 = Question("cat", "kedi")
q13 = Question("bird", "kuş")
q14 = Question("flower", "çiçek") 
q15 = Question("water", "su")
q16 = Question("sun", "güneş")
q17 = Question("moon", "ay")
q18 = Question("star", "yıldız")
q19 = Question("music", "müzik")
q20 = Question("friend", "arkadaş")

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
             q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]

quiz = Quiz(questions)

for i in range(0,5):
    new_question = quiz.getQuestion()
    if new_question.answerControl():
        print("True")
        quiz.score += 1
    else:
        print("False")
    print()
print(f"Score : {quiz.score}")

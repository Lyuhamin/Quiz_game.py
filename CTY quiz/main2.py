import tkinter as tk
from quiz_character import Quiz_Character
from timer import Timer

if __name__ == "__main__":
    questions = [
        "이 인물은 누구일까요?", "이 인물은 누구일까요?", "이 인물은 누구일까요?",
        "이 인물은 누구일까요?", "이 인물은 누구일까요?", "이 인물은 누구일까요?",
        "이 인물은 누구일까요?", "이 인물은 누구일까요?", "이 인물은 누구일까요?",
        "이 인물은 누구일까요?"
    ]

    images = [
        "유재석.jpeg", "오타니.jpeg", "유관순.jpeg", "김채원.jpeg", "맥아더.jpeg",
        "하니.jpeg", "이순신.jpeg", "일론머스크.jpeg", "지드래곤.jpeg", "손흥민.jpeg"
    ]

    answers = [
        "유재석", "오타니", "유관순", "김채원", "맥아더", "하니", "이순신",
        "일론 머스크", "지드래곤", "손흥민"
    ]

    character = tk.Tk()
    app = Quiz_Character(character, questions, images, answers)
    timer = Timer(character, time_limit=30)

    def check_answer():
        app.check_answer()
        timer.reset_timer()

    app.check_button.config(command=check_answer)
    character.mainloop()
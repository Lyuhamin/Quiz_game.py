import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from timer import Timer
import random
from score import Score


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("속담 퀴즈 게임")

        self.proverbs = [
            ("소 잃고 외양간 고친다", "소 잃고 외양간 고친다.jpeg"),
            ("원숭이도 나무에서 떨어진다", "원숭이도 나무에서 떨어진다.jpeg"),
            ("가는 말이 고와야 오는 말이 곱다", "가는 말이 고와야 오는 말이 곱다.jpeg"),
            ("호랑이도 제말하면 온다", "호랑이도 제말하면 온다.jpeg"),
            ("개천에서 용난다", "개천에서 용난다.jpeg"),
        ]
        random.shuffle(self.proverbs)  # 문제를 랜덤으로 섞기
        self.current_index = 0  # 현재문제의 index를 저장

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.question_label = tk.Label(
            root, text="이 속담은 무엇일까요?", font=("Helvetica", 16)
        )
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind(
            "<Return>", self.check_answer_event
        )  # Enter 키 이벤트 바인딩

        self.check_button = tk.Button(root, text="정답 확인", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.timer = Timer(root, self.show_next_question)
        self.score = Score()  # 점수 시스템 초기화
        self.show_image()  # 현재 index에 해당하는 속담 표시
        self.timer.start_timer()

    def show_image(self):
        if self.current_index < len(self.proverbs):
            proverb, image_file = self.proverbs[self.current_index]
            image_path = os.path.join(os.path.dirname(__file__), "images", image_file)

            # Load image using PIL
            image = Image.open(image_path)
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=self.photo)

            self.current_proverb = proverb  # 현재 속담은 self.current_proverb에 저장
        else:
            messagebox.showinfo(
                "끝",
                f"모든 문제를 완료하였습니다. 최종 점수: {self.score.get_score()}점",
            )

    def show_next_question(self):
        self.current_index += 1
        if self.current_index < len(self.proverbs):
            self.show_image()
            self.timer.reset_timer()
        else:
            messagebox.showinfo(
                "끝",
                f"모든 문제를 완료하였습니다. 최종 점수: {self.score.get_score()}점",
            )
            self.root.quit()

    def check_answer(self):
        # 사용자가 입력한 정답을 확인하고, 정답일 경우 다음 문제로 넘어감

        user_answer = self.answer_entry.get()
        correct_answer = self.current_proverb

        if user_answer == correct_answer:
            self.score.increase()  # 정답일 경우 점수 증가
            messagebox.showinfo(
                "정답", f"정답입니다! 현재 점수: {self.score.get_score()}점"
            )
            self.show_next_question()
        else:
            messagebox.showerror(
                "오답",
                f"틀렸습니다. 정답은 '{correct_answer}' 입니다. 현재 점수: {self.score.get_score()}점",
            )

    def check_answer_event(self, event):
        self.check_answer()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()

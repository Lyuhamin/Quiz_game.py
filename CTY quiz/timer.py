import tkinter as tk
from tkinter import messagebox
#타이머 시간 재는 함수, 다음문제 넘어가면 타이머 초기화
class Timer:
    def __init__(self, character, time_limit=15):
        self.character = character
        self.time_limit = time_limit
        self.time_left = time_limit

        self.time_label = tk.Label(character, text=f"남은 시간: {self.time_left}초", font=("Helvetica", 16))
        self.time_label.pack(pady=20)

        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"남은 시간: {self.time_left}초")
            self.character.after(1000, self.update_timer)
        else:
            messagebox.showinfo("타임 업", "시간이 초과되었습니다.")

    def reset_timer(self):
        self.time_left = self.time_limit
        self.time_label.config(text=f"남은 시간: {self.time_left}초")
        self.character.after_cancel(self.character.after_id)  # 기존 타이머 취소
        self.update_timer()

    def start_timer(self):
        self.update_timer()

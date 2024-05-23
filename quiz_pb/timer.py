import tkinter as tk
from tkinter import messagebox


class Timer:
    def __init__(self, character, on_timeout, time_limit=15):
        self.character = character
        self.time_limit = time_limit
        self.time_left = time_limit
        self.on_timeout = on_timeout
        self.timer_id = None

        self.time_label = tk.Label(
            character, text=f"남은 시간: {self.time_left}초", font=("Helvetica", 16)
        )
        self.time_label.pack(pady=20)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"남은 시간: {self.time_left}초")
            self.timer_id = self.character.after(1000, self.update_timer)
        else:
            messagebox.showinfo("타임 업", "시간이 초과되었습니다.")
            self.on_timeout()

    def reset_timer(self):
        if self.timer_id:
            self.character.after_cancel(self.timer_id)
        self.time_left = self.time_limit
        self.time_label.config(text=f"남은 시간: {self.time_left}초")
        self.update_timer()

    def start_timer(self):
        self.reset_timer()

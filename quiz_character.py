import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from question_manager import QuestionManager

# 문제생성이랑 문제판단 함수 생성하는 클래스, 이미지 크기 조정 포함
class Quiz_Character:
    def __init__(self, character, questions, images, answers):
        self.character = character
        self.character.title("인물")
        
        self.questions = questions
        self.images = images
        self.answers = answers
        self.current_question_index = 0

        # 이미지 크기 조정 및 초기화
        self.image = self.resize_image(self.images[self.current_question_index], 400, 300)
        self.image_label = tk.Label(character, image=self.image)
        self.image_label.pack(pady=10)

        self.question_label = tk.Label(character, text=self.questions[self.current_question_index], font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(character, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(character, text="정답 확인", command=self.check_answer)
        self.check_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.answers[self.current_question_index]
        if QuestionManager.check_answer(user_answer, correct_answer):
            self.current_question_index = QuestionManager.go_to_next_question(
                self.character, 
                self.current_question_index, 
                self.questions, 
                self.images, 
                self.image_label,  
                self.answers, 
                self.answer_entry, 
                self.question_label
            )
            # 이미지 크기 조정 및 업데이트
            self.image = self.resize_image(self.images[self.current_question_index], 400, 300)
            self.image_label.config(image=self.image)
            self.image_label.image = self.image  # 필요한 경우 이미지 참조 유지
            self.answer_entry.delete(0, 'end')  # 다음 문제로 넘어가면 입력 초기화

    def resize_image(self, path, width, height):
        image = Image.open(path)
        resized_image = image.resize((width, height))
        return ImageTk.PhotoImage(resized_image)

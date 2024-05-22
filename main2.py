import tkinter as tk
from tkinter import *
from tkinter import messagebox
from quiz_character import Quiz_Character
from question_manager import QuestionManager
from timer import Timer

#전체적으로 합친 메인 프로그램

if __name__ == "__main__":
    questions = ["이 인물은 누구일까요?", "이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?","이 인물은 누구일까요?"]  # 질문 리스트
    images = ["/Users/changtaeyoung/Desktop/python/pic/유재석.jpeg","/Users/changtaeyoung/Desktop/python/pic/오타니.jpeg","/Users/changtaeyoung/Desktop/python/pic/유관순.jpeg","/Users/changtaeyoung/Desktop/python/pic/김채원.jpeg","/Users/changtaeyoung/Desktop/python/pic/맥아더.jpeg","/Users/changtaeyoung/Desktop/python/pic/하니.jpeg","/Users/changtaeyoung/Desktop/python/pic/이순신.jpeg","/Users/changtaeyoung/Desktop/python/pic/일론머스크.jpeg","/Users/changtaeyoung/Desktop/python/pic/지드래곤.jpeg","/Users/changtaeyoung/Desktop/python/pic/손흥민.jpeg"]  # 각 질문에 해당하는 이미지 경로, 수정 필요 사진 파일 같이 첨부
    answers = ["유재석","오타니","유관순","김채원","맥아더","하니","이순신","일론 머스크","지드래곤","손흥민"]  # 각 질문에 해당하는 정답 리스트
    
    character = tk.Tk()
    app = Quiz_Character(character, questions, images, answers)
    timer = Timer(character,time_limit=30)

    def check_answer():
        app.check_answer()
        timer.reset_timer()  # 타이머 초기화



    app.check_button.config(command=check_answer) 
    character.mainloop()

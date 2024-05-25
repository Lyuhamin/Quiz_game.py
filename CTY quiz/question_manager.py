from tkinter import messagebox

#문제 정답 오답 판단이랑 다음문제로 넘기는 클래스
class QuestionManager:
    @staticmethod
    def check_answer(answer, correct_answer): #문제 정답 오답 판단
        if answer == correct_answer:
            messagebox.showinfo("정답", "정답입니다!")
            return True
        else:
            messagebox.showerror("오답", f"틀렸습니다. 정답은 {correct_answer} 입니다.")
            return False

    @staticmethod #문제풀면 다음문제로 넘기는 함수
    def go_to_next_question(character, current_question_index, questions, images, image_label, answers, answer_entry, question_label):
        current_question_index += 1
        if current_question_index < len(questions):
            question_label.config(text=questions[current_question_index])
            return current_question_index
        else:
            messagebox.showinfo("완료", "퀴즈가 종료되었습니다.")
            character.quit()  # 퀴즈 종료
            return current_question_index 

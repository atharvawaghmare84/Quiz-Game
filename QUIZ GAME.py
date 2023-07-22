#-------------------------------------------------------------------------------
# Name:       Atharva Waghmare
# Purpose:    TASK 5
# TASK:       QUIZ GAME
# Author:      atharva
# Created:     20-07-2023
# Copyright:   (c) athar 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import tkinter as tk
import random

# Quiz questions and answers related to Indian cricket
quiz_data = [
    {
        "question": "Who is the only Indian cricketer to score a triple century in Test cricket?",
        "options": ["Sachin Tendulkar", "Rahul Dravid", "Virender Sehwag", "V.V.S. Laxman"],
        "answer": "Virender Sehwag"
    },
    {
        "question": "Which Indian cricketer has the highest individual score in One Day Internationals?",
        "options": ["Sachin Tendulkar", "Rohit Sharma", "Virender Sehwag", "Virat Kohli"],
        "answer": "Rohit Sharma"
    },
    {
        "question": "Who is the leading wicket-taker in T20 International cricket for India?",
        "options": ["Harbhajan Singh", "Ravichandran Ashwin", "Jasprit Bumrah", "Yuzvendra Chahal"],
        "answer": "Jasprit Bumrah"
    }
]

def display_question(question_data):
    question_label.config(text=question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        option_buttons[i].config(text=option)

def evaluate_answer(question_data, user_choice):
    correct_answer = question_data["answer"]
    user_answer = question_data["options"][user_choice - 1]

    if user_answer == correct_answer:
        feedback_label.config(text="Correct!")
        return 1
    else:
        feedback_label.config(text=f"Incorrect. The correct answer is: {correct_answer}.")
        return 0

def on_option_click(choice):
    global score, current_question
    score += evaluate_answer(quiz_data[current_question], choice)

    current_question += 1
    if current_question < len(quiz_data):
        display_question(quiz_data[current_question])
    else:
        final_score_label.config(text=f"Your Final Score: {score}/{len(quiz_data)}")
        if score == len(quiz_data):
            feedback_label.config(text="Congratulations! You got all the questions correct!")
        else:
            feedback_label.config(text="Keep practicing to improve your score.")

def create_quiz_game():
    global question_label, option_buttons, feedback_label, final_score_label
    global score, current_question

    score = 0
    current_question = 0

    root = tk.Tk()
    root.title("Indian Cricket Quiz")

    question_label = tk.Label(root, text="", wraplength=400)
    question_label.pack(pady=10)

    option_buttons = {}
    for i in range(1, 5):
        option_buttons[i] = tk.Button(root, text="", padx=10, pady=5, command=lambda idx=i: on_option_click(idx))
        option_buttons[i].pack()

    feedback_label = tk.Label(root, text="", wraplength=400)
    feedback_label.pack(pady=10)

    final_score_label = tk.Label(root, text="", wraplength=400)
    final_score_label.pack(pady=10)

    display_question(quiz_data[current_question])

    root.mainloop()

if __name__ == "__main__":
    create_quiz_game()

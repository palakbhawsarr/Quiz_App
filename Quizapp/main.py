from distutils.cmd import Command
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quizdata import quizdata
def show_que():
    question=quizdata[current_que]
    qs_label.config(text=question["question"])

    choices=question["choices"]
    for i in range(4):
        ch_btn[i].config(text=choices[i],state='normal')

    feedback_label.config(text="")
    next_btn.config(state="disabled")    

def check_answer(choice):
     question=quizdata[current_que]
     selected_choice=ch_btn[choice].cget("text")
     if selected_choice==question["answer"]:
         global score
         score +=1
         score_label.config(text="Score: {}/{}".format(score, len(quizdata)))
         feedback_label.config(text="Correct!", foreground="green")

     else:
         feedback_label.config(text="Wrong!", foreground="red")  

     for button in ch_btn :
         button.config(state="disabled")
     next_btn.config(state="normal")     



def next_question():
    global current_que
    current_que +=1
    
    if current_que<len(quizdata):
        show_que()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score:{}/{}".format(score, len(quizdata) ))
        root.destroy()


root = tk.Tk()
root.title("QUIZ APP")
root.geometry("600x500")
style=Style(theme='flatly')

style.configure("TLabel", font=("Helvetica",20))
style.configure("TButton", font=("Helvetica",16))


qs_label= ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)


ch_btn=[]
for i in range(4):
    button=ttk.Button(
      root,
      command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    ch_btn.append(button)

feedback_label=ttk.Label(
    root,anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

score=0
score_label=ttk.Label(
    root,
    text="Score: 0/{}".format(len(quizdata)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)


next_btn=ttk.Button(
    root,text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

current_que=0

show_que()


root.mainloop()

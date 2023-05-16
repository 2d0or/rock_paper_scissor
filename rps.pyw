import random
import customtkinter
import time 
from PIL import Image, ImageTk
from tkinter import *


values = ['rock', 'paper', 'scissor']
window = customtkinter.CTk()
window.geometry('500x500')
window.configure(fg_color = '#42F2F7')
window.title('Rock Paper Scissor')


def start():
    user_choices = entry_value.get().lower()
    user_choice = str(user_choices)
    opp_move = random.choice(values)
    if user_choice in ['rock', 'paper','scissor']:
        def lab_del():
            while True:
                entry_value.delete(0,END)
                button_destroy.destroy()
                label_text.destroy()
                #qlabel_feedback.destroy()   
                break 
                


        def del_lab():
            while True:
                print('')
                label_draw.destroy()
                label_w.destroy()
                label_lose.destroy()
                break 
            

        def del_try():
            while True:
                label_feedback.destroy()
                break  
            
         
        label_text = customtkinter.CTkLabel(master=window, text = opp_move)
        label_text.pack()
        if user_choice =='paper' and opp_move =='paper' or user_choice =='rock' and opp_move =='rock' or user_choice =='scissor' and opp_move =='scissor':
            label_draw = customtkinter.CTkLabel(master=window, text='you draw')
            label_draw.pack()
        else: pass
        if user_choice =='paper' and opp_move =='rock' or user_choice =='scissor' and opp_move =='paper' or user_choice =='scissor' and opp_move =='paper':
            label_w = customtkinter.CTkLabel(master=window, text='you win')
            label_w.pack()
        else: pass

        if user_choice =='paper' and opp_move =='scissor' or user_choice =='rock' and opp_move =='paper' or user_choice =='scissor' and opp_move =='rock':
            label_lose = customtkinter.CTkLabel(master=window, text='you lose')
            label_lose.pack()
        else: pass

        button_destroy = customtkinter.CTkButton(master=window, text='play again', command= lambda: [lab_del(), del_lab(), del_try()]) #command= lab_del, text='play again')
        button_destroy.pack()
    
    else: label_feedback = customtkinter.CTkLabel(master=window, text='try again')
    label_feedback.pack()




label = customtkinter.CTkLabel(master=window, text='rock, paper, scissor?')
label.pack()#pady=10)
entry_value = customtkinter.CTkEntry(master=window) 
entry_value.pack()

button= customtkinter.CTkButton(master=window, text='submit', command= start)
button.pack()


window.mainloop()
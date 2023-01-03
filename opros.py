from tkinter import *
from tkinter import messagebox 
import random


tk =Tk()
tk.title('Опрос')
tk.geometry('400x250')
tk.resizable(0, 0)


def yes(event):
	btnyes.place(x=random.randint(0, 350), y=random.randint(0,200))


def no():
	messagebox.showinfo('Голос', 'Ваш голос был учтён')






lab = Label(tk, text='Ты натурал', font='Arial 15 bold').pack()

btnyes = Button(tk, text='Да', font='Arial 15')
btnyes.place(x=100, y=125)

btnno = Button(tk, text='Нет', font='Arial 15', command=no)
btnno.place(x=250, y=125)

btnyes.bind('<Motion>', yes)






tk.mainloop()
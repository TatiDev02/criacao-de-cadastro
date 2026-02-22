from tkinter import *
# Criando campos de entrada
I_nome = Label(frame_detalhes, text='Nome *', height=1, anchor=NW, font=('Ivy', 10), bg=co1, fg=co4)
I_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=45, justify='left', relief='solid')
e_nome.place(x=7, y=40)

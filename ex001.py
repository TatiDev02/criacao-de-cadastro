from tkinter import *

# Criar janela principal
janela = Tk()
janela.title("Teste")
janela.geometry("400x200")

# Cores (senão dá erro)
co1 = "white"
co4 = "black"

# Criar frame
frame_detalhes = Frame(janela, bg=co1)
frame_detalhes.pack(fill="both", expand=True)

# Criando campos
l_nome = Label(frame_detalhes, text='Nome *',
               height=1, anchor=NW,
               font=('Ivy', 10),
               bg=co1, fg=co4)
l_nome.place(x=4, y=10)

e_nome = Entry(frame_detalhes, width=45,
               justify='left', relief='solid')
e_nome.place(x=7, y=40)

# Manter janela aberta
janela.mainloop()
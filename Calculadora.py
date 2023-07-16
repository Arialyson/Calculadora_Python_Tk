from tkinter import *
from tkinter import ttk

#cores
cor_1 = '#1e1f1e' #black
cor_2 = '#feffff' #white
cor_3 = '#38576b' #blue
cor_4 = '#eceff1' #gray
cor_5 = '#ffab40' #orange

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x305')
janela.config(bg=cor_1)

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor_3)
frame_tela.grid(column=0, row=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(column=0, row=1)

# vaiavel todos os valores

todos_valores = ''


# criando função
def entrar_valores(event):

    global todos_valores
    
    todos_valores = todos_valores + str(event)
    

    #passando o valor para a tela
    valor_texto.set(todos_valores)

# função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor_3, fg=cor_2)
app_label.place(x=0, y=0)

# criando botões
b_1 = Button(frame_corpo, command=limpar_tela, text='C', width=11, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda:entrar_valores('%'), text='%', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command= lambda:entrar_valores('/'), text='/', width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=179, y=0)

b_4 = Button(frame_corpo, command= lambda:entrar_valores('7'), text='7', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command= lambda:entrar_valores('8'), text='8', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)
b_4 = Button(frame_corpo, command= lambda:entrar_valores('9'), text='9', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=120, y=52)
b_6 = Button(frame_corpo, command= lambda:entrar_valores('*'), text='*', width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=180, y=51)

b_7 = Button(frame_corpo, command= lambda:entrar_valores('4'), text='4', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=102)
b_8 = Button(frame_corpo, command= lambda:entrar_valores('5'), text='5', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=60, y=102)
b_9 = Button(frame_corpo, command= lambda:entrar_valores('6'), text='6', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=102)
b_10 = Button(frame_corpo, command= lambda:entrar_valores('-'), text='-', width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=180, y=102)

b_11 = Button(frame_corpo, command= lambda:entrar_valores('1'), text='1', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=0, y=152)
b_12= Button(frame_corpo, command= lambda:entrar_valores('2'), text='2', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=60, y=152)
b_13 = Button(frame_corpo, command= lambda:entrar_valores('3'), text='3', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=120, y=152)
b_14= Button(frame_corpo, command= lambda:entrar_valores('+'), text='+', width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=180, y=152)

b_1 = Button(frame_corpo, command= lambda:entrar_valores('0'), text='0', width=11, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=204)
b_2 = Button(frame_corpo, command= lambda:entrar_valores('.'), text='.', width=5, height=2, bg=cor_4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=204)
b_3 = Button(frame_corpo, command= calcular, text='=', width=5, height=2, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=204)






janela.mainloop()

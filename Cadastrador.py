#!/usr/bin/env python3
from tkinter import *
from lucaslib import *

janela = Tk()
janela.title('CADASTRADOR')
janela.geometry('1000x700')

#criando as telas
tela1 = Frame(janela, bg='gray')
tela2 = Frame(janela, bg='gray')
tela3 = Frame(janela, bg='gray')
tela4 = Frame(janela, bg='gray')

#colocando uma tela sobre a outra
tela1.place(relx=0, rely=0, relwidth=1, relheight=1)
tela2.place(relx=0, rely=0, relwidth=1, relheight=1)
tela3.place(relx=0, rely=0, relwidth=1, relheight=1)
tela4.place(relx=0, rely=0, relwidth=1, relheight=1)

#Itens da tela 1
Label(tela1, text='MENU', font='arial 30 bold', background='gray').place(relx=0.5, rely=0.1, anchor='center')
Label(tela1, text='C@dastros', font='arial 20 bold italic', background='gray').place(relx=0.5, rely=0.19, anchor='center')
Label(tela1, text='Criado por: LUCAS KUSSA', background='gray').place(relx=0.8,rely=0.95, anchor='center')
Button(tela1, text='Ver pessoas cadastradas', command=lambda: [troca(tela2), ver(tela2, msg_tela2, texto)]).place(relx=0.5, rely=0.4, relwidth=0.4, anchor='center')
Button(tela1, text='Cadastrar nova pessoa', command=lambda: troca(tela3)).place(relx=0.5, rely=0.48, relwidth=0.4, anchor='center')
Button(tela1, text='Excluir pessoa cadastrada', command=lambda: [troca(tela4), tela_exclusao(tela4, msg_zero, texto_deletar)]).place(relx=0.5, rely=0.56, relwidth=0.4, anchor='center')

#Itens da tela 2
Label(tela2, text='Pessoas Cadastradas', font='arial 20 bold',background='gray').place(relx=0.5,rely=0.1, anchor='center')
msg_tela2 = Label(tela2, text='Não há pessoas cadastradas ainda!', font='arial 20 bold', fg='green')

texto = Text(tela2, wrap='word')
texto.place(relx=0.04, rely=0.25, relwidth=0.92, relheight=0.5)
barra = Scrollbar(tela2, command=texto.yview)
barra.place(relx=0.96, rely=0.5, relwidth=0.03, relheight=0.5, anchor='center')
texto.config(yscrollcommand=barra.set)
Button(tela2, text='Voltar', command=lambda: troca(tela1)).place(relx=0.1, rely=0.9, anchor='center')
Button(tela2, text='Cadastrar', command=lambda: troca(tela3)).place(relx=0.9, rely=0.9, anchor='center')

#Itens da tela 3
Label(tela3, text='Cadastrar', font='arial 30 bold', background='gray').place(relx=0.5, rely=0.2, anchor='center')
Label(tela3, text='Nome:', font='arial 15 bold', background='gray').place(relx=0.28, rely=0.4, anchor='center')
Label(tela3, text='Idade:', font='arial 15 bold', background='gray').place(relx=0.28, rely=0.5, anchor='center')
nome = Entry(tela3)
nome.place(relx=0.6, rely=0.4, relwidth=0.5, anchor='center')
idade = Entry(tela3)
idade.place(relx=0.6, rely=0.5, relwidth=0.5, anchor='center')
Button(tela3, text='Inserir', command=lambda: dados(nome.get(), idade.get(), nome, idade, tela3)).place(relx=0.5, rely=0.6, anchor='center')
Button(tela3, text='Voltar', command=lambda: troca(tela1)).place(relx=0.1, rely=0.9, anchor='center')

#Itens da tela 4
Label(tela4, text='DIGITE O NÚMERO CORRESPONDENTE A PESSOA QUE SERÁ DELETADA!', bg='gray').place(relx=0.5, rely=0.05, anchor='center')
texto_deletar = Text(tela4, wrap='word')
texto_deletar.place(relx=0.04, rely=0.08, relwidth=0.92, relheight=0.5)
barra2 = Scrollbar(tela4, command=texto_deletar.yview)
barra2.place(relx=0.95, rely=0.08, relwidth=0.03, relheight=0.5)
texto_deletar.config(yscrollcommand=barra2.set)
apagar = Entry(tela4)
apagar.place(relx=0.5, rely=0.65, relwidth=0.1, anchor='center')
Button(tela4, text='DELETAR', bg='#FA8072', command=lambda: excluir(apagar.get(), apagar, tela4, texto_deletar, msg_zero)).place(relx=0.5, rely=0.73, anchor='center')
msg_zero = Label(tela4, text='Não há pessoas cadastradas para exclusão')
Button(tela4, text='Voltar', command=lambda: troca(tela1)).place(relx=0.1, rely=0.9, anchor='center')
Button(tela4, text='Cadastrar', command=lambda: troca(tela3)).place(relx=0.9, rely=0.9, anchor='center')

troca(tela1)
janela.mainloop()

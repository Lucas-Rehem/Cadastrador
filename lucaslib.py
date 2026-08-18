from tkinter import *
import os

def troca(tela):
    tela.tkraise()


def dados(nome, idade, cx_nome, cx_idade, tela3):
    cx_nome.delete(0, END)
    cx_idade.delete(0, END)
    # if - verifica se a idade é um numero / elif - verifica se algum nome foi digitado / else - Salva os dados
    if nome.strip() == '':
        msg_erro1 = Label(tela3, text='O NOME não pode ficar em branco!', bg='white', fg='red')
        msg_erro1.place(relx=0.5, rely=0.7, anchor='center')
        tela3.after(5000, msg_erro1.place_forget)
    elif idade.isnumeric() == False:
        msg_erro2 = Label(tela3, text='A IDADE precisa ser um número inteiro!', bg='white', fg='red')
        msg_erro2.place(relx=0.5, rely=0.7, anchor='center')
        tela3.after(5000, msg_erro2.place_forget)
    else:
        with open('banco.txt', 'a') as arquivo:
            arquivo.write(f'{nome.strip().upper()};{idade.strip()}\n')
        msg_sucesso = Label(tela3, text='Cadastro realizado com SUCESSO!', bg='white', fg='green')
        msg_sucesso.place(relx=0.5, rely=0.7, anchor='center')
        tela3.after(5000, msg_sucesso.place_forget)


def ver(tela2, msg, texto):
    texto.config(state=NORMAL)
    texto.delete('1.0', END)
    texto.config(state=DISABLED)
    msg.place(relx=0.5, rely=0.8, anchor='center')
    if os.path.exists('banco.txt'):
        msg.place_forget()
        texto.config(state=NORMAL)
        texto.delete('1.0', END)
        with open('banco.txt', 'r') as arquivo:
            info = arquivo.readlines()
        idade = ''
        nome = ''
        mensagem = ''        
        for c in range(0, len(info)):
            if ' ' in info[c]:
                info[c] = info[c].replace(' ', ':')
        for linha in info:
            if ';' in linha:
                dado = linha.replace(';',' ')
                dado = dado.split()
                idade = dado[-1]
                nome = dado[0].replace(':',' ')
                mensagem = mensagem + (f'Nome: {nome:<35} Idade:{idade:>3}\n')
        texto.insert('1.0', mensagem)
        texto.config(state=DISABLED)
        

def tela_exclusao(tela4, msg, texto):
    texto.config(state=NORMAL)
    texto.delete('1.0', END)
    texto.config(state=DISABLED)
    msg.place(relx=0.5, rely=0.8, anchor='center')
    if os.path.exists('banco.txt'):
        msg.place_forget()
        texto.config(state=NORMAL)
        texto.delete('1.0', END)
        with open('banco.txt', 'r') as arquivo:
            info = arquivo.readlines()
        idade = ''
        nome = ''
        mensagem = ''
        indice = 0
        for c in range(0, len(info)):
            if ' ' in info[c]:
                info[c] = info[c].replace(' ', ':')
        for linha in info:
            if ';' in linha:
                dado = linha.replace(';', ' ')
                dado = dado.split()
                idade = dado[-1]
                nome = dado[0].replace(':', ' ')
                indice += 1
                mensagem = mensagem + (f'{indice:^3} → Nome: {nome:<32} Idade:{idade:>3}\n')
        texto.insert('1.0', mensagem)
        texto.config(state=DISABLED)


def excluir(n1, apagar, tela4, texto, msg):
    apagar.delete(0, END)
    if os.path.exists('banco.txt'):
        with open('banco.txt', 'r') as arquivo:
            info = arquivo.readlines()
        if n1.isnumeric() == True and int(n1) > 0 and int(n1) < len(info)+1:
            if len(info) == 1:
                os.remove('banco.txt')
            else:
                info.pop(int(n1)-1)
                os.remove('banco.txt')
                with open('banco.txt', 'a') as arquivo:
                    for c in range(0, len(info)):
                        arquivo.write(info[c])
            tela_exclusao(tela4,msg,texto)
        else:
            msg1 = Label(tela4, text='O indice deve ser o número na esquerda do nome!')
            msg1.place(relx=0.5, rely=0.8, anchor='center')
            tela4.after(4000, msg1.place_forget)

        
    
    












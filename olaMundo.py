from tkinter import *
#Tk é uma biblioteca do tkinter
#Tk é uma janela

janela = Tk()
#Mainloop no tkinter funciona como uma janela em loop infinito
#Janela que o python mostra na realidade um programa em
janela.geometry("650x400")
janela.title("Interface Gráfica")
titulo = Label(text="\n Olá Mundo!", font='Arial 35')
titulo.pack()
texto = Label(text="Estamos aprendendo tkinter!", font="Arial 20")
texto.pack()

janela.mainloop()


# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:29:17 2015

@author: Rafael
"""


import turtle
from random import *

giz = turtle.Turtle()
giz.speed(5) #velocidade
giz.pensize(7)
giz.pencolor("yellow")


def cabeca():
    giz.penup()
    giz.setpos(0,230)
    giz.pendown()
    giz.right(180)    
    giz.circle(50) # desenho cabeça
    
    
def corpo():
    giz.penup()
    giz.setpos(0,130)
    giz.pendown()    
    giz.right(270)
    giz.forward(100) #desenho corpo
    
def perna1():
    giz.penup()
    giz.setpos(0,30)    
    giz.left(30)
    giz.pendown()
    giz.forward(75)#desenho perna direita
    
def perna2():
    giz.penup()
    giz.setpos(0,30)    
    giz.left(290)
    giz.pendown()
    giz.forward(75)    #desenho perna esquerda    
    
def braço1():
    giz.penup()   
    giz.setpos(0,100) #posicionamento braços
    giz.pendown()
    giz.right(75)    
    giz.forward(50) #braço esquerdo
    
def braço2():
    giz.penup()
    giz.setpos(0,100)
    giz.pendown()
    giz.right(140)
    giz.forward(50) #braço direito



#criando lista com conteudo
arquivo=open("arquivopalavras.txt",encoding="utf-8")
conteudo = arquivo.readlines()
lista = []     

#criando janela

window = turtle.Screen()

#limpando

for p in conteudo:
    palavras = p.strip().lower()
    lista.append(palavras)



#trocando com ascento por sem    
computerchoice = choice(lista)
computerchoice=computerchoice.replace("â","a")
computerchoice=computerchoice.replace("ã","a")
computerchoice=computerchoice.replace("ó","o")
computerchoice=computerchoice.replace("ô","o")
computerchoice=computerchoice.replace("í","i")

print(computerchoice)

#formatando janela e desenhando forca
window.bgcolor("black")
window.title("Forca")
forca = turtle.Turtle()
forca.speed(5) #velocidade
forca.pensize(7)
forca.pencolor("yellow")
forca.penup() #caneta fora
forca.setpos(-100,-100) #posição inicial
forca.pendown() #caneta dentro
forca.backward(200) #desenho base
forca.forward(100) 
forca.left(90)
forca.forward(400) #desenho tronco
forca.right(90)
forca.forward(200) #deseno tronco cima
forca.right(90)
forca.forward(70) #desenho corda
forca.right(90)
forca.penup()
forca.setpos(-300,-200)
forca.right(180)


#desenhando traços    
def traco (computerchoice):
    for c in computerchoice:
        if c == " ":
            forca.penup()
            forca.fd(30)
            forca.pendown()
            d = computerchoice.count(" ")
            
        if c != " ":
            forca.pendown()
            forca.fd(20)
            forca.penup()
            forca.fd(10)
            forca.pendown()
            
traco(computerchoice)
    
    
certo = 0
errado = 0
    
#Inicio recomeço
    #fim do recomeço

while certo < (len(computerchoice)-computerchoice.count(" ")) and errado < 6:
        
    tentativa = window.textinput("Forca","Escolha uma letra")
    

    if tentativa in computerchoice:   #desenhar letra
            f= computerchoice.count(tentativa)
            certo +=1*f
            l=-1
            for t in range (0,f):
                l=computerchoice.index(tentativa, l+1)
                forca.penup()
                forca.setpos(-300 + l*30,-200)
                forca.write(tentativa,font = ("Arial", 20))
    else:
            errado+=1
        
            if errado == 1:
                cabeca()
            
            if errado == 2:
                corpo()
        
            if errado == 3:
                perna1()
            
            if errado == 4:
                perna2()
                
            if errado == 5:
                braço1()
                
            if errado == 6:
                braço2()
                forca.pensize(10)
                forca.penup()
                forca.setpos(100,0)
                forca.pendown()
                forca.write("Você perdeu!")
                recomeçar = window.textinput("Acabou!","Você quer jogar novamente?")       

            if certo == (len(computerchoice)):
                recomeçar = window.textinput("Acabou!","Você quer jogar novamente?") 
            
            
window.exitonclick()
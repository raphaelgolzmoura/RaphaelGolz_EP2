# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:37:29 2015

@author: Rafael
"""

import turtle
from random import *
arquivo=open("arquivopalavras.txt",encoding="utf-8")
conteudo = arquivo.readlines()
lista = []     
window = turtle.Screen()

for p in conteudo:
    palavras = p.strip().lower()
    lista.append(palavras)
    

computerchoice = choice(lista)
computerchoice.replace("â","a")
computerchoice.replace("ó","o")
computerchoice.replace("ô","o")
computerchoice.replace("í","i")

window.bgcolor("black")
window.title("Forca")
window.exitonclick()

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
i=0


while i < len(computerchoice):    #traços
    forca.pendown()
    forca.forward(15)
    forca.penup()
    forca.forward(15)
    i+=1
    
certo=0
errado=0


for tentativa in computerchoice:
    certo +=1
    forca.setpos(-300,-200)
    forca.pendown()
    forca.pensize
    forca.write(tentativa,font=("Arial",20,"normal")
  


def cabeca():
    forca.penup()
    forca.setpos(0,230)
    forca.pendown()    
    forca.circle(50) # desenho cabeça
    forca.circle(50,180)
    
def corpo():
    forca.penup()
    forca.setpos(0,130)
    forca.pendown()    
    forca.right(90)
    forca.forward(100) #desenho corpo
    
def perna1():
    forca.penup()
    forca.setpos(0,30)    
    forca.left(30)
    forca.forward(75)#desenho perna direita
    
def perna2():
    forca.penup()
    forca.setpos(0,30)    
    forca.left(210)
    forca.forward(75)
    forca.right(240)
    forca.forward(75) #desenho perna esquerda    
    
def braço1():
    forca.penup()   
    forca.setpos(0,100) #posicionamento braços
    forca.pendown()
    forca.right(75)    
    forca.forward(50) #braço esquerdo
    
def braço2():
    forca.penup()
    forca.setpos(0,100)
    forca.pendown()
    forca.right(225)
    forca.forward(50) #braço direito

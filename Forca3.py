# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:37:29 2015

@author: Rafael
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:08:18 2015

@author: Rafael
"""

import turtle
from random import *

arqu

window = turtle.Screen()
window.bgcolor("")
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

def cabeca():
    forca.penup()
    forca.setpos(0,230)#ver
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



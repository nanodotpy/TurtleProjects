import turtle
import time

loadwindow = turtle.Screen()
loadwindow.screensize(1500,1500)

pen = turtle.Pen()
pen.penup()
pen.goto((-450,0))
pen.pendown()

def virage(side):
    pen.left(60)
    pen.forward(side)
    pen.right(120)
    pen.forward(side)
    pen.left(60)

def triangle(length) :
    pen.forward(length)
    virage(length)
    pen.forward(length)
    

def von_koch(n,length = 900) :
    
    if n == 1 :
        pen.forward(length)
    
    if n == 2 : 
        a = length/3**(n-1)
        triangle(a)
        
    
    if n == 3 :
        a = length/3**(n-1)                                 #Could have not hard coded for n=3 but wanted to understand the process UwU
        von_koch(2,length/3)
        pen.left(60)
        von_koch(2,length/3)
        pen.right(120)
        von_koch(2,length/3)
        pen.left(60)
        von_koch(2,length/3)
        
    if n > 3 :
        von_koch(n-1,length/3)
        
        pen.left(60)
        von_koch(n-1,length/3)
        
        pen.right(120)
        von_koch(n-1,length/3)
        
        pen.left(60)
        von_koch(n-1,length/3)
   
for a in range(1,10) :
    pen.penup()
    pen.speed(0)
    pen.goto((-450,0))
    pen.pendown()
    pen.clear()
    pen.speed(3*a)
    von_koch(a)
    time.sleep(0.5)

        
    
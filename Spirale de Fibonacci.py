import turtle 

loadwindow = turtle.Screen()
loadwindow.screensize(1920,1080)

pen = turtle.Pen()
pen.penup()
pen.goto((-1920//5,1080//5))
pen.speed(3)
pen.width(1)
pen.pendown()

def fibonacci(a = 1,b = 1) :
    fibo = [a,b]
    while fibo[-1]<800 :
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

fibo = fibonacci(a=4,b=4)

def quartercircle(radius):
    pen.circle(radius,90)
    
def square(c):
    pen.pencolor("black") 
    pen.forward(c)
    pen.left(90)
    pen.forward(c)
    pen.left(90)
    pen.forward(c)
    pen.left(90)
    pen.forward(c)


def spiral_of_fibonacci(a) :
    initial = pen.pos()
    square(a)
    pen.pencolor("red") 
    pen.speed("fastest")
    pen.goto(initial)
    pen.speed(3)
    pen.left(90)
    quartercircle(a)
    
for a in fibo :
    spiral_of_fibonacci(a)
    
        
    
pen.exitonclick()
    
    
           
    
    
import turtle # Tess becomes a traffic light.

turtle.setup(1280,720)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

size = 1
tela = 0
pen = 1

def redPen():
    """
    ao apertar a tecla "r", a caneta se torna vermelha
    """
    tess.pencolor("red")

def greenPen():
    """
    ao apertar a tecla "g", a caneta se torna verde
    """
    tess.pencolor("green")

def bluePen():
    """
    ao apertar a tecla "b", a caneta se torna azul
    """
    tess.pencolor("blue")

def up():
   """
   ao apertar a seta para cima, a tartaruga anda na direção que está olhando
   """

   tess.forward(10)

def down():
   """
   ao apertar a seta para baixo, a tartaruga anda na direção contrária à que está olhando
   """
   tess.back(10)

def right():
    """
    ao apertar a seta para direita, a tartaruga vira 90 graus à direita
    """
    tess.right(90)

def left():
    """
        ao apertar a seta para esquerda, a tartaruga vira 90 graus à esquerda
    """
    tess.left(90)

def grow():
    """
    Ao apertar a tecla "c", a ceneta deixa sua linha mais grossa, até o tamanho máximo de 20.
    Nao foi possivel implementar essa funcao na tecla "+" devido à bugs em alguma biblioteca do Anaconda.
    """
    global size
    if size < 20:
        tess.pensize(size + 1)
    size += 1

def shrink():
    """
    Ao apertar a tecla "s", a ceneta deixa sua linha mais fina, até o tamanho mínimo de 1
    Nao foi possivel implementar essa funcao na tecla "-" devido à bugs na biblioteca do Anaconda.
    """
    global size
    if size > 1:
        tess.pensize(size - 1)
    size -= 1

def background():
    """
    Ao apertar a tecla "l", a cor do plano de fundo alterna entre laranja, branco e azul claro
    """
    global tela
    if tela == 0:
        wn.bgcolor("orange")
        tela = 1
    elif tela == 1:
        wn.bgcolor("white")
        tela = 2
    elif tela == 2:
        wn.bgcolor("lightblue")
        tela = 0

def pen_up_down():
    """
    Ao apertar a tecla "p", a ceneta para de escrever, e ao apertar novamente, ela volta a escrever
    """
    global pen
    if pen == 1:
        tess.penup()
        pen = 0
    else:
        tess.pendown()
        pen = 1


wn.onkey(redPen, "r")
wn.onkey(greenPen, "g")
wn.onkey(bluePen, "b")

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkey(right, "Right")
wn.onkey(left, "Left")

wn.onkey(grow, "c")
wn.onkey(shrink, "s")

wn.onkey(background, "l")
wn.onkey(pen_up_down,"p")


wn.listen()  # Listen for events
wn.mainloop()
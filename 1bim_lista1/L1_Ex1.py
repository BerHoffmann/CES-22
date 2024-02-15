import turtle

def draw_square(dona, size):
    """
    Desenha um quadrado de tamanho 'size'
    utilizando a turtle 'dona'
    """
    dona.forward(size / 2)
    for i in range(3):
        dona.right(90)
        dona.forward(size)
    dona.right(90)
    dona.forward(size / 2)

def next_square():
    """
    Move a turtle sem desenhar para uma posição externa ao quadrado
    desenhado para estar no local adequado para desenhar o próximo quadrado
    """
    dona.penup()
    dona.left(90)
    dona.forward(10)
    dona.right(90)
    dona.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
dona = turtle.Turtle()
dona.color("pink")
dona.pensize(3)

for i in range(5):
    draw_square(dona, (20 + (i) * 20))
    next_square()

dona.hideturtle()
wn.mainloop()


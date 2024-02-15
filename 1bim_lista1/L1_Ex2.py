import turtle

def draw_polygon(t, n, sz):
    """
    desenha um polígono de n lados, os quais possuem
    tamanho sz, utilizando a turtle t
    """
    ext = 360 / n
    for i in range(n):
        t.forward(sz)
        t.left(ext)

lados = int(input("Number of sides of the polygon? "))
size = float(input("Size of each side? "))
wn = turtle.Screen()
wn.bgcolor("lightgreen")
dona = turtle.Turtle()
dona.color("pink")
dona.pensize(4)
draw_polygon(dona, lados, size)
wn.mainloop()

import turtle # Tess becomes a traffic light.
import time

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

inicio = time.time()

def tempo():
    """
    Retorna o tempo de execucao da aplicacao desde a ultima vez que o "inicio" foi reiniciado
    """
    return time.time() - inicio

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def statetimer():
    """
    Define o tempo em que a funcao advance_state_machine seja acionada.
    Os requisitos de state_num sao para que cada um das luzes do semafaro possam ter
    tempos distintos.
    """
    global inicio
    global state_num
    if state_num == 0 and tempo() > 5:
        advance_state_machine()
        inicio = time.time()
    elif state_num == 1 and tempo() > 1:
        advance_state_machine()
        inicio = time.time()
    elif tempo() > 4:
        advance_state_machine()
        inicio = time.time()
    wn.ontimer(statetimer, 1000)

wn.ontimer(statetimer, 1000)
wn.mainloop()



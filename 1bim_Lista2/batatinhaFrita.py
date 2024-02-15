import turtle # Tess becomes a traffic light.
import time

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
p1 = turtle.Turtle()
p2 = turtle.Turtle()

tess.penup()
tess.left(90)
tess.forward(100)
tess.left(90)
tess.pendown()
tess.forward(1000)
tess.left(180)
tess.forward(1400)

p1.pencolor("red")
p1.penup()
p1.right(90)
p1.forward(400)
p1.right(90)
p1.forward(600)
p1.right(90)

p2.pencolor("blue")
p2.penup()
p2.right(90)
p2.forward(400)
p2.right(90)
p2.forward(560)
p2.right(90)


inicio = time.time()

def tempo():
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
def movep1():
    p1.forward(10)

def movep2():
    p2.forward(10)

def statetimer():
    global inicio
    global state_num
    wn.onkeypress(movep1, "w")
    wn.onkeypress(movep2, "Up")
    if state_num == 0 and tempo() > 4:
        advance_state_machine()
        inicio = time.time()
        print("entrou")
    elif state_num == 1 and tempo() > 1:
        advance_state_machine()
        inicio = time.time()
    elif tempo() > 4:
        advance_state_machine()
        inicio = time.time()

    wn.ontimer(statetimer, 10)


wn.ontimer(statetimer, 100)


wn.mainloop()




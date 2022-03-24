import turtle as tr
import random as rd

def bubbles(n):
    tr.shape('turtle')
    tr.bgcolor('black')
    tr.speed('fast')
    tr.up()
    colors = ['blue', 'MediumAquamarine', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'paleturquoise', 'aqua', 'deepskyblue', 'cornflowerblue', 'seagreen', 'royalblue', 'slateblue', 'teal']
    for i in range(n):
        tr.goto(rd.randint(-200, 200), rd.randint(-200,200))
        tr.down()
        tr.color(rd.choice(colors))
        tr.circle(rd.randint(20, 150))
        tr.up()
    tr.done()

bubbles(10)

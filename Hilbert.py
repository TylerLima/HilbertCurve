"""
@Author: Tyler Lima tpl8254@rit.edu

Purpose: Trying out Hilbert curve to perform space-filling function. Create a grid of users desire, then fill that space
         with a Pseudo-Hilbert Curve to prove that any square/grid formation can be filled using the Hilbert Curve.

"""


import turtle as t

# Variables

# how big should each grid square be? (Square Size)
ss = 70

# how big should the grid be?
gridH = 8
gridW = 8

depth = 3


# methods

def flip_bool(top):
    if top:
        return False
    else:
        return True


def turn_right():
    t.forward(ss)
    t.rt(90)


def draw_box():
    t.forward(ss)
    t.rt(90)
    t.forward(ss)
    t.rt(90)
    t.forward(ss)
    t.rt(90)
    t.forward(ss)
    t.rt(90)
    t.forward(ss)


def draw_y_segment(y):
    while y != 0:
        draw_box()
        y -= 1


def draw_grid(x, y, top):
    myTurtle1 = t.Turtle()
    myTurtle1.speed(0)
    t.lt(90)

    while x != 0:
        draw_y_segment(gridH)
        top = flip_bool(top)

        if top:
            t.rt(90)
            t.fd(ss*2)
            t.rt(90)

        else:
            t.lt(180)

        x -= 1


# Hilbert code taken from: "http://blog.klipse.tech/python/2017/01/04/python-turtle-fractal.html"
# Use as a guide to create my own smart hilbert curve
def hilbert(step, rule, angle, depth, t):
    if depth > 0:
        a = lambda: hilbert(step, "a", angle, depth - 1, t)
        b = lambda: hilbert(step, "b", angle, depth - 1, t)
        left = lambda: t.left(angle)
        right = lambda: t.right(angle)
        forward = lambda: t.forward(step)
        if rule == "a":
            left();
            b();
            forward();
            right();
            a();
            forward();
            a();
            right();
            forward();
            b();
            left();
        if rule == "b":
            right();
            a();
            forward();
            left();
            b();
            forward();
            b();
            left();
            forward();
            a();
            right();


def draw_hilbert_curve():
    myTurtle = t.Turtle()
    myTurtle.speed = 0
    myTurtle.up()
    myTurtle.lt(90)
    myTurtle.fd(ss/2)
    myTurtle.rt(90)
    myTurtle.fd(ss/2)
    myTurtle.down()
    hilbert(ss, "a", 90, depth, myTurtle)


if __name__ == '__main__':

    draw_grid(gridW, gridH, False)

    # TODO: modify the hilbert method to fit inside the grid formed
    draw_hilbert_curve()
    t.done()









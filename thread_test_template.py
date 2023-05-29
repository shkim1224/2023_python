# thread test program
import turtle
import threading   # 몇 개의 함수를 동시에 실행시키기 위해 threading 모쥴을 import
from time import sleep

t = turtle.Turtle()
t.shape("turtle")
t1 = turtle.Turtle()
t1.shape("circle")

def draw_rect_t():

    for i in range(4):
        t.forward(100)
        sleep(1)
        t.left(90)

def draw_rect_t1():

    for i in range(4):
        t1.forward(100)
        sleep(0.5)
        t1.left(90)




turtle.mainloop()
turtle.bye()
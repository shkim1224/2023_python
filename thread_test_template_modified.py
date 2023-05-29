# thread test program
import turtle
import threading   # 몇 개의 함수를 동시에 실행시키기 위해 threading 모쥴을 import
from time import sleep

t = turtle.Turtle()
t.shape("turtle")
t1 = turtle.Turtle()
t1.shape("circle")

def draw_rect_t(a):
    for i in range(4):
        a.forward(100)
        sleep(1)
        a.left(90)

def draw_rect_t1(b):
    for i in range(4):
        b.forward(100)
        sleep(0.5)
        b.left(90)

t_thread = threading.Thread(target=draw_rect_t,args=(t,))
t1_thread = threading.Thread(target=draw_rect_t1,args=(t1,))
t_thread.start()
t1_thread.start()

turtle.mainloop()
turtle.bye()
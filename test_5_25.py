import turtle
t = turtle.Turtle()
t.shape("turtle")
t1 = turtle.Turtle()
t1.shape("circle")
print("id of t =",id(t))
print("id of t1 =",id(t1))
#t1.fillcolor('violet')
#s = input("몇각형을 원하시나요?:")
#n=int(s)

def draw_rect_t(a):
    print("****inside of func1*****")
    print("id of a =",id(a))
    for i in range(4):
        a.forward(100)
        a.left(90)

def draw_rect_t1(b):
    print("****inside of func2*****")
    print("id of b =",id(b))
    for i in range(4):
        b.forward(100)
        b.left(90)

draw_rect_t(t)
draw_rect_t1(t1)

turtle.mainloop()
turtle.bye()
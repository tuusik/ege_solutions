from turtle import*

screensize(10000,10000)
k=15
tracer(0)

for i in range(9):
    fd(15*k)
    rt(90)
    fd(25*k)
    rt(90)
up()
bk(10*k)
rt(90)
down()
for i in range(8):
    fd(15*k)
    lt(90)
    fd(25*k)
    lt(90)
up()
fd(6*k)
lt(90)
down()
for i in range(7):
    fd(15*k)
    rt(90)
    fd(25*k)
    rt(90)
up()
for x in range(30):
    for y in range(40):
        goto(x*k,-y*k+180)
        dot(5,'Red')

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
forward(-200)
for i in range (18):
    left(20)
    for j in range (0,4):
        forward(50)
        left(90)    
left(30)
end_fill()
done()

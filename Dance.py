from Myro import *
forward(2,2)
def electricslide():
 spin=0
 while spin<4:
   turnBy(90)
   forward(2,1)
   turnBy(180)
   forward(2,1)
   turnBy(90)
   backward(2,1)
   forward(1,1)
   backward(1,1)
   turnBy(90)
   backward(1,1)
   forward(1,1)
   turnBy(90)
   forward(2,1)
   backward(2,1)
   spin=spin+1
electricslide()
turnBy(360)
forward(.5,1)
backward(.5,1)
turnBy(360)
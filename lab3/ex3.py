from turtle import *
from numpy import *

def addnum(num:int):
    inp = open('ex3_sup.txt', 'r').readlines()
    s = inp[num].rstrip()
    commlist = s.split(' -> ')
    for command in commlist:
        eval(command)


def drawindex(index:float):
    for num in index:
        addnum(int(num))


shape('turtle')
speed(8)
color('blue','blue')
width(3)
left(90)
index = '141700'
drawindex(index) 
done()

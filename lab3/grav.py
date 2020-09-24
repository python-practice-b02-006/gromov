import turtle as tl

g = -10
vx = 10
vy = 60
dt = 0.05
k = 0.01

ax = -k * vx; ay = g - k*vy; asx = 0; asy = 0; vsx = 0; vsy = 0; ux = 0; uy = 0; x = -200; y = 0; 

tl.penup(); tl.goto(x, y); tl.pendown(); tl.shape("circle");

while 0 == 0:
    vsx = vx + ax*dt
    asx = -k * vsx
    ax = -k * vx
    ux = vx + dt * (ax + asx)/2
    vsy = vy + ay*dt
    asy = -k*vsy + g 
    ay = -k * vy
    uy = vy + dt * (ay + asy)/2
    x = x + dt * (vx + ux)/2
    y = y + dt * (vy + uy)/2
    tl.goto(x, y)
    vx = ux
    vy = uy
    if y <= 0: vy = -vy
tl.done()

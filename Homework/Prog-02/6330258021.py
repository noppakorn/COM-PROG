# Prog-02: Elastic Collision
# 6330258021 Noppakorn Jiravaranun

import math
import random
from matplotlib import pyplot as plt
from matplotlib import animation, rc

WIDTH, HEIGHT = 300, 300

class Ball(plt.Circle) :
    def __init__(self, r=None, xy=None,
                 v=None, color=None):
        if r == None: 
            r = random.randint(4, 10)
        if xy == None:
            x = random.randint(r, WIDTH-r)
            y = random.randint(r, HEIGHT-r)
            xy = (x,y)
        if v == None:
            dx = -5 + random.random()*10
            dy = -5 + random.random()*10
            v = (dx,dy)
        self.v = v
        if color == None: 
            color = [random.random() for i in range(3)]
        super().__init__(xy, radius=r, facecolor=color)

def update_v_if_collide(b1, b2):
    x1, y1 = b1.center
    x2, y2 = b2.center
    r1 = b1.radius
    r2 = b2.radius
    v1x, v1y = b1.v
    v2x, v2y = b2.v
    dx = x1 - x2
    dy = y1 - y2
    t = dx**2 + dy**2 - (r1+r2)**2
    if t <= 0:
        if t < 0:
            x1 -= v1x; y1 -= v1y
            x2 -= v2x; y2 -= v1y
        b1.v, b2.v = update_v(x1, y1, r1, v1x, v1y,
                              x2, y2, r2, v2x, v2y)

def update_v(x1, y1, r1, v1x, v1y, 
             x2, y2, r2, v2x, v2y):
    m1,m2 = r1**2,r2**2
    theta1,theta2 = math.atan2(v1y,v1x),math.atan2(v2y,v2x)
    v1,v2 = v1y/math.sin(theta1),v2y/math.sin(theta2)
    phi = math.atan2((y2-y1),(x2-x1))
    v1_x = ((((v1*math.cos(theta1-phi)*(m1-m2)) + (2*m2*v2*math.cos(theta2-phi)))/(m1+m2)) * math.cos(phi)) + (v1*math.sin(theta1-phi)*math.cos(phi+math.pi/2))
    v1_y = ((((v1*math.cos(theta1-phi)*(m1-m2)) + (2*m2*v2*math.cos(theta2-phi)))/(m1+m2)) * math.sin(phi)) + (v1*math.sin(theta1-phi)*math.sin(phi+math.pi/2))
    v2_x = ((((v2*math.cos(theta2-phi)*(m2-m1)) + (2*m1*v1*math.cos(theta1-phi)))/(m1+m2)) * math.cos(phi)) + (v2*math.sin(theta2-phi)*math.cos(phi+math.pi/2))
    v2_y = ((((v2*math.cos(theta2-phi)*(m2-m1)) + (2*m1*v1*math.cos(theta1-phi)))/(m1+m2)) * math.sin(phi)) + (v2*math.sin(theta2-phi)*math.sin(phi+math.pi/2))
    return (v1_x, v1_y), (v2_x, v2_y)

def move(ball):
    x, y = ball.center
    vx, vy = ball.v
    r = ball.radius
    x += vx
    y += vy
    if not (r <= x <= WIDTH-r):
        vx *= -1
        x += vx
        if x-r < 0: x = r
        if x+r > WIDTH: x = WIDTH-r
    if not (r <= y <= HEIGHT-r):
        vy *= -1
        y += vy
        if y-r < 0: y = r
        if y+r > HEIGHT: y = HEIGHT-r
    ball.center = (x,y)
    ball.v = (vx,vy)

def total_Ek():
    sum_Ek = sum(0.5*(balls[i].radius**2 *
                      (balls[i].v[0]**2 + balls[i].v[1]**2))
                  for i in range(len(balls)))
    return sum_Ek

def animate(i):
    for i in range(len(balls)):
        move(balls[i])
    print(total_Ek())        
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            update_v_if_collide(balls[i], balls[j])
    return balls

#--------------------------------------------------
fig, ax = plt.subplots()
fig.set_size_inches(4,4)
ax.set_xlim((0, WIDTH))
ax.set_ylim((0, HEIGHT))

balls = []
n = 9
for i in range(n):
    b = Ball(xy = ((i+1)*WIDTH/(n+1), HEIGHT-70), v=(0,-1))
    balls.append(b)
    ax.add_patch(b)
b = Ball(xy=(WIDTH/2, 40), r=30, v=(1,5), color='red')
balls.append(b)
ax.add_patch(b)
anim = animation.FuncAnimation(fig, animate, 
                               frames=None,
                               interval=30,
                               blit=True)
plt.show()
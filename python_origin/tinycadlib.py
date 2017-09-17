from math import pi, cos, sin, sqrt, acos
 
radian = 180/pi
degree = pi/180

#PLAP
def plap(ax, ay, ac, bac, bx, by, ccw):
    if ccw == 1:
        cx= ac*cos(bac - acos((ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 + abs(ax - bx)**2 - abs(ay - by)**2)/(2*sqrt(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2)*abs(ax - bx)))) + ax 
        cy= ac*sin(bac - acos((ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 + abs(ax - bx)**2 - abs(ay - by)**2)/(2*sqrt(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2)*abs(ax - bx)))) + ay
    else:
        cx= ac*cos(bac + acos((ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 + abs(ax - bx)**2 - abs(ay - by)**2)/(2*sqrt(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2)*abs(ax - bx)))) + ax 
        cy= ac*sin(bac + acos((ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 + abs(ax - bx)**2 - abs(ay - by)**2)/(2*sqrt(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2)*abs(ax - bx)))) + ay
    return cx, cy

#PLLP
def pllp(ax, ay, ac, cb, bx, by, cw):
    if cw == 1:
        cx =  -((ay - by)*(-ac**2*ay + ac**2*by + ax**2*ay + ax**2*by - 2*ax*ay*bx - 2*ax*bx*by + ay**3 - ay**2*by + ay*bx**2 - ay*by**2 + ay*cb**2 + bx**2*by + by**3 - by*cb**2 - sqrt((-ac**2 + 2*ac*cb + ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 - cb**2)*(ac**2 + 2*ac*cb - ax**2 + 2*ax*bx - ay**2 + 2*ay*by - bx**2 - by**2 + cb**2))*(ax - bx)) + (ac**2 - ax**2 - ay**2 + bx**2 + by**2 - cb**2)*(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2))/(2*(ax - bx)*(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2))
        cy =  (-ac**2*ay + ac**2*by + ax**2*ay + ax**2*by - 2*ax*ay*bx - 2*ax*bx*by + ay**3 - ay**2*by + ay*bx**2 - ay*by**2 + ay*cb**2 + bx**2*by + by**3 - by*cb**2 + sqrt((-ac**2 + 2*ac*cb + ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 - cb**2)*(ac**2 + 2*ac*cb - ax**2 + 2*ax*bx - ay**2 + 2*ay*by - bx**2 - by**2 + cb**2))*(-ax + bx))/(2*(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2))
    else:
        cx =  -((ay - by)*(-ac**2*ay + ac**2*by + ax**2*ay + ax**2*by - 2*ax*ay*bx - 2*ax*bx*by + ay**3 - ay**2*by + ay*bx**2 - ay*by**2 + ay*cb**2 + bx**2*by + by**3 - by*cb**2 + sqrt((-ac**2 + 2*ac*cb + ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 - cb**2)*(ac**2 + 2*ac*cb - ax**2 + 2*ax*bx - ay**2 + 2*ay*by - bx**2 - by**2 + cb**2))*(ax - bx)) + (ac**2 - ax**2 - ay**2 + bx**2 + by**2 - cb**2)*(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2))/(2*(ax - bx)*(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2))
        cy =  (-ac**2*ay + ac**2*by + ax**2*ay + ax**2*by - 2*ax*ay*bx - 2*ax*bx*by + ay**3 - ay**2*by + ay*bx**2 - ay*by**2 + ay*cb**2 + bx**2*by + by**3 - by*cb**2 + sqrt((-ac**2 + 2*ac*cb + ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2 - cb**2)*(ac**2 + 2*ac*cb - ax**2 + 2*ax*bx - ay**2 + 2*ay*by - bx**2 - by**2 + cb**2))*(ax - bx))/(2*(ax**2 - 2*ax*bx + ay**2 - 2*ay*by + bx**2 + by**2))
    return cx, cy

def PLLP(x0, y0, L0, R0, x1, y1, loop=1):
    return (
        -loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-y0 + y1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0 + (-x0 + x1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2)),
        loop*sqrt(L0**2 - (L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)**2/(4*((x0 - x1)**2 + (y0 - y1)**2)))*(-x0 + x1)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0 + (-y0 + y1)*(L0**2 - R0**2 + (x0 - x1)**2 + (y0 - y1)**2)/(2*sqrt((-x0 + x1)**2 + (-y0 + y1)**2)*sqrt((x0 - x1)**2 + (y0 - y1)**2))
    )

def PLAP(x0, y0, L0, a0, x1, y1, loop=1):
    return (
        -L0*loop*(-y0 + y1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-x0 + x1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + x0,
        L0*loop*(-x0 + x1)*sin(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + L0*(-y0 + y1)*cos(a0)/sqrt((-x0 + x1)**2 + (-y0 + y1)**2) + y0
    )

if __name__=='__main__':
    ax = -38
    ay = 0
    # b 為原點
    bx = 0
    by = 0
    cx = 0
    cy = 7.8
    # m 為配合 PLAP 新增固定點
    mx = 30
    my = 7.8
    # dcm ccw 方向角度
    dcm = 30*degree
    cd = 15
    # 三角形 dcm 為 ccw plap d=(a, cd, dcm, m)
    dx, dy = plap(cx, cy, cd, dcm, mx, my, ccw=1)
    print("dx=", dx, "dy=", dy)
    dx, dy = PLAP(cx, cy, cd, dcm, mx, my, loop=1)
    print("dx=", dx, "dy=", dy)
    # 三角形 aed 為 cw pllp e=(a, ae, ed, d)
    ae = 41.5
    ed = 50
    ex, ey = pllp(ax, ay, ae, ed, dx, dy, cw=1)
    print("ex=", ex, "ey=", ey)
    ex, ey = PLLP(ax, ay, ae, ed, dx, dy, loop=1)
    print("ex=", ex, "ey=", ey)

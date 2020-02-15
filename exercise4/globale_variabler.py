import math
GRAVITY = 9.81
def getFallTime(d,gravity):
    global GRAVITY
    GRAVITY = gravity
    t=math.sqrt(2*d/GRAVITY)
    return t
print(getFallTime(20,1.62))

import numpy as np
import random as rnd
def Generate(a,b,size):
    reqest = np.zeros(size)
    for i in range(size):
        reqest[i] =rndbetavariate(a,b)

    return reqest
def rndbetavariate(a,b):
    y = rnd.gammavariate(a, 1.0)
    if y:
        return y / (y + rnd.gammavariate(b, 1.0))
    return 0.0
    return y

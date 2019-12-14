# exec with using python3

import numpy as np
import math

a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = np.array(a)
B = np.array(b)

x = np.inner(A,B)
print(x)

s = np.linalg.norm(A)
t = np.linalg.norm(B)
print(s)
print(t)

theta = np.arccos(x/(s*t))
print(theta)

deg = math.degrees(theta)
print(deg)

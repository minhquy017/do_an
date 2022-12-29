import random
import numpy as np


def tinh_tich(x, A):
    s = x * A
    print("X*A", s)
    return s
def tinh_tich_hadamard(A,B):
    x = np.multiply(A, B)
    return x

def tich_chuyen_vi(A1, B1):
    chuyen = A1.transpose()
    x = np.dot(chuyen,B1)
    print('sau khi chuyển vị A = \n  ', chuyen)
    print("At*B = ", x)
    return x

# sinh dữ liệu

def main():
    x1 = 2
    A = np.random.randint(low=-5, high=5, size=16).reshape((4, 4))
    a = np.array(A)
    B = np.random.randint(low=-5, high=5, size=16).reshape((4, 4))
    b = np.array(B)
    print("x = ", x1)
    print("A=", a)
    print("B = ", b)
    z=tinh_tich(x1,A)
    z1=tinh_tich_hadamard(a,b)
    z1 = tich_chuyen_vi(a,b)
    return z ,z1


if __name__=="__main__":
  main()
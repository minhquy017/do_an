#1
from sympy.plotting import  plot
from sympy import *

def do_thi(x):
  y = x**4-2*x**2-3
  return y

def dao_ham1(x):
  x=symbols("x")
  f=do_thi(x)
  ket_qua= diff(f,x)
  return ket_qua
def dao_ham2(x):
  x=symbols("x")
  f=dao_ham1(x)
  ket_qua= diff(f,x)
  return ket_qua
def dao_ham3(x):
  x=symbols("x")
  f=dao_ham2(x)
  ket_qua= diff(f,x)
  return ket_qua

def main():
  x=symbols("x")
  plot(do_thi(x),dao_ham1(x),dao_ham2(x),dao_ham3(x),(x,-10,10),title="đồ thị y=x**4-2*x**2-3 và các đạo hàm của nó",xlabel="trục hoành x",ylabel="trục tung y")

if __name__ == "__main__":
      main()
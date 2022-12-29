#1
from sympy.plotting import  plot
from sympy import *
import sympy as sp
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
  p = sp.plot(do_thi(x), (x, -10, 10), legend=True, line_color="red",show=False)
  p.extend(sp.plot(dao_ham1(x), (x, -10, 10), legend=True, line_color="green",show=False))
  p.extend(sp.plot(dao_ham2(x), (x, -10, 10), legend=True, line_color="orange",show=False))
  p.extend(sp.plot(dao_ham3(x), (x, -10, 10), legend=True, line_color="blue", show=False))
  p.show()


if __name__ == "__main__":
      main()
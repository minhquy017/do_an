#1
import math
import sympy
def giai_he_pt():
  x,y,z=sympy.symbols( " x y z ")
  eq1= sympy.Eq(2*x-5*y+z,-5)
  eq2= sympy.Eq(4*x +2*y-2*z,2)
  eq3= sympy.Eq(x+y-z,0)
  ket_qua= sympy.solve((eq1,eq2,eq3),(x , y , z))
  print(ket_qua)
  return ket_qua

#2
def tinh_gioi_han():
  x=sympy.symbols("x")
  f= (x**3-3*x**2)**1/3 + (x**2-2*x)**1/2
  ket_qua=sympy.limit(f,x,math.inf)
  print(ket_qua)
  return ket_qua

#3
def tinh_dao_ham():
  x=sympy.symbols("x")
  f=(2*x-1)/(x+2)
  ket_qua=sympy.diff(f,x)
  print(ket_qua)
  return ket_qua


#4
def tinh_nguyen_ham():
  x=sympy.symbols("x")
  f=x/(x**2+1)
  ket_qua= sympy.integrate(f,x)
  print(ket_qua)
  return ket_qua


#5
def tinh_tich_phan():
  x=sympy.symbols("x")
  f = (1-x*sympy.tan(x))/(x**2*sympy.cos(x)+x)
  ket_qua=sympy.integrate(f,(x,2*math.pi/3,math.pi))
  print(ket_qua)
  return ket_qua

def main():
  x1=giai_he_pt()
  x2=tinh_gioi_han()
  x3=tinh_dao_ham()
  x4=tinh_nguyen_ham()
  x5=tinh_tich_phan()

if __name__ == '__main__':
      main()

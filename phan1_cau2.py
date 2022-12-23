#1
import os
import numpy as np
import random
import pickle
def sinh_ngau_nhien():
  a=-2
  b=3
  x1=(b-a)*np.random.random_sample(10)+a
  print("x1 = ",x1)
  return x1

def sap_xep(x1,reverse):
  if reverse == False :
    n = len(x1)
    for i in range(0, n - 1):
      for j in range(i + 1, n):
        if x1[i] < x1[j]:
          x1[i], x1[j] = x1[j], x1[i]
    print("sắp xếp giảm dần : ",x1)
    return x1
  if reverse ==True:
    n = len(x1)
    for i in range(0, n - 1):
      for j in range(i + 1, n):
        if x1[i] > x1[j]:
          x1[i], x1[j] = x1[j], x1[i]
    print("sắp xếp tăng dần ",x1)
    return x1

def tim_kiem(x2,v):
  vitri = []
  for i in range(len(x2)):
    if abs(x2[i] - v) < 0.001:
      vitri.append(i)
  if len(vitri)>0:
    print("tìm thấy các vị trí của nó là : ",vitri)
  else :
    print("không tìm thấy")
def luu_tap_tin(thu_muc:str,tap_tin:str,danh_sach:str, m:str):
  if m == "w":
    try:
      with open(os.path.join(thu_muc,tap_tin),"w")as f :
        f.write(str(danh_sach))
      print("hoàn thành lưu")
    except Exception as e:
      print("lỗi rồi ",e)
  if m == "wb":
    try:
      with open(os.path.join(thu_muc,tap_tin),"wb") as f:
        pickle.dump(str(danh_sach))
      print("hoành thành ")
    except Exception as e:
      print("lỗi rồi ",e)
def main ():
  x=sinh_ngau_nhien()
  path = "C:/Users/MINH QUY"
  file = "cau1.txt"
  n=str(input("nhập kiểu : "))
  luu_tap_tin(path,file,x,n)
  y1=sap_xep(x,False)
  file2= "cau11.txt"
  luu_tap_tin(path,file2,y1,n)
  tim_kiem(y1,float(input("nhập số cần tìm : ")))


if __name__=="__main__":
  main()




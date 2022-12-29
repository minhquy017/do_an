from phan3_oop import NhanVien
import pickle
import os
def nhap_nhanvien(ds):
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        hoten = input("Nhập họ tên nhân viên: ")
        tuoi = int(input("Nhập tuổi nhân viên: "))
        luong = int(input("Nhập lương nhân viên: "))
        nhan_vien=NhanVien(hoten,tuoi,luong)
        ds.append(nhan_vien)

def hien_thi_danh_sach_nhan_vien(ds):
        for nhan_vien in ds :
            print(nhan_vien)
def sap_xep_tuoi(ds):
    ds.sort(key=lambda x: x.tuoi, reverse=True)

def luu_danh_sach_nhan_vien(thu_muc:str , ten_tap_tin:str ,x):
        try:
            with open(os.path.join(thu_muc,ten_tap_tin), "wb") as f:
                pickle.dump(x,f)
                print("hoàn thành lưu")
        except Exception as e:
            print("lỗi rồi ", e)

def doc_nhanvien(thu_muc:str, ten_taptin: str) :
        try:
            with open(os.path.join(thu_muc, ten_taptin), 'rb') as f:
                nv = pickle.load(f)
            return nv
        except Exception as e:
            return None

def in_list_nhan_vien (s: list[NhanVien]):
    for i in s:
        print(i)

def main():
        x = []
        nhap_nhanvien(x)
        sap_xep_tuoi(x)
        hien_thi_danh_sach_nhan_vien(x)
        luu_danh_sach_nhan_vien("C:/Users/Minh Quy","doc.txt",x)
        noi_dung=doc_nhanvien("C:/Users/Minh Quy","doc.txt")
        in_list_nhan_vien(noi_dung)

if __name__ == '__main__':
    main()

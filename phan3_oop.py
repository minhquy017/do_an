
class NhanVien:

    def __init__(self,hoten,tuoi,luong):
        self.hoten=hoten
        self.tuoi=tuoi
        self.luong=luong
    def __str__(self):
        message = "[hoten: " + self.hoten + "; tuoi:" + str(self.tuoi) + "; luong: " + str(self.luong) + "]"
        return message






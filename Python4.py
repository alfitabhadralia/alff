class motor:
    def _init_(self, warna, tahun, merk):
        self.warna  = warna
        self.tahun = tahun
        self.merk = merk

    def printname(self):
        print(self.warna)
        print(self.tahun)
        print(self.merk)

class matic(motor):
    def  __init__(self, warna, tahun, merk):
        motor._init_(self, warna, tahun, merk)
        self.produk ="Beat"

    def tampilanmatic(self):
        print("Jenis Matic :", self.produk)
        print("Merk        :", self.merk)
        print("Warna       :", self.warna)
        print("Tahun       :", self.tahun)

class manual(motor):
    def  __init__(self, warna, tahun, merk):
        motor._init_(self, warna, tahun, merk)
        self.produk ="Satria F U"

    def tampilanmanual(self):
        print("Jenis Matic :", self.produk)
        print("Merk        :", self.merk)
        print("Warna       :", self.warna)
        print("Tahun       :", self.tahun)

x = matic("Putih", 2020, "Honda")
y = manual("Hitam", 2019, "Suzuki")

x.printname()
print("***************************")
y.printname() 

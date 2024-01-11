import datetime

DataParkir = []

def parkirKendaraan():
    PlatNomor = input("\nMasukkan Plat Nomor      : ")
    JenisKendaraan = input("Masukkan Jenis Kendaraan : ")
    TipeKendaraan = input("Masukkan Tipe Kendaraan  : ")
    ParkirKendaraan = {'Plat Nomor' : PlatNomor, 'Jenis Kendaraan' : JenisKendaraan, 'Tipe Kendaraan' : TipeKendaraan, 'Waktu Masuk' : datetime.datetime.now()}
    DataParkir.append(ParkirKendaraan)
    return parkirKendaraan

def daftarParkir():
    print("\n========Daftar Parkir========")
    for i, ParkirKendaraan in enumerate(DataParkir, start=1):
        print(f"{i}. Plat Nomor           : {ParkirKendaraan['Plat Nomor']} \n   Jenis Kendaraan      : {ParkirKendaraan['Jenis Kendaraan']} \n   Tipe Kendaraan       : {ParkirKendaraan['Tipe Kendaraan']}")

def inputTarif(DataParkir):
    daftarParkir()
    if DataParkir:
        pilih = int(input("Pilih nomor untuk menghitung tarif parkir : "))
        if 1 <= pilih <= len(DataParkir):
            SelectKendaraan = DataParkir[pilih - 1]
            PlatNomor = SelectKendaraan['Plat Nomor']
            JenisKendaraan = SelectKendaraan['Jenis Kendaraan']
            TipeKendaraan = SelectKendaraan['Tipe Kendaraan']
            TarifPerJam = int(input(f"Masukkan Tarif Per Jam untuk {JenisKendaraan}: "))
            WaktuMasuk = SelectKendaraan['Waktu Masuk']
            WaktuKeluar = datetime.datetime.now()
            TotalWaktu = (WaktuKeluar - WaktuMasuk).total_seconds() / 3600
            TotalTarif = TarifPerJam * TotalWaktu
            print("\n===========Nota===========")
            print(f"Plat Nomor          : {PlatNomor}")
            print(f"Jenis Kendaraan     : {JenisKendaraan}")
            print(f"Tipe Kendaraan      : {TipeKendaraan}")
            print(f"Tarif Per Jam       : {TarifPerJam}")
            print(f"Jam Masuk           : {WaktuMasuk}")
            print(f"Jam Keluar          : {WaktuKeluar}")
            print(f"Total tarif         : Rp.{TotalTarif}\n")
            print(datetime.datetime.now())
            print("========Terima Kasih========")
            return TotalTarif
        else:
            print("Belum ada Kendaraan yang ditambahkan")
    else:
        print("Plat Nomor Tidak Tersedia")

def hapusParkir():
    daftarParkir()
    if DataParkir:
        pilih = int(input("Pilih nomor untuk menghapus parkir : "))
        if 1 <= pilih <= len(DataParkir):
            del DataParkir[pilih - 1]
            print("Parkir berhasil dihapus")
        else:
            print("Nomor parkir tidak valid")
    else:
        print("Plat Nomor Tidak Tersedia")

while True:
    UserInput = input("\n========Program Parkir========\n A. Parkir Kendaraan\n B. Daftar Parkir\n C. Tarif Parkir\n D. Hapus Parkir\n E. Keluar\n Silahkan pilih : ")
    if UserInput == "a" or UserInput == "A":
        parkirKendaraan()
    elif UserInput == "b" or UserInput == "B":
        daftarParkir()
    elif UserInput == "c" or UserInput == "C":
        inputTarif(DataParkir)
    elif UserInput == "d" or UserInput == "D":
        hapusParkir()
    else:
        print("========Terima Kasih========")
        break
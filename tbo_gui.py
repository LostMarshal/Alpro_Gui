import datetime
import tkinter as tk
from tkinter import messagebox
DataParkir = []

def daftarParkir():
    if DataParkir:
        daftar_parkir = ""
        for i, ParkirKendaraan in enumerate(DataParkir, start=1):
            daftar_parkir += f"{i}. Plat Nomor           : {ParkirKendaraan['Plat Nomor']} \n   Jenis Kendaraan      : {ParkirKendaraan['Jenis Kendaraan']} \n   Tipe Kendaraan       : {ParkirKendaraan['Tipe Kendaraan']}\n\n"
        messagebox.showinfo("Daftar Parkir", daftar_parkir)
    else:
        messagebox.showinfo("Daftar Parkir", "Belum ada kendaraan yang ditambahkan.")

def inputTarif():
    if DataParkir:
        pilih = int(entry_pilih())
        if 1 <= pilih <= len(DataParkir):
            SelectKendaraan = DataParkir[pilih - 1]
            PlatNomor = SelectKendaraan['Plat Nomor']
            JenisKendaraan = SelectKendaraan['Jenis Kendaraan']
            TipeKendaraan = SelectKendaraan['Tipe Kendaraan']
            TarifPerJam = int(entry_tarif_per_jam.get())
            WaktuMasuk = SelectKendaraan['Waktu Masuk']
            WaktuKeluar = datetime.datetime.now()
            TotalWaktu = (WaktuKeluar - WaktuMasuk).total_seconds() / 3600
            TotalTarif = TarifPerJam * TotalWaktu
            messagebox.showinfo("Nota", f"Plat Nomor          : {PlatNomor}\nJenis Kendaraan     : {JenisKendaraan}\nTipe Kendaraan      : {TipeKendaraan}\nTarif Per Jam       : {TarifPerJam}\nJam Masuk           : {WaktuMasuk}\nJam Keluar          : {WaktuKeluar}\nTotal tarif         : Rp.{TotalTarif}")
        else:
            messagebox.showinfo("Input Tarif", "Nomor parkir tidak valid.")
    else:
        messagebox.showinfo("Input Tarif", "Plat Nomor Tidak Tersedia.")

def hapusParkir():
    if DataParkir:
        pilih = int(entry_pilih())
        if 1 <= pilih <= len(DataParkir):
            del DataParkir[pilih - 1]
            messagebox.showinfo("Hapus Parkir", "Parkir berhasil dihapus.")
        else:
            messagebox.showinfo("Hapus Parkir", "Nomor parkir tidak valid.")
    else:
        messagebox.showinfo("Hapus Parkir", "Plat Nomor Tidak Tersedia.")

def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Program Parkir")
    menu_window.geometry("300x200")

    label_menu = tk.Label(menu_window, text="Silahkan pilih:")
    label_menu.pack()

    button_parkir = tk.Button(menu_window, text="Parkir Kendaraan", command=lambda: [parkirKendaraan(), menu_window.destroy()])
    button_parkir.pack()

    button_daftar = tk.Button(menu_window, text="Daftar Parkir", command=lambda: [daftarParkir(), menu_window.destroy()])
    button_daftar.pack()

    button_tarif = tk.Button(menu_window, text="Tarif Parkir", command=lambda: [inputTarif(), menu_window.destroy()])
    button_tarif.pack()

    button_hapus = tk.Button(menu_window, text="Hapus Parkir", command=lambda: [hapusParkir(), menu_window.destroy()])
    button_hapus.pack()

    button_keluar = tk.Button(menu_window, text="Keluar", command=root.quit)
    button_keluar.pack()

root = tk.Tk()

root.title("Program Parkir")
root.geometry("300x200")

def parkirKendaraan():
    parkir = tk.Tk()
    parkir.title("Parkir kendaraan")
    parkir.geometry("300x200")

    plat_nomor_label = tk.Label(parkir, text="Plat Nomor")
    plat_nomor_label.pack()
    plat_nomor_entry = tk.Entry(parkir)
    plat_nomor_entry.pack()

    jenis_kendaraan_label = tk.Label(parkir, text="Jenis Kendaraan")
    jenis_kendaraan_label.pack()
    jenis_kendaraan_entry = tk.Entry(parkir)
    jenis_kendaraan_entry.pack()

    tipe_kendaraan_label = tk.Label(parkir, text="Tipe Kendaraan")
    tipe_kendaraan_label.pack()
    tipe_kendaraan_entry = tk.Entry(parkir)
    tipe_kendaraan_entry.pack()

    button_start = button_start = tk.Button(parkir, text="Parkir Kendaraan", command=lambda: parkirKendaraan(plat_nomor_entry.get(), jenis_kendaraan_entry.get(), tipe_kendaraan_entry.get()))
    button_start.pack()
    
    def parkirKendaraan(plat_nomor, jenis_kendaraan, tipe_kendaraan):
        ParkirKendaraan = {'Plat Nomor' : plat_nomor, 'Jenis Kendaraan' : jenis_kendaraan, 'Tipe Kendaraan' : tipe_kendaraan, 'Waktu Masuk' : datetime.datetime.now()}
        DataParkir.append(ParkirKendaraan)
        messagebox.showinfo("Success", "Vehicle parked successfully")
        parkir.destroy()


def entry_pilih():
    pilih_label = tk.Label(root, text="Pilih")
    pilih_label.pack()
    pilih_entry = tk.Entry(root)
    pilih_entry.pack()
    return entry_pilih

def entry_tarif_per_jam():
    tarif_per_jam_label = tk.Label(root, text="Tarif Per Jam")
    tarif_per_jam_label.pack()
    tarif_per_jam_entry = tk.Entry(root)
    tarif_per_jam_entry.pack()
    return entry_tarif_per_jam

label_title = tk.Label(root, text="Program Parkir")
label_title.pack()

button_start = tk.Button(root, text="Mulai", command=show_menu)
button_start.pack()

root.mainloop()

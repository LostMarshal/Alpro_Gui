import datetime
import tkinter as tk
from tkinter import messagebox

DataParkir = []

def parkirKendaraan(plat_nomor, jenis_kendaraan, tipe_kendaraan):
    ParkirKendaraan = {'Plat Nomor' : plat_nomor, 'Jenis Kendaraan' : jenis_kendaraan, 'Tipe Kendaraan' : tipe_kendaraan, 'Waktu Masuk' : datetime.datetime.now()}
    DataParkir.append(ParkirKendaraan)
    messagebox.showinfo("Success", "Vehicle parked successfully")

def daftarParkir():
    parkir_list = "\n".join([f"{i+1}. {parkir['Plat Nomor']} - {parkir['Jenis Kendaraan']} - {parkir['Tipe Kendaraan']}" for i, parkir in enumerate(DataParkir)])
    messagebox.showinfo("Parked Vehicles", parkir_list)

root = tk.Tk()

plat_nomor_label = tk.Label(root, text="Plat Nomor")
plat_nomor_label.pack()
plat_nomor_entry = tk.Entry(root)
plat_nomor_entry.pack()

jenis_kendaraan_label = tk.Label(root, text="Jenis Kendaraan")
jenis_kendaraan_label.pack()
jenis_kendaraan_entry = tk.Entry(root)
jenis_kendaraan_entry.pack()

tipe_kendaraan_label = tk.Label(root, text="Tipe Kendaraan")
tipe_kendaraan_label.pack()
tipe_kendaraan_entry = tk.Entry(root)
tipe_kendaraan_entry.pack()

parkir_button = tk.Button(root, text="Parkir Kendaraan", command=lambda: parkirKendaraan(plat_nomor_entry.get(), jenis_kendaraan_entry.get(), tipe_kendaraan_entry.get()))
parkir_button.pack()

daftar_parkir_button = tk.Button(root, text="Daftar Parkir", command=daftarParkir)
daftar_parkir_button.pack()

root.mainloop()
import datetime
import tkinter as tk
from tkinter import messagebox

DataParkir = []

def daftarParkir():
    if DataParkir:
        daftar_parkir = ""
        for i, ParkirKendaraan in enumerate(DataParkir, start=1):
            daftar_parkir += f"{i}. Plat Nomor               : {ParkirKendaraan['Plat Nomor']} \n    Jenis Kendaraan      : {ParkirKendaraan['Jenis Kendaraan']} \n    Tipe Kendaraan       : {ParkirKendaraan['Tipe Kendaraan']}\n\n"
        messagebox.showinfo("Daftar Parkir", daftar_parkir)
    else:
        messagebox.showinfo("Daftar Parkir", "Belum ada kendaraan yang ditambahkan.")

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

    button_tarif = tk.Button(menu_window, text="Tarif Parkir", command=lambda: [entry_pilih(), menu_window.destroy()])
    button_tarif.pack()

    button_hapus = tk.Button(menu_window, text="Hapus Parkir", command=lambda: [hapusParkir(), menu_window.destroy()])
    button_hapus.pack()

    button_keluar = tk.Button(menu_window, text="Keluar", command=root.quit)
    button_keluar.pack()

root = tk.Tk()
root.title("Program Parkir")
root.geometry("300x200")

def parkirKendaraan():
    parkir = tk.Toplevel(root)
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

    button_start = tk.Button(parkir, text="Parkir Kendaraan", command=lambda: saveParkir(plat_nomor_entry.get(), jenis_kendaraan_entry.get(), tipe_kendaraan_entry.get(), parkir))
    button_start.pack()

def saveParkir(plat_nomor, jenis_kendaraan, tipe_kendaraan, parkir_window):
    ParkirKendaraan = {'Plat Nomor': plat_nomor, 'Jenis Kendaraan': jenis_kendaraan, 'Tipe Kendaraan': tipe_kendaraan, 'Waktu Masuk': datetime.datetime.now()}
    DataParkir.append(ParkirKendaraan)
    messagebox.showinfo("Success", "Kendaraan berhasil diparkir.")
    parkir_window.destroy()

def entry_pilih():
    pilih_window = tk.Toplevel(root)
    pilih_window.title("Pilih kendaraan")
    pilih_window.geometry("300x200")

    pilih_label = tk.Label(pilih_window, text="Pilih")
    pilih_label.pack()
    pilih_entry = tk.Entry(pilih_window)
    pilih_entry.pack()

    button_start = tk.Button(pilih_window, text="Pilih Kendaraan", command=lambda: processEntryPilih(pilih_entry.get(), pilih_window))
    button_start.pack()

def processEntryPilih(pilih, pilih_window):
    try:
        pilih = int(pilih)
        entry_tarif_per_jam(pilih, pilih_window)
    except ValueError:
        messagebox.showinfo("Input Tarif", "Nomor parkir tidak valid.")

def entry_tarif_per_jam(selected_index, pilih_window):
    entry_tarif_window = tk.Toplevel(root)
    entry_tarif_window.title("Input Tarif")
    entry_tarif_window.geometry("300x200")

    if DataParkir:
        if 1 <= selected_index <= len(DataParkir):
            SelectKendaraan = DataParkir[selected_index - 1]
            PlatNomor = SelectKendaraan['Plat Nomor']
            JenisKendaraan = SelectKendaraan['Jenis Kendaraan']
            TipeKendaraan = SelectKendaraan['Tipe Kendaraan']
            tarif_per_jam_label = tk.Label(entry_tarif_window, text="Tarif Per Jam")
            tarif_per_jam_label.pack()
            tarif_per_jam_entry = tk.Entry(entry_tarif_window)
            tarif_per_jam_entry.pack()

            button_start = tk.Button(entry_tarif_window, text="Hitung Tarif", command=lambda: hitungTarif(PlatNomor, JenisKendaraan, TipeKendaraan, tarif_per_jam_entry.get(), SelectKendaraan['Waktu Masuk'], entry_tarif_window))
            button_start.pack()
        else:
            messagebox.showinfo("Input Tarif", "Nomor parkir tidak valid.")
    else:
        messagebox.showinfo("Input Tarif", "Plat Nomor Tidak Tersedia.")

def hitungTarif(plat_nomor, jenis_kendaraan, tipe_kendaraan, tarif_per_jam, waktu_masuk, entry_tarif_window):
    try:
        TarifPerJam = int(tarif_per_jam)
        WaktuKeluar = datetime.datetime.now()
        TotalWaktu = (WaktuKeluar - waktu_masuk).total_seconds() / 3600
        TotalTarif = TarifPerJam * TotalWaktu
        messagebox.showinfo("Nota", f"Plat Nomor          : {plat_nomor}\nJenis Kendaraan     : {jenis_kendaraan}\nTipe Kendaraan      : {tipe_kendaraan}\nTarif Per Jam       : {TarifPerJam}\nJam Masuk           : {waktu_masuk}\nJam Keluar          : {WaktuKeluar}\nTotal tarif         : Rp.{TotalTarif}")
        entry_tarif_window.destroy()
    except ValueError:
        messagebox.showinfo("Input Tarif", "Tarif per jam tidak valid.")

def entry_pilih_hapus():
    pilih_window = tk.Toplevel(root)
    pilih_window.title("Pilih kendaraan")
    pilih_window.geometry("300x200")

    pilih_label = tk.Label(pilih_window, text="Pilih")
    pilih_label.pack()

    # Use StringVar to store the entry value
    pilih_var = tk.StringVar()
    pilih_entry = tk.Entry(pilih_window, textvariable=pilih_var)
    pilih_entry.pack()

    button_start = tk.Button(pilih_window, text="Pilih Kendaraan", command=lambda: pilih_window.destroy())
    button_start.pack()

    pilih_window.wait_window()
    return pilih_var.get()


def hapusParkir():
    if DataParkir:
        try:
            pilih = int(entry_pilih_hapus())
            if 1 <= pilih <= len(DataParkir):
                del DataParkir[pilih - 1]
                messagebox.showinfo("Hapus Parkir", "Parkir berhasil dihapus.")
            else:
                messagebox.showinfo("Hapus Parkir", "Nomor parkir tidak valid.")
        except ValueError:
            messagebox.showinfo("Hapus Parkir", "Masukkan nomor parkir yang valid.")
    else:
        messagebox.showinfo("Hapus Parkir", "Plat Nomor Tidak Tersedia.")


label_title = tk.Label(root, text="Program Parkir")
label_title.pack()

button_start = tk.Button(root, text="Mulai", command=show_menu)
button_start.pack()

root.mainloop()

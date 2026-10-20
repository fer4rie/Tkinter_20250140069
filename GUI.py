import tkinter as tk
from tkinter import ttk

def label_luar(): #label luar untuk display hasil
    label_luar = tk.Toplevel(root)
    label_luar.title("Luaran Hasil")
    label_luar.geometry("350x120")
    label_luar.configure(bg="#1a2035") 


    # label hasil untuk display hasil prediksi prodi
    label_hasil = tk.Label(
        label_luar, 
        text="Prediksi Prodi : Teknologi Informasi", 
        font=("Arial", 12, "bold"), 
        bg="#1a2035", 
        fg="#00e5ff" # Warna cyan terang
    )
    label_hasil.pack(expand=True)

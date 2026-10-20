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

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("480x620")
root.configure(bg="#1a2035") 

# desain font & tampilannya
font_judul = ("Arial", 14, "bold")
font_label = ("Arial", 10)
bg_color = "#1a2035"
fg_color = "white"

# label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=font_judul, bg=bg_color, fg=fg_color)
label_judul.pack(pady=20)
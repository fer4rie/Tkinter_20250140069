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

# Frame input
frame_input = tk.Frame(root, bg=bg_color)
frame_input.pack()

# input nilai 
entries = []
for i in range(1, 11):
    # Teks label
    lbl_matpel = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i} :", font=font_label, bg=bg_color, fg=fg_color)
    lbl_matpel.grid(row=i, column=0, sticky="e", padx=10, pady=6)
    
    # Kotak input
    ent_matpel = tk.Entry(frame_input, width=25)
    ent_matpel.grid(row=i, column=1, padx=10, pady=6)
    entries.append(ent_matpel)

# Tambahan pilihan jurusan 
lbl_jurusan = tk.Label(frame_input, text="Pilihan Jurusan Anda:", font=font_label, bg=bg_color, fg=fg_color)
lbl_jurusan.grid(row=11, column=0, sticky="e", padx=10, pady=(15, 5))

combo_jurusan = ttk.Combobox(frame_input, values=["Teknologi Informasi"], width=22)
combo_jurusan.set("Teknologi Informasi")
combo_jurusan.grid(row=11, column=1, padx=10, pady=(15, 5), sticky="w")

# button 
btn_prediksi = tk.Button(root, text="Hasil Prediksi", font=("Arial", 10, "bold"), width=15, command=label_luar)
btn_prediksi.pack(pady=30)

root.mainloop() 

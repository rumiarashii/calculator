import tkinter as tk

jendela = tk.Tk()

jendela.title("Kalkulator Rumi!")
jendela.geometry("400x400")

angka = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]

symbol = ["+", "-", "x", "/"]

layar = tk.Entry(
    jendela,
    width=15, 
    font=("Arial", 24),
    justify="right",
    borderwidth=2,
    relief="solid"
)
layar.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

def tombol_ditekan(item):
    layar.insert("end", str(item))

def del_ditekan():
    print(f"isi layar: '{layar.get()}'")
    print(f"panjang: '{len(layar.get())}'")
    layar.delete(len(layar.get())-1, "end")

def clear():
    layar.delete(0, "end")
    tombol_del.config(text="Del", command=del_ditekan)

def hitung():
    isi = layar.get().replace("x", "*")
    hasil = eval(isi)
    layar.delete(0, "end")

    layar.insert("end", str(hasil))

    tombol_del.config(text="AC", command=clear)



tombol_result = tk.Button(
    jendela, 
        text="=",
        width=5,
        height=2,
        font=("Arial", 18),

        command=hitung
)
tombol_result.grid(row=4, column=2)

tombol_del = tk.Button(
    jendela, 
        text="Del",
        width=5,
        height=2,
        font=("Arial", 18),

        command = del_ditekan
)
tombol_del.grid(row=4, column=1)

for index, item in enumerate(symbol):
    tombol_symbol = tk.Button(
        jendela, 
        text=item,
        width=5,
        height=2,
        font=("Arial", 18),

        command=lambda i=item:tombol_ditekan(i)
    )
    tombol_symbol.grid(row=(index+1), column=3)


for index, item in enumerate(angka):
    tombol = tk.Button(
        jendela, 
        text=item,
        width=5,
        height=2,
        font=("Arial", 18),
        
        command=lambda i=item:tombol_ditekan(i)
    )
    tombol.grid(row=(index//3)+1, column=index%3) 






jendela.mainloop()





def tambah (a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi (a,b):
    if (b == 0):
        print("Tidak bisa dibagi 0")
    return a / b

def main():
    print("Calculator Simple Good And Reliable")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("0. Keluar")

    pilihan = int(input("\nPilih operasi (0-4): "))

    if pilihan == 0:
        print("Sampai Jumpa")
        return
    
    angka1 = float(input("\n Masukkan Angka 1: "))
    angka2 = float(input("\n Masukkan Angka 2: "))

    if pilihan == 1:
        print(f"Hasil: {tambah(angka1, angka2)}")
    elif pilihan == 2:
        print(f"Hasil: {kurang(angka1, angka2)}")
    elif pilihan == 3:
        print(f"Hasil: {kali(angka1, angka2)}")
    elif pilihan == 4:
        print(f"Hasil: {bagi(angka1, angka2)}")
    else:
        print("Pilihan Tidak Valid")


main()

   


    
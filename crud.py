
data_pengguna = []

def menu():
    while True:
        print("Menu")
        print("1. daftar")
        print("2. lihat data yang sudah masuk")
        menu = input("masukkan pilihan: ")

        if(menu == "1"):
            create()
        elif menu == "2":
            read()

def create():
    print("Menu daftar akun")
    while True:
        email = input("Masukkan email: ")

        if "@gmail.com" not in email:
            print("harus mengandung @gmail.com")
        else:
            password = input("Masukkan password: ")
            print("data berhasil di simpan")
            break

    di_simpan = {"email": email, "pass": password}
    data_pengguna.append(di_simpan)

def read():
    print("\ndata yang sudah terdftar\n")
    for i,data in enumerate(data_pengguna, start=1):
        print(f"{i}. Email: {data['email']}, Password: {data['pass']}")
        


def update():
    print("Menu update data")





menu()

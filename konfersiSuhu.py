def konversi_suhu():
    print("=== Program Konversi Suhu ===")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Kelvin")

    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == '1':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif pilihan == '2': #elif untuk menambahkan lebih byk kondisi itu singkatan dari else if
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    elif pilihan == '3':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin}K")
    else:
        print("Pilihan tidak valid!")

konversi_suhu()

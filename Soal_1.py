while True:
	print("----------------------------------")
	print("Masukkan '1' untuk penjumlahan")
	print("Masukkan '2' untuk pengurangan")
	print("Masukkan '3' untuk perkalian")
	print("Masukkan '4' untuk pembagian")
	print("Masukkan '0' untuk *keluar*")
	user_input = int(input("pilihan: "))
	if user_input == 0:
		break
	elif user_input == 1:
		angka1 = float(input("angka-1 : "))
		angka2 = float(input("angka-2 : "))
		hasil = angka1 + angka2
		print(">>> Hasil = {}".format(hasil))
	elif user_input == 2:
		angka1 = float(input("angka-1 : "))
		angka2 = float(input("angka-2 : "))
		hasil = angka1 - angka2
		print(">>> Hasil = {}".format(hasil))
	elif user_input == 3:
		angka1 = float(input("angka-1 : "))
		angka2 = float(input("angka-2 : "))
		hasil = angka1 * angka2
		print(">>> Hasil = {}".format(hasil))
	elif user_input == 4:
		angka1 = float(input("angka-1 : "))
		angka2 = float(input("angka-2 : "))
		hasil = angka1 / angka2
		print(">>> Hasil = {}".format(hasil))
	else:
		print(">>> Angka yang anda masukkan salah!")
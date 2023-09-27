'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
Input_Harga = 370000
Input_Diskon = 15/100
Harga = Input_Diskon * Input_Harga
Harga_akhir = Input_Harga - Harga
print("Harga yang harus dibayar adalah Rp.", "{:,}".format(round(Harga_akhir)))
# print("{:,}".format(round(Harga_akhir)))
def manualSort(n): 
    if n.isnumeric() and int(n) <= 359999: # mengecek inputan user apakah sesuai dengan condition atau tidak
        a = [] #menampung list angka
        for i in range(int(jumlah)): #looping untuk menginputan angka inputan user
            b = int(input('Angka ke - :'))
            a.append(b)
        return a.sort() #sorting
    else: # mengecek inputan user apakah sesuai dengan condition atau tidak
        print("Invalid Input!") #jika condition tidak sesuai
        return False

#membuat inputan jumlah angka yang akan diambil
jumlah = input('Masukkan jumlah angka: ')
manualSort(jumlah)









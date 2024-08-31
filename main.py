import datetime

class RumahSakit:
    def __init__(self, name, add, numICU, numHCU, numICCU, numNICU, numPICU):
        self.name = name
        self.add = add
        self.numICU = numICU
        self.numHCU = numHCU
        self.numICCU = numICCU
        self.numNICU = numNICU
        self.numPICU = numPICU
        self.pasien = list()
        self.noicu = 0
        self.nohcu = 0
        self.nonicu = 0
        self.nopicu = 0
        self.noiccu = 0
        
    def getNo_id(self, room):
        if room == 1:
            self.noicu += 1
            return '001-' + '0' * (3 - len(str(self.noicu))) + str(self.noicu)
        elif room == 2:
            self.nohcu += 1
            return '002-' + '0' * (3 - len(str(self.nohcu))) + str(self.nohcu)
        elif room == 3:
            self.nonicu += 1
            return '003-' + '0' * (3 - len(str(self.nonicu))) + str(self.nonicu)
        elif room == 4:
            self.nopicu += 1
            return '004-' + '0' * (3 - len(str(self.nopicu))) + str(self.nopicu)
        elif room == 5:
            self.noiccu += 1
            return '005-' + '0' * (3 - len(str(self.noiccu))) + str(self.noiccu)
    
    def appendPasien(self, pasien):
        self.pasien.append(pasien)
    
    def checkPasien(self, no_id):
        for p in self.pasien:
            if p.no_id == no_id:
                return p
        return False

    def getDataPasien(self, no_id):
        data = self.checkPasien(no_id)
        if data == False:
            return False
        else:
            print('Data Anda')
            print('Name :', data.name)
            print('Genre : ', data.genre)
            print('Age : ', data.age)
            print('No hp : ', data.nohp)
            print('Address : ', data.address)
            print('No Id : ', data.no_id)
            print('Tanggal Masuk : ', data.tgl_masuk)
            print('Tanggal Keluar : ', data.tgl_keluar)
            print('Penyakit yang diderita : ', data.penyakit)
    
    def getPosisiAntrian(self, no_id):
        for i in range(len(self.pasien)):
            if self.pasien[i].no_id == no_id:
                return i
        return False
    
    def ubahHarga(self, price, no_urut):
        self.pasien[no_urut].biayaObat(price)
            
class People:
    def __init__(self, name, genre, age, address, nohp):
        self.name = name
        self.genre = genre
        self.age = age
        self.address = address
        self.nohp = nohp
        
class Pasien(People):
    def __init__(self, name, genre, age, address, nohp, no_id, penyakit, tgl_masuk, tgl_keluar):
        super().__init__(name, genre, age, address, nohp)
        self.no_id = no_id
        self.penyakit = penyakit
        self.tgl_masuk = tgl_masuk
        self.tgl_keluar = tgl_keluar
        self.price = self.getPriceRoom()
    
    def biayaObat(self, biaya):
        self.price += int(biaya)
        
    def getPriceRoom(self):
        if self.tgl_masuk == self.tgl_keluar:
            return 0
        else:
            durasi = (self.tgl_keluar - self.tgl_masuk).days
            if self.no_id[:3] == '001':
                return durasi * 350000
            elif self.no_id[:3] == '002':
                return durasi * 400000
            elif self.no_id[:3] == '003':
                return durasi * 450000
            elif self.no_id[:3] == '004':
                return durasi * 500000
            elif self.no_id[:3] == '005':
                return durasi * 550000

class Apoteker:
    def __init__(self, harga=0):
        self.harga = (20, 25, 25, 25, 30, 30, 50, 50, 70, 70, 110, 110, 110, 110, 110, 110, 110, 120, 120, 140, 140, 140, 140, 140, 140, 14, 15, 170, 50, 40, 30, 20, 90, 90,
                    110, 110, 100, 110, 130, 130, 130, 140, 60, 60, 60, 60)

    def getObat(self):
        print("-------------------------------------------------------------------------")
        print("                      Apotek Hospotal")
        print("-------------------------------------------------------------------------")
        print("                      Menu Obat")
        print("-------------------------------------------------------------------------")
        print("----------------------------------    ")
        print("\n Obat Batuk/pilek/demam             26 minyak kayu putih 50ml...... 1400")
        print("----------------------------------    27 minyak kayu putih 100ml..... 1500")
        print(" 1 paracetamol............... 2000    28 minak kayu putih 120ml...... 17000")
        print(" 2 panadol biru.............. 2500")
        print(" 3 Panadol Flu Batuk......... 2500     Alkohol")
        print(" 4 inza...................... 2500     ----------------------------------")
        print(" 5 Oskadon................... 3000     29 Alkohol 100%............ 5000")
        print(" 6 mixagrip.................. 3000     30 Alkohol 70%............. 4000")
        print(" 7 napacin................... 5000     31 Alkohol 50%............. 3000")
        print(" 8 woods..................... 5000     32 Alkohol 30%............. 2000")
        print(" 9 OBH anak.................. 7000")
        print(" 10 OBH Batuk................ 7000          P3k")
        print("                                  ----------------------------------")
        print(" Obat salep                                 33 handsplast.......... 9000")
        print("----------------------------------------    34 betadin............. 9000")
        print(" 11 Balsem Lang 10 gr............ 11000    35 perban.............. 11000")
        print(" 12 Balsem Lang 20 gr............ 11000    36 benang jahit........ 11000")
        print(" 13 Balsem Geliga 10 gr.......... 11000")
        print(" 14 Balsem Geliga 20 gr.......... 11000    Obat Suntik")
        print(" 15 Balpirik merah............... 11000    ----------------------------------")
        print("                                           37 Xon-c............... 10000")
        print(" Minyak urut                               38 saridon............. 11000")
        print("----------------------------------         39 Masala Dosa......... 13000")
        print(" 16 fres Care........... 11000            40 Pulcracap........... 13000")
        print(" 17 safe care........... 11000            41 vitamin............. 13000")
        print(" 18 minyak kapak 10ml........... 12000    42 puyer 16............ 14000")
        print(" 19 minyak kapak 20ml........... 12000")
        print(" 20 minyak kapak 30ml........... 14000    obat tablet/kapsul")
        print(" 21 minyak tawon cc............. 14000    ----------------------------------")
        print(" 22 minyak tawon dd............. 14000    43 laxing.......... 6000")
        print(" 23 minyak tawon EE............. 14000    44 vitaminc........ 6000")
        print(" 24 Minyak Tekon 3 anak 60ml.... 14000    45 inzana.......... 6000")
        print(" 25 minyak telon 3 ankan 100ml.. 14000    46 hemaviton....... 6000")
        print("Press 0 -to end ")
        list_obat = list(map(int, input('List obat yang mau di beli (e.g 1 2 3 5) :').strip().split()))
        price = 0
        for i in list_obat:
            price += self.harga[i - 1]
        return price * 100
    
def Insert():
    while True:
        name = input("Name: ")
        genre = input('Genre (male/female) : ')
        age = int(input('Age (e.g 18) : '))
        nphone = input("Phone No.: ")
        add = input("Address: ")
        penyakit = input("Penyakit yang diderita :")
        
        if name != "" and nphone != "" and add != "" and penyakit != "":
            break
        else:
            print("\tName, Phone no, Address, & Penyakit cannot be empty..!!")
        
    check = input('Do you want to get a room (y/n)?')
    if check == 'y':
        cin = list(map(int, (input("Waktu masuk(dd/mm/yy): ").strip().split('/'))))
        cout = list(map(int, (input("Waktu keluar(dd/mm/yy): ").strip().split('/'))))
        timeStart = datetime.datetime(cin[2], cin[1], cin[0])
        timeOut = datetime.datetime(cout[2], cout[1], cout[0])
        while True:
            print("----SELECT ROOM TO PATIENT----")
            print(" 1. Intensive Care Unit (ICU)")
            print(" 2. High Care Unit (HCU)")
            print(" 3. Intensive Coronary Care Unit (ICCU)")
            print(" 4. Neonatal Intensive Care Unit (NICU)")
            print(" 5. Pediatric Intensive Care Unit (PICU)")
            ch = int(input("->"))
            if ch in range(1, 6):
                room = ch
                room_dict = {
                    1: ('Intensive Care Unit (ICU)', 350000),
                    2: ('High Care Unit (HCU)', 400000),
                    3: ('Intensive Coronary Care Unit (ICCU)', 450000),
                    4: ('Neonatal Intensive Care Unit (NICU)', 500000),
                    5: ('Pediatric Intensive Care Unit (PICU)', 500000),
                }
                print(room_dict[room][0])
                print("Price per day - Rp.", room_dict[room][1])
                break
            else:
                print('Please enter the right choice')
        
        no_id = BaligeHospital.getNo_id(room)
        pasien = Pasien(name, genre, age, add, nphone, no_id, penyakit, timeStart, timeOut)
        BaligeHospital.appendPasien(pasien)
        print('Terima kasih anda telah terdaftar sebagai pasien')
        print('No pasien anda : ', pasien.no_id)
    else:
        time = datetime.datetime.now()
        pasien = Pasien(name, genre, age, add, nphone, None, penyakit, time, time)
        BaligeHospital.appendPasien(pasien)
        print('Terima kasih anda telah terdaftar sebagai pasien')
        print('No pasien anda : ', pasien.no_id)

def Rooms_Info():
    print("      ------  ROOMS INFO Hospital ------")
    print("")
    print("Intensive Care Unit (ICU)")
    print("---------------------------------------------------------------")
    print("ICU adalah ruangan khusus bagi pasien kritis yang perlu perawatan intensif dan pengawasan terus menerus\n")
  
    print("High Care Unit (HCU)")
    print("---------------------------------------------------------------")
    print("HCU adalah pelayanan yang dikendalikan ke ruangan rawat inap. Ruangan ini diperuntukkan kepada pasien yang sudah kondisi membaik namun masih perlu pengawasan ketat oleh tenaga medis\n")

    print("Intensive Coronary Care Unit (ICCU)")
    print("---------------------------------------------------------------")
    print("Ruangan ini cocok untuk penderita penyakit jantung.\n")
    
    print("Neonatal Intensive Care Unit (NICU)")
    print("---------------------------------------------------------------")
    print("Ruangan ini cocok untuk pelayanan bersalin/melahirkan.\n")

    print("Pediatric Intensive Care Unit (PICU)")
    print("---------------------------------------------------------------")
    print("Ruangan ini diperuntukkan bagi bayi dan anak hingga 18 tahun.\n")
    
    n = int(input("0-BACK\n ->"))
    if n == 0:
        return

def Payment(no_id):
    data = BaligeHospital.getDataPasien(no_id)
    if data == False:
        print('Mohon maaf anda belum melakukan proses pendaftaran, Silahkan lakukan pendaftaran pada menu Insert')
    else:
        print(" Payment")
        print(" --------------------------------")
        print(" MODE OF PAYMENT")
        print('1. ATM')
        print('2. Cash\n')
        pilih_pay = input('- >')
        if pilih_pay == '1':
            print('Anda memilih menggunakan ATM')
        elif pilih_pay == '2':
            print('Anda memilih menggunakan sistem Cash')
        no_urut = BaligeHospital.getPosisiAntrian(no_id)
        price = BaligeHospital.pasien[no_urut].price
        BaligeHospital.pasien[no_urut].price = 0
        print('Total biaya pengobatan anda sebesar Rp.', price)
        print('Silahkan lakukan proses pembayaran dan Terima kasih, Semoga lekas sembuh !!!\n\n\n')

def Record(no_id):
    data = BaligeHospital.getDataPasien(no_id)
    if data == False:
        print('Mohon maaf anda belum melakukan proses pendaftaran, Silahkan lakukan pendaftaran pada menu Insert')

def Home():
    while True:
        print("\t\t\t\t\t\t Data Rumah Sakit\n")
        print("\t\t\t 1 Insert\n")
        print("\t\t\t 2 Rooms Info\n")
        print("\t\t\t 3 Apotek\n")
        print("\t\t\t 4 Payment\n")
        print("\t\t\t 5 Record\n")
        print("\t\t\t 0 Exit\n")

        ch = int(input("->"))
        if ch == 1:
            print(" ")
            Insert()
    
        elif ch == 2:
            print(" ")
            Rooms_Info()
    
        elif ch == 3:
            print(" ")
            price = ApotekBalige.getObat()
            no_id = input('Silakan masukkan no_id anda :')
            data = BaligeHospital.checkPasien(no_id)
            if data == False:
                print('Maaf anda belum mendaftarkan diri silahkan pergi ke menu insert untuk melakukan pendaftaran')
            else:
                BaligeHospital.getDataPasien(no_id)
                no_urut = BaligeHospital.getPosisiAntrian(no_id)
                BaligeHospital.ubahHarga(price, no_urut)
                print('Harga obat yang harus anda bayar : Rp.', price)
                print('Thanks untuk pembelian nya semoga lekas sembuh, Silahkan melakukan pembayaran pada menu payment')
        elif ch == 4:
            print(" ")
            no_id = input('Silahkan masukkan no_id anda : ')
            Payment(no_id)
        elif ch == 5:
            print(" ")
            no_id = input('Silahkan masukkan no_id anda : ')
            Record(no_id)
        elif ch == 0:
            print('Thank you, Get well soon')
            break
        else:
            print('Sorry, please enter the right number !!!')
    
BaligeHospital = RumahSakit('Rumah Sakit Balige', 'Balige Tobasa', 50, 50, 50, 50, 50)
ApotekBalige = Apoteker()
Home()

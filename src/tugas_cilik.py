#Tugas Kecil I Strategi Algoritma
#Ryandito Diandaru
#13519157

#modul untuk menghitung waktu runtime
from datetime import datetime

#opening files dan membaca
namafile = input("Masukkan nama file: ")
filenya = open("../test/"+namafile,"r")
riddle = filenya.readlines()

#start timer
start=datetime.now()

#inisialisasi
letters = []
idxFirstLet = []
subt = False
wesmari = False
cyc = 0

#inisialisasi lookup table huruf
for kata in (riddle):
    for huruf in(kata):
        if (huruf != '-' and huruf != '+' and huruf != '\n'):
            if [huruf,0] not in letters:
                letters.append([huruf,0])

#inisialisasi huruf depan
for kata in (riddle):
    slese = False
    zz = 0
    while(not(slese) and zz < len(letters)):
        if(kata[0] == letters[zz][0] and zz not in idxFirstLet):
            idxFirstLet.append(zz)
            slese = True
        zz += 1

#fungsi isArrayUnique, memastikan huruf yang diassign dengan angka yang sama
def isStringArrayUnique(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if (x[i] == x[j]):
                return False
    return True

#fungsi isValid untuk mengecek apakah sudah valid, angka unik dan depan tidak 0
def isValid(x, hurufPert):
    for i in hurufPert:
        if(x[i] == '0'):
            return False
    if(isStringArrayUnique(x)):
        return True
    else:
        return False

#fungsi validate, untuk menjadikan huruf awal bukan 0
def validate(x, hurufPert):
    cek = False
    for i in(hurufPert):
        if(x[i] == '0'):
            cek = True
    if(cek):
        done = False
        i = 0
        while(i < len(x) and not(done)):
            if(x[i] == '0' and (i in hurufPert)):
                x = list(x)
                x[i] = '1'
                for j in range(i+1,len(x)):
                    x[j] = '0'
                x = "".join(x)
                done = True
            i += 1
    return x

#fungsi incrementString, menambahkan sebuah integer yang bertipe string
def incrementString(x):
    if(x[0] == '0'):
        leninit = len(x)
        x = str(int(x) + 1)
        if(len(x) != leninit):
            x = '0' + x
    else:
        x = str(int(x) + 1)
    return x

#fungsi nextPermute, untuk menunjukkan kombinasi berikutnya
def nextPermute(x):
    if(not(isStringArrayUnique(x))):
        i = 0
        reset = False
        while(i < len(x)):
            travelIdx = i + 1
            while(travelIdx < len(x)):
                if(x[travelIdx] == x[i]):
                    x = list(x)
                    if(x[travelIdx] != '9'):
                        x[travelIdx] = incrementString(x[travelIdx])
                        for j in range(travelIdx+1,len(x)):
                            x[j] = '0'
                        x = "".join(x)
                        reset = True
                    else:
                        while(x[travelIdx-1] == '9' and travelIdx>0):
                            x[travelIdx] = '0'
                            travelIdx -= 1
                        x[travelIdx] = '0'
                        x[travelIdx-1] = incrementString(x[travelIdx-1])
                        x = "".join(x)
                        reset = True
                travelIdx += 1
                if(reset):
                    travelIdx = len(x)
            i += 1
            if(reset):
                i = 0
                reset = False
    return x        

#tentukan batas bawah
bawah = ''
for i in range(len(letters)):
    bawah = bawah + str(i)

#tentukan batas atas
atas = ''
for i in range(len(letters)):
    atas = atas + str(9-i)

#brute force :,)
lookupDict = {}
print("Solusi yang mungkin adalah: ")
while (int(bawah) <= int(atas) and not(wesmari)):
    if(isValid(bawah, idxFirstLet)):
        total = 0
        subt = False
        lookupDict['+'] = ''
        lookupDict['\n'] = ''
        for i in range(len(bawah)):
            letters[i][1] = bawah[i]
        for n in letters:
            lookupDict[n[0]] = n[1]
        for word in riddle:
            for hurf, angk in lookupDict.items():
                word = word.replace(hurf,angk)
            if (word[0] != '-'):
                if(subt == False):
                    total = total + int(word)
                else:
                    total = total - int(word)
            else:
                subt = True
        if(total == 0):
            del lookupDict['+']
            del lookupDict['\n']
            for word in (riddle):
                for hurf, angk in lookupDict.items():
                    word = word.replace(hurf,angk)
                print(word, end='')
            print('\n')
            wesmari = True
        bawah = incrementString(bawah)
    else:
        bawah = validate(bawah, idxFirstLet)
        bawah = nextPermute(bawah)
    cyc += 1

#stop timer dan print waktu dan percobaan
print("Time taken:", datetime.now()-start)
print('Number of trials: ', cyc, ' kali')

#menutup file
filenya.close()
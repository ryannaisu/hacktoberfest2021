## AUTHOR: Andy-Ra
## GITHUB: https://github.com/Andy-Ra/
## Python Concept : Binner To Decimal Convertation

import re

print ("+++ Binner to Decimal Convertation +++")

ulang = 'Y'
while ulang == 'Y' or ulang == 'y':
  binner = int(input("Please Input your Binner: "))
  pangkat = len(str(binner)) - 1
  angka_bin = []
  decimal = 0
  for a in range (0, len(str(binner))):
    angka_bin.append(int(str(binner)[a]))
    satu = (angka_bin[a] * pow(2,pangkat))
    pangkat = pangkat - 1
    decimal = satu + decimal

  if (re.search("[2-9]", str(binner))):
    print ("Please input number 1 or 0")
    ulang == 'Y'

  else:
    print (decimal)
    
  
  ulang = input("Try Again? [Y/N] ")
  if ulang == 'N':
    print ("")
    print ("++++++ THANKYOU ++++++")  
    print ("+++++++++++++++++++++++++")
  
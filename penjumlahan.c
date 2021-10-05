#include <iostream.h>
#include <stdio.h>
#include <conio.h>

main(){
//deklarasi tipe data.
      int hasil, a =12, b=13;
//rumus penjumlahan.
      hasil = a + b;
//output dengan C.
      printf("Hasil penjumlahan dari 12 + 13 adalah %d",hasil);
//output dengan C++.
      cout<<hasil;
getch();
}

contoh diatas adalah bentuk dengan penjumlahan yang tidak dinamis (tanpa input sesuai kebutuhan).

Perbedaan dengan yang statis hanyalah pada inputnya, keunggulannya jika  ingin menjumlahkan untuk nilai yang berbeda cukup membuat satu program saja. berikut contoh programnya :

#include <iostream.h>
#include <stdio.h>
#include <conio.h>


main(){
//deklarasi tipe data.
      int a, b, hasil;
//input dengan bahasa C.
      printf("masukkan nilai a = ");
      scanf("%d",&a);

      printf("masukkan nilai b = ");
      scanf("%d",&b);
//input dengan bahasa C++.
      cout<<"masukkan nilai a = ";cin>>a;

      cout<<"masukkan nilai b = ";cin>>b;



//rumus penjumlahan.
      hasil = a+b;
//output dengan bahasa C.
      printf("Hasil penjumlahan a + b = %d", hasil);
//output dengan bahasa C++.
      cout<<"Hasil penjumlahan a + b = "<<hasil;
getch();
}

    @	   	   ��	  P � � �	 S M I   C o r p o r a t i o n                               U S B   D I S K                                                                                                                           
    @ 	   ��	  P �@ �@ � �smiSMI     USB DISK        1100                  <�	  ��?�   �  (_   0P      �  f!!� H  �O0905   O0905   	    0   3259AA_O0908_6TD     a=a+1
#         print(y, "za ", koszyk[a], "zł")
#
#     elif opcje=="K":
#         suma = 0
#         for x in koszyk:
#             suma=suma+x
#
#         print("Cena: ", suma, "zł")
#         break






produkty = {"chleb": 5, "woda":2.20, "masło":5.29, "jogurt":6, "mleko":4.40}
koszyk={}

while True:
    menu = input("Dodaj do koszyka - D, Podgląd koszyka - P, Kasa - K: ")

    if menu.upper() == "D":
        user = input("Dodaj produkt: ")
        if user in produkty:
            if user in koszyk:
                koszyk[user] +=1
            else:
                koszyk[user]=1
        else:
            print("Tego produktu nie ma w sklepie.")


    elif menu.upper() == "P":
        for key, value in koszyk.items():
            print(f" Produkt: {key}, ilość: {value}")

    elif opcje == "K":
        suma = 0
        for produkt, ilosc in koszyk.items():
            suma += ilosc*produkty[produkt]

        print(f"Suma twojego koszyka: {suma}")
        break
import listeler

liste=[]

liste=[ x for x in range(10) if x % 3==0]
# print(liste)   

liste2=[x for x in listeler.muhtelif if x.isalpha()]
# print(liste2)


liste3=[(listeler.ogrenciler[x],listeler.notlar[x]) for x in range (0,len(listeler.ogrenciler))]

liste_dic={key:value for (key,value) in liste3}

print(liste_dic)





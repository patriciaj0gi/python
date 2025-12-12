#Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha,
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, 
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, 
# siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)

name = input("Mis sinu nimi on? ")
print("Tere,", name + "!")

location = input("Kus sa elad? ")
print(location)

if "saaremaa" in location.lower():
    print("Saarlane")

age = int(input("Kui vana sa oled? "))
if age < 18:
    print("Sa oled liiga noor, et autot juhtida. ")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul! ")
else:
    print("Sa võid autot juhtida. ")
    
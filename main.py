import random
#Úkol číslo 1
print("\033[4mÚkol 1\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
# Vytvoření pole s čísly od 0 do 100
numbers = list(range(101))

# Přeházení čísel
random.shuffle(numbers)

# Výběr prvních 9 čísel
random_numbers = numbers[:9]

print(random_numbers)


#Úkol číslo 2
print("\033[4mÚkol 2\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí,4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
# Výpis prvního, prostředního a posledního čísla
Prvni_hodnota = random_numbers[0]  # První hodnota
Prostredni_hodnota = random_numbers[4]  # Prostřední hodnota (index 4 pro 9 čísel)
Posledni_hodnota = random_numbers[8]    # Poslední hodnota

print("První hodnota:", Prvni_hodnota)
print("Prostřední hodnota:", Prostredni_hodnota)
print("Poslední hodnota:", Posledni_hodnota)

#Úkol číslo 3
print("\033[4mÚkol 3\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
#Změna hodnoty na indexu 5 na 34
random_numbers[5] = 34
#Výpis nového pole
print("Nové pole:", random_numbers)

#Úkol číslo 4
print("\033[4mÚkol 4\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
#Vypiště indexove 7 hodnotu z pole
seventh_value = random_numbers[7]
#Vypisuje 7 hodnotu z pole
print("Hodnota na 7 indexovém místě:", seventh_value)

#Úkol číslo 5
print("\033[4mÚkol 5\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
length_of_array = len(random_numbers)
print("Délka pole:", length_of_array)

#Úkol číslo 6
print("\033[4mÚkol 6\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
#Výpis minimální a maximální hodnoty z pole
min_value = min(random_numbers)
max_value = max(random_numbers)
print("Minimální hodnota", min_value)
print("Maximální hodnota", max_value)

#Úkol číslo 7
print("\033[4mÚkol 7\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
#Druhé pole
pole2 = [1, 2, 3, 4, 5]
#Druhé pole s libovolnými čísly a náhodnou délkou
delka = random.randint(5, 15)  # náhodná délka mezi 5 a 15
pole2 = [random.randint(-100, 100) for _ in range(delka)]
print("Druhé pole:", pole2)

#Úkol číslo 8
print("\033[4mÚkol 8\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
soucet = sum(pole2) #secteme vsechny hodnoty v poli
print("Součet čísel je:", soucet)

#Úkol číslo 9
print("\033[4mÚkol 9\033[0m")  #Pomohl jsem si pomocí AI jak podtrhnout text, nevěděl jsem tak jsem si pomohl, snad to nevadí, 4m = povoluje podtržený text, 0m = resetuje formatovani predchoziho textu, ktere jsme pouzili pred timhle kodem
# Sečteme první a pátou hodnotu (pokud pole má alespoň 5 prvků)
if len(pole2) >= 5:
    soucet = pole2[0] + pole2[4]
    print("Pole:", pole2)
    print("Součet první a páté hodnoty je:", soucet)
else:          
    print("Pole má méně než 5 prvků, nelze sečíst první a pátou hodnotu.") #Pokud to má méně než 5 polí, vypíše to tenhle kód
import random

numberofdrops = 0
drops = []
summa = 0
count = 0

"""
1. feladat
"""
print("1. feladat")
numberofdrops = int(input("Ird be a dobások számát!\t"))

"""
2. feladat
"""
print("2. feladat")
for index in range(numberofdrops):
    drops.append(random.randint(1,6))
print("A dobások: "+ str(drops))

"""
3. feladat
"""
print("3. feladat")
for index in drops:
    summa = summa + index
print(f"A játékos átlagosan {round(summa/len(drops), 2)} mezőt lépett, összesen {summa} mezőt lépett.")

"""
4. feladat
"""
print("4. feladat")
for index in drops:
    if index == 6: count += 1
if count > 0: print(f"A játékos {count} alkalommal dobott hatost.")
else: print("A játékos sajnos egy alkalommal sem dobott hatost")

"""
5. feladat
"""
print("5. feladat")
count = 0 # Mivel újra felhasználásra kerül ezért le kell nullázni.
for index in drops:
    if (index % 2) == 0 : count += 1
print(f"A játékos {count} alkalommal dobott páros számot.")

"""
6. feladat
Az index ezuttal az elem listában elfoglat helyét jelöli, ezért ki kell törölni a korábbi tartalmát!
"""
print("6. feladat")
index = 0
count = 0 # Mivel újra felhasználásra kerül ezért le kell nullázni.
for number in drops:
    if index != 0:
        if drops[index-1] > number: count += 1
    index += 1
print(f"A játékos {count} alkalommal dobott kevesebbet, mint előző körben.")
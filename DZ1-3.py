sek = int(input("Введите время в секундах "))
min = (sek // 60) % 60
hh = (sek // 3600) % 60
sek1 = sek % 60
print("Время %d:%d:%d" % (hh, min, sek1))
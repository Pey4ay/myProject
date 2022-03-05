import random
from random import randint

ig = int(input())                                               #Количество игроков
pol = ["М","Ж"]
plodov = ["Плодовитый","Плодовитый","Плодовитый","Бесплодный","Плодовитый","Плодовитый","Плодовитый","Бесплодный"]



with open(r'D:/python/game/data/prof.txt', 'r',encoding="utf-8") as f1:               #|Создание переменной, куда вписываю проффесии
    prof = f1.read().splitlines()                                #|

p = list(range(0,len(prof)))                                    #переменная для рандома проффесий
random.shuffle(p)
#____________________________________________________
with open(r'D:/python/game/data/zdorov.txt', 'r',encoding="utf-8") as f2:             #|Создание переменной, куда вписываю здоровье
    zdor = f2.read().splitlines()                                #|

z = list(range(0,len(zdor)))                                     #переменная для рандома здоровья
random.shuffle(z)
tyazh = ["Лёгкая","Средняя","Последняя"]
#____________________________________________________
with open(r'D:/python/game/data/bagazh.txt', 'r',encoding="utf-8") as f3:             #|Создание переменной, куда вписываю багаж
    bag = f3.read().splitlines()                                 #|

b = list(range(0,len(bag)))                                      #переменная для рандома багажа
random.shuffle(b)
#____________________________________________________
with open(r'D:/python/game/data/cherta.txt', 'r',encoding="utf-8") as f4:             #|Создание переменной, куда вписываю черту характера
    cherta = f4.read().splitlines()                              #|

ch = list(range(0,len(cherta)))                                  #переменная для рандома черты характера
random.shuffle(ch)
#____________________________________________________
with open(r'D:/python/game/data/hobbi.txt', 'r',encoding="utf-8") as f5:             #|Создание переменной, куда вписываю хобби
    hobbi = f5.read().splitlines()                              #|

hob = list(range(0,len(hobbi)))                                 #переменная для рандома хобби
random.shuffle(hob)
#____________________________________________________
with open(r'D:/python/game/data/fobiy.txt', 'r',encoding="utf-8") as f6:             #|Создание переменной, куда вписываю фобии
    fobiy = f6.read().splitlines()                              #|

fob = list(range(0,len(fobiy)))                                 #переменная для рандома фобий
random.shuffle(fob)
#____________________________________________________
with open(r'D:/python/game/data/dopi.txt', 'r',encoding="utf-8") as f7:             #|Создание переменной, куда вписываю допы
    dopi = f7.read().splitlines()                              #|

dop = list(range(0,len(dopi)))                                 #переменная для рандома допов
random.shuffle(dop)
#____________________________________________________
with open(r'D:/python/game/data/karti.txt', 'r',encoding="utf-8") as f8:             #|Создание переменной, куда вписываю карты
    karti = f8.read().splitlines()                              #|

kar = list(range(0,len(karti)))                                 #переменная для рандома карт
random.shuffle(kar)

kar2 = list(range(0,len(karti)))                                 #переменная для рандома карт2
random.shuffle(kar2)

#____________________________________________________



for i in range (0,ig):                                          #запись в файл
    with open(r"D:/python/game/Players/player"+str(i+1)+".txt", "w",encoding="utf-8") as file:
        file.write("Возраст:"+str(randint(18,60)))
        file.write("\nПол:"+str(random.choice(pol)))
        file.write("\nПлодовитость:"+str(random.choice(plodov)))
        file.write("\nПрофессия:"+prof[p[i]])
        file.write("\nЗдоровье:"+zdor[z[i]]+"("+random.choice(tyazh)+")")
        file.write("\nБагаж:"+bag[b[i]])
        file.write("\nЧерта характера:"+cherta[ch[i]])
        file.write("\nХобби:"+hobbi[hob[i]])
        file.write("\nФобии:"+fobiy[fob[i]])
        file.write("\nДоп.информация:"+dopi[dop[i]])
        file.write("\nКарта1:"+karti[kar[i]]+"\nКарта2:"+karti[kar2[i]])




with open(r'D:/python/game/data/katastrofa.txt', 'r',encoding="utf-8") as k:               #|Создание переменной, куда вписываю описание
    katas = k.read().splitlines()                                     #|

with open(r'D:/python/game/data/vbunkere.txt', 'r',encoding="utf-8") as k1:                #|Создание переменной, куда вписываю что в бункере
    vbunk = k1.read().splitlines()                                    #|

eda = ["В большом количестве","На каждого человека","В недостатке"]


with open(r"D:/python/game/Players/"+"Opisanie.txt", "w",encoding="utf-8") as file:
    file.write("Катастрофа:"+katas[(randint(0,len(katas)-1))])
    file.write("\nВ бункере есть:"+vbunk[(randint(0,len(vbunk)-1))])
    file.write("\nВ бункере есть:"+vbunk[(randint(0,len(vbunk)-1))])
    file.write("\nВ бункере есть:"+vbunk[(randint(0,len(vbunk)-1))])
    file.write("\nРазмер бункера:"+(str(randint(100,200))+"м2"))
    file.write("\nВремя проведенное в бункере:"+(str(randint(1,12))+"мес."))
    file.write("\nКоличество еды:"+str(random.choice(eda)))
    file.write("\nКоличество мест:"+str(ig//2))
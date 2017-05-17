__author__ = '5967009: Paul Daechert'
print("Form: ax^2 + bx = c")
a = input("a: ")                                    #Eigabe der Variablen
b = input("b: ")                                    #
c = input("c: ")                                    #

print("\nNullstellen der Funktion ",int(a),"x^2 +",int(b),"x =",int(c))
if int(a) != 0:                                     #fuer den fall, dass eine lineare funktion angegeben wird
    p = int(b) / int(a)                             #p der pq-Formel berechnen
    q = -1 * int(c) / int(a)                        #q der pq-Formel berechnen
    if ((p/2) ** 2 -  q )>= 0:                      #if-Abfrage, falls Funktion die x-Achse nicht schneidet -> keine Nulsltellen
        x1 = -1 * p / 2 + ((p/2) ** 2 -  q) ** 0.5  #mit pq-Formel erste Nullstelle berechnen
        x2 = -1 * p / 2 - ((p/2) ** 2 -  q) ** 0.5  #mit pq-Formel zweite Nullstelle berechnen

        if x1 != x2:                                #Nullstellen ausgeben
            print("x1= ",x1,"\tx2= ",x2)
        else:                                       #falls es nur eine Nullstelle gibt
            print("x= ",x1)
    else:
        print("Keine Nullstellen vorhanden!")
elif int(b) != 0:
    print("x= ",int(c) / int(b))
else:
    print("Keine Nullstellen vorhanden!")
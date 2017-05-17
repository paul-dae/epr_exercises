__author__ = '5967009: Paul Daechert'

isbnstr = input("ISBN-13: ")                        #Input-ISBN in einem String speichern

isbn1 = int(isbnstr[0])                             #ISBN in einzelnen Integer Variablen abspeichern
isbn2 = int(isbnstr[1])
isbn3 = int(isbnstr[2])
isbn4 = int(isbnstr[3])
isbn5 = int(isbnstr[4])
isbn6 = int(isbnstr[5])
isbn7 = int(isbnstr[6])
isbn8 = int(isbnstr[7])
isbn9 = int(isbnstr[8])
isbn10 = int(isbnstr[9])
isbn11 = int(isbnstr[10])
isbn12 = int(isbnstr[11])
isbn13p = (10 - (isbn1 + 3 * isbn2 + isbn3 + 3 * isbn4 + isbn5 + 3 * isbn6 + isbn7          #ISBN13 Pruefnummer
                 + 3 * isbn8 + isbn9 + 3 * isbn10 + isbn11 + 3 * isbn12) % 10) % 10         #berechnen

isbn10p = (isbn1 + 2 * isbn2 + 3 * isbn3 + 4 * isbn4 + 5 * isbn5 + 6 * isbn6 + 7 * isbn7    #ISBN10 Pruefnummer
           + 8 * isbn8 + 9 * isbn9 + 10 * isbn10 + 11 * isbn11 + 12 * isbn12) % 11          #berechnen

isbnstr10 = str(isbn4)                              #ISBN10 String zusammenfuegen
isbnstr10 += "-"
isbnstr10 += str(isbn5)
isbnstr10 += str(isbn6)
isbnstr10 += "-"
isbnstr10 += str(isbn7)
isbnstr10 += str(isbn8)
isbnstr10 += str(isbn9)
isbnstr10 += str(isbn10)
isbnstr10 += str(isbn11)
isbnstr10 += str(isbn12)
isbnstr10 += "-"

isbnstr13 = str(isbn1)                              #ISBN13 String zusammenfuegen
isbnstr13 += str(isbn2)
isbnstr13 += str(isbn3)
isbnstr13 += "-"
isbnstr13 += str(isbnstr10)

isbnstr10 += str(isbn10p)                           #Pruefnummer fuer die Strings anfuegen
isbnstr13 += str(isbn13p)

print(isbnstr13)                                    #Strings ausgeben
print(isbnstr10)

#Erkennbare Fehler: Falls 2 nebenstehende Ziffern vertauscht werden und diese Beiden nicht die Differenez 5 voneinander
#haben (Testfall 1), genau eine Ziffer ist falsch (Testfall 3)
#Unerkennbarer Fehler: Falls 2 nebenstehende Ziffern vertauscht werden und diese Beiden die Differenz 5 voneinander
#haben (Testfall 2), mehr als eine Ziffer ist falsch (Testfall 4)
#Testfaelle:
#1. Eingabe:    978312732230        (statt 978312732320)
#   Ausgabe:    978-3-12-732230-9   (statt 978-3-12-732230-7)
#               3-12-732230-0       (statt 3-12-732230-10)

#2. Eingabe:    978317232320		(statt 978312732320)
#   Ausgabe:    978-3-12-7232320-7
#               3-17-232320-5		(statt 3-12-732230-10)

#3. Eingabe:    978312732321        (statt 978312732320)
#   Ausgabe:    978-3-12-732321-4   (statt 978-3-12-732230-7)
#               3-12-732321-0       (statt 3-12-732230-10)

#4. Eingabe:    978312732317        (statt 978312732320)
#   Ausgabe:    978-3-12-732317-7   (statt 978-3-12-732230-7)
#               3-12-732317-6       (statt 3-12-732230-10)

#5. Eingabe:    385967485963
#   Ausgabe:    385-9-67-485963-9
#               9-67-485963-9

#6. Eingabe:    978564988372
#   Ausgabe:    978-5-64-988372-6
#               5-64-988372-0

#7. Eingabe:    3475867754633
#   Ausgabe:    347-5-86-775463-7
#               5-86-775463-2

#8. Eingabe:    3499857490999
#   Ausgabe:    349-9-85-749099-2
#               9-85-749099-7

#9. Eingabe:    4857688938671
#   Ausgabe:    485-7-68-893867-7
#               7-68-893867-9

#10. Eingabe:   939458904853
#   Ausgabe:    939-4-58-904853-1
#               4-58-904853-5

#11. Eingabe:   485777684592
#    Ausgabe:   485-7-77-684592-4
#               7-77-684592-4

#12. Eingabe:   903487609354
#    Ausgabe:   903-4-87-609354-6
#               4-87-609354-9
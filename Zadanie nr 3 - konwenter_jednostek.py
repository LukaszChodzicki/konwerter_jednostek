print("Witamy w programie - Konwerter jednostek")

celsjusz = int(input("Podaj temperaturę w stopniach celsjusza = "))

fahrenheit = (celsjusz * 1.8) + 32 
print(celsjusz, "stopni celsjusza to:", fahrenheit, "Fahrenheitów")
 
dzialanie = int(input("Wybierz co chcesz konwertować:\n 1 - metry na stopy \n 2 - stopy na metry \n"))

if (dzialanie == 1):
    metry = int(input("Podaj odległość w metrach = "))
    print()
    stopy = (metry * 3.28084)
    print(metry, "metrów to:", round(stopy,2), "stóp")

if (dzialanie == 2):
    stopy = int(input("Podaj odległość w stopach = "))
    print()
    metry = (stopy / 3.28084)
    print(stopy, "stóp to:", round(metry,2), "metrów")
 
 
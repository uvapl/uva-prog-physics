Tentamen vrijdag 1 februari
====================================

Regels
------

* Je mag geen Python-libraries `import`eren.


Verbeter de fout
----------------

In de onderstaande implementatie van de functie `x_tot_de_derde` zitten twee
fouten. Repareer de functie zodat we inderdaad de derde macht van een getal
kunnen berekenen.

	def x_tot_de_derde(x)
		y = x * x * x
		return

Zo zou het moeten werken:

	x = 2.0
    y = x_tot_de_derde(x)   
    print y                 <= 8.0

	x = 2.2
    y = x_tot_de_derde(x)   
    print y                 <= 10.648000000000003 (ongeveer)


Klein programma
---------------

Schrijf een functie `find_max(numbers)` die het maximum-getal vindt in een
lijst en die als *return value* teruggeeft.

Je programma zou als volgt moeten werken:

	lijst = [1,13,15,27,31,89,41,5,11]
	maximumgetal = find_max(lijst)
	print "het maximumgetal in de lijst = ", maximumgetal

Nota bene: bij deze test moet dus het getal 89 geprint worden.


Groter programma
----------------

Een "abundant number" is een geheel getal waarvan de som van de delers groter
is dan het getal zelf: 12 is een abundant getal omdat geldt 1 + 2 + 3 + 4 + 6
= 16 (en 16 > 12).

Schrijf een functie die alle abondante getallen onder de 100 uitrekent en
print. Dat zijn: 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72,
78, 80, 84, 88, 90, 96.

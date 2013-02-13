Tentamen woensdag 30 januari
====================================

Verbeter de fout
----------------

In de onderstaande implementatie van de functie x_kwadraat zitten twee fouten.
Repareer de functie zodat we inderdaad het kwadraat van een getal kunnen
berekenen.

	def x_kwadraat(x)
		y = x * x
		return

Zo zou het moeten werken:

	x = 2.0
	y = x_kwadraat(x)
	print y                 <= 4.0

	x = 2.2
	y = x_kwadraat(x)
	print y                 <= 4.84000000000001 (ongeveer)


Klein programma
---------------

Schrijf een functie `print_sequence(xmin, xmax, steps)` die met behulp van een
`for`-loop een rij getallen print van `xmin` tot `xmax` in `steps` steppen.

Dit zou dus moeten werken:

	print_sequence(1.0, 2.0, 10)
    
    step 0 = 1.0
    step 1 = 1.1
    step 2 = 1.2
    step 3 = 1.3
    step 4 = 1.4
    step 5 = 1.5
    step 6 = 1.6
    step 7 = 1.7
    step 8 = 1.8
    step 9 = 1.9
    step 10 = 2.0


Groter programma
----------------

Een perfect getal is een getal waarvan de som van de delers (met rest 0) het
getal zelf is. Een voorbeeld is 6 (1 + 2 + 3 = 6).

Schrijf een programma dat de andere perfecte getallen onder de 500 vindt en
uitprint. Dat zijn er maar twee, namelijk 28 en ...?

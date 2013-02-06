# Priemgetallen berekenen

##Exercise 1.0 - het duizendste priemgetal

Schrijf een programma `primes.py` dat het duizendste priemgetal berekent en op
het scherm print.

### Computing hint

* Eén manier om te testen of een getal $$a$$ een veelvoud is van een getal
  $$b$$ ($$b$$ deelt $$a$$ met rest $$0$$) is het gebruik van de `%`-operator.
  In Python geeft `a % b` de rest: `8 % 3` is `2`. Check zelf de werking in de
  Python shell.

* Vandaag gaan we ook een data type `list` gebruiken. Het is een 'rijtje',
  lees erover in de documentatie. Voorbeeldje.

Vul een list met 3 getallen en print deze:

       x = []          # declareer een lege lijst
       x.append(17)    # voeg het getal 17 toe
       x.append(2)     # voeg het getal 2 toe
       x.append(1367)  # voeg het getal 1367 toe
       print x         # vraag Python om de list te printen
       [17,2,1367]     # dit is de output


Toegang tot de informatie in de lijst is als volgt. Let op, het eerste object
in het rijtje staat op plek 0.

       a = x[0]
       print a
       17

### Strategie hints

Hoewel een computer je in staat stelt om snel te rekenen is het toch
belangrijk om voor elk probleem de optimale strategie te bepalen. Hier
bijvoorbeeld:

* Genereer eerst een lijst van oneven getallen (>1) als priemgetal-kandidaten.

* Verzin hoe je per priem-kandidaat bijhoudt of het wel/niet priem is als je
  over kandidaat delers heenloopt. Bedenk van tevoren hoe je de lijst met
  gevonden priemgetallen gaat opslaan.

* Wanneer kan je stoppen voor een individuele kandidaat ? Als je wilt bepalen
  of 37 een priemgetal, welke kandidaat delers bekijk je voordat je kan
  concluderen dat het een priemgetal is ?

* Print voor elke kandidaat informatie zodat je weet waar je bent in de
  berekening en je ziet of de computer ook echt jouw strategie volgt.

* Bedenkt goed hoe het programma uiteindelijk stopt bij het 1000ste
  priemgetal. Realiseer je hierbij dat je programma waarschijnlijk niet het
  eerste priemgetal heeft gegenereerd (2).

Als je wilt controleren of je programma goed werkt kan je je gevonden lijst
priemgetallen matchen met een 
[lijst bekende priemgetallen](http://primes.utm.edu/lists/small/1000.txt).

## Exercise 2.0 - eigenschappen priemreeksen

Welke getallen (onder $$n=10000$$) vormen de langste reeks aaneengesloten
niet-priemgetallen? Start met de code in `primes.py` en voeg dit toe als
output aan het eind van je programma

## Hacker edition ##

Maak bij het testen van een getal `n` gebruik van de kennis over de
priemgetallen onder de `n`. Bepaal hoeveel sneller dat is voor grote getallen.
En tot welk priemgetal kan je komen binnen 1 minuut?

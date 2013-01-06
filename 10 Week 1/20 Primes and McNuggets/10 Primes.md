
# Priemgetallen berekenen

Schrijf een programma dat het duizendste priemgetal berekent en op het scherm print.

### Computing hint:###

Eén manier om te testen of een getal $a$ een veelvoud is van een getal $b$ ($b$ deelt $a$ met rest $0$) is het gebruik van de `%`-operator. In Python geeft `a % b` de rest: `8 % 3` is `2`. Check zelf de werking in de Python shell.

### Strategie hints:###
Hoewel een computer je in staat stelt om snel te rekenen is het toch belangrijk om 
voor elk probleem de optimale strategie te bepalen. Hier bijvoorbeeld:

* Genereer eerst een lijst van oneven getallen (>1) als priemgetal-kandidaten
* Verzin hoe je per priem-kandidaat bijhoudt of het wel/niet priem is als je over kandidaat delers heenloopt. Bedenk van tevoren hoe je de lijst met gevonden priemgetallen gaat opslaan.
* Wanneer kan je stoppen voor een individuele kandidaat ? Als je wilt bepalen of 37 een priemgetal, welke kandidaat delers bekijk je voordat je kan concluderen dat het een priemgetal is ?
* Print voor elke kandidaat informatie zodat je weet waar je bent in de berekening en je ziet of de computer ook echt jouw strategie volgt.
* Bedenkt goed hoe het programma uiteindelijk stopt bij het 1000ste priemgetal. Realiseer je hierbij dat je programma waarschijnlijk niet het eerste priemgetal heeft gegenereerd (2).

Als je wilt controleren of je programma goed werkt kan je je gevonden lijst priemgetallen hier 
matchen met een lijst bekende priemgetallen: <http://primes.utm.edu/lists/small/1000.txt>.

## Hacker edition ##

1. Maak bij het testen van een getal `n` gebruik van de kennis over de priemgetallen onder de `n`. Bepaal 
hoeveel sneller dat is voor grote getallen. En tot welk priemgetal kan je komen binnen 1 minuut?

2. Welke getallen (onder n=10000) vormen de langste reeks aaneengesloten niet-priemgetallen ?

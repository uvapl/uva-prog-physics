# Diophantische McNuggets

In de wiskunde bestaat er een klasse vergelijkingen die bekend zijn onder diophantische vergelijkingen. Het 
zijn vergelijkingen waar de variabelen alleen geheeltallig kunnen zijn. De bekendste diophantische vergelijking 
is:

$x ^ n + y ^ n = z ^ n$

Voor $n = 2$ zijn er oneindig veel oplossingen (waarden van $x,y,z$ die elke geheeltallig zijn): Pythagoras. 
De beroemde stelling van Fermat zegt dat voor waarden groter dan 2 er geen geheeltallige oplossing is. Ook 
McDonalds gebruikt diophantische vergelijkingen. Jazeker. McDonalds verkoop namelijk McNuggests in verpakkingen 
van 6, 9 of 20 McNuggets. Het is bijvoorbeeld mogelijk om exact 15 McNuggets te kopen (1x6 + 1x9), maar 
onmogelijk om 16 McNuggets te kopen. We gaan in deze opgave berekenen wat het grootste aantal McNuggets is 
dat je kan bestellen dat niet precies 'past'. Om te kijken of je precies $n$ McNuggets kan kopen moet je een 
diophantische vergelijking oplossen, namelijk: vind positieve gehele getallen $a$, $b$ en $c$ zodanig dat:

$6a + 9b + 20c = n$

Voor we in opgave 5 gaan bepalen wat het grootste aantal McNuggets is dat
niet precies besteld kan worden proberen we 2 strategie-hints uit te werken.

## Opgave 3

Laat zien dat het mogelijk is om precies 50, 51, 52, 53, 54 en 55 McNuggets te bestellen (met pen en papier of eigen programma). Laat steeds zien hoeveel doosjes van 6,9 en 20 McNuggets je krijgt.

**Theorema**: Als het mogelijk is exact $x, x+1, ..., x+5$ McNuggets te bestellen dan betekent dat, dat je 
elk aantal McNuggets $>=x$ kan bestellen als de McNuggets komen in doosjes van 6, 9 en 20.

## Opgave 4

Beschrijf waarom bovenstaand theorema waar is (in tekst) en overtuig jezelf dat het antwoord uit vraag 3 
($50, 51, ..., 55$) betekent dat ook ($56, 57, ... 61$) een oplossing zijn. Sterker: alle aantallen boven de 50.

## Opgave 5

Schrijf een programma dat het grootste aantal McNuggets (Nmax) bepaalt dat niet precies past in doosjes 
van 6,9 en 20.

**Note**: de output van het programma moet als volgt op het scherm komen:

	Het grootste aantal McNuggets dat niet exact besteld kan worden is:  ...

### Strategie Hints: ###

* Gebruik de antwoorden uit vraag 3 en 4 in je strategie.
* Bedenk voor je begint goed welke grootheden je bij moet houden als je
door de verschillende mogelijkheden heen-'loopt'.

Youtube filmpje met het goede antwoord: McDonaldsmedewerkertje pesten

Nu we een concrete vraag hebben opgelost kunnen we ons programma uitbreiden naar een meer algemene 
oplossing. We gaan nu oplossingen bekijken voor verschillende keuzes van doosjes grootte (wel nog steeds 
3 doosjes). Stel dat er een variabele in je programma is (tuple of array van lengte 3) is die packages 
heet en de grootte van de verschillende McNugget doosjes bevat.

## Opgave 6

Schrijf een programma dat, gegeven 3 verschillende doosjes, het grootste aantal McNuggets vindt (onder de 200) 
dat niet precies in een geheel aantal doosjes past.

Zorg dat je programma de volgende output geeft:

	Gegeven 3 McNuggets doosjes met grootte x, y en z, dan is het grootste aantal McNuggets dat niet exact besteld kan worden: Nmax.

#### Strategie hints:###

* We limiteren onze test tot 200 omdat er in sommige gevallen geen grootste aantal is, denk bijvoorbeeld aan 3 doosjes van 10.
* Test je programma op een groot aantal keuzes door de variabele in packages te veranderen en vergeet niet ook (6,9,20) mee te nemen.


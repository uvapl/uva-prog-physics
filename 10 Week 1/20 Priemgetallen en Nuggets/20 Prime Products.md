# Product van priemgetallen

Vanuit de elementaire getaltheorie is bekend dat voor grote $n$ het product van alle priemgetallen onder de $n$ minder is dan $e ^ n$ en dat bij groeiende $n$ het product steeds dichter bij $e ^ n$ komt te liggen.

## Exercise 2.0 - eigenschappen priemgetallen
Schrijf een programma `products.py` dat laat zien dat dit zo is. Meer specifiek: schrijf een programma dat voor elk getal $n$ de som van de logaritmes van alle priemgetallen uitrekent (van $2$ tot het getal $n$) en vervolgens op het scherm print:

1. het getal $n$,
2. de som van de logaritmes van alle priemgetallen onder $n$, en
3. hun ratio

### Computing hint:###
als je wiskundige operaties wilt gebruiken in python moet je die eerst 'beschikbaar' maken. Dat doe je door ze bovenin je programma te 'importeren':

	from math import *

### Strategie en wat wiskunde:###

Een directe manier zou zijn om het product van de priemgetallen te vergelijken met $e ^ n$, maar het product van veel grote priemgetallen levert al snel een zeer groot getal op. Dit levert snel problemen om met numerieke precisie (dat bespreken we later nog). Door aan beide kanten van het $=$--teken de logaritme te nemen wordt het product van priemgetallen een som van de logaritmes. De oorspronkelijke vergelijking hierboven wordt dan:

$sum_(i=\"prime\", i < n)log(i) < n$,

waarbij het verschil tussen beide kanten kleiner wordt als $n$ groeit.

Tip: begin met je werkende programma van opgave 1.

## Hacker edition

1. Maak een grafiek om je resultaat zichtbaar te maken.


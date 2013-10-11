Vanuit de elementaire getaltheorie is bekend dat voor grote $$n$$ het product
van alle priemgetallen onder de $$n$$ minder is dan $$e^n$$ en en dat bij
groeiende $$n$$ het product steeds dichter bij $$e^n$$ komt te liggen.

Schrijf een programma `products.py` dat laat zien dat dit zo is. Specifiek:
bepaal voor elke $$n$$ de som van de logaritmes van alle priemgetallen (van 2
tot $$n$$) en print op het scherm:

1. het getal $$n$$,
2. de som van de logaritmes van alle priemgetallen onder $$n$$ en,
3. hun ratio.

## Computing hints

Aals je wiskundige operaties wilt gebruiken in python moet je die eerst
'beschikbaar' maken. Dat doe je door ze bovenin je programma te `import`eren.
Als je de sinusfunctie wil gebruiken om bijvoorbeeld sin(0.5) uit te rekenen
moet je die sinusfunctie eerst laden. Bovenin je programma zet je dan (twee
opties):

1. `import math` importeert de math library, in je programma zeg je dan
   `math.sin(0.5)`

2. `from math import *` importeert expliciet alle functies, waardoor je in
   je programma direct `sin(0.5)` kunt gebruiken

## Strategiehints en wiskundige achtergrond

Een directe check is om het product van de priemgetallen te vergelijken met
$$e^n$$. Helaas levert het product al snel een zeer groot getal op, wat
problemen met numerieke precisie oplevert (dat bespreken we later). Door aan
beide kanten van het $$=$$-teken de logaritme te nemen wordt het product van
priemgetallen een som van de logaritmes. De oorspronkelijke vergelijking
hierboven wordt dan:

$$sum_(i="prime", i < n)log(i) < n$$,

waarbij het verschil tussen beide kanten kleiner wordt als $$n$$ groeit. Tip:
begin met je werkende programma van opgave 1.

## Grafiek

Maak een grafiek om je resultaat zichtbaar te maken.

# Opgave 2: Simulatie - clusteren massa onder de zwaartekracht (het heelal)

We gaan het heelal simuleren. Nou ok, een 2-dimensionaal heelal met een klein aantal deeltjes en allene de zwaartekracht, maar toch. Het is precies wat verschillende onderzoeksgroepen (bijvoorbeeld http://maia.ice.cat/mice/) doen: bedenk een initieel heelal, reken door hoe het er 13 miljard jaar later uitziet en vergelijk het met de huidige observaties.


       1. initieer het heelal. In ons geval en 2-dimensionale doos van 1 bij 1.
       
       2. initieer de deeltjes in het heelal. In ons geval puntdeeltjes met massa m (meestal m=1) op bepaalde posities en snelheden.
       
       3. bepaal voor elk deeltje de netto kracht die hij ondervindt van alle andere deeltjes. Dit kan je gebruiken om de versnelling uit te rekenen.
       
          $F = G\frac(Mm)(r\^(2))$. Zorg dat je G kan veranderen.
       
          Tip: behandel x en y afzonderlijk 
       
       4. Neem een kleine stap in de tijd en bepaal de nieuwe snelheid en positie.
       
          Gebruik: $x\_(i+1) = x\_(i) + v\_(x)(i)\Delta t$. 

          Gebruik: $v\_(i+1) = v\_(i) + a\_(x)(i)\Delta t$. 


       5. Ga terug naar stap 3.
       
       
Note: de deeltjes ketsen elastisch tegen de rand van het heelal

Net als in de vorige opgave gaan we bekijken hoe een groep deeltjes 
zich door het heelal gaat verplaatsen. Volg de deeltjes in de tijd 
(neem kleine stapje in t) en hou positie, snelheid en versnelling 
van de deeltjes bij.

Maak voor elke opgave een grafiek van de gemiddelde afstand tussen de deeltjes als functie van de tijd en probeer een animatie van je heelal te maken.

### opgave 2.1: Felix Baumgartner

Initieer een heelal met 2 deeltjes: een grote massa (m=1000) op (x=0.5 en y=0.1) en een kleine massa (m=1) op (x=0.5 en y=0.9).

Kijk hoe de 2 deeltjes gaan bewegen. Specifiek:
       a) plot de afstand tussen de deeltjes als functie van de tijd
       b) plot de y-positie van de grote massa als functie van de tijd
       c) bepaal op welke y-waarde de deeltjes elkaar tegenkomen 
       d) plot de totale kinetische energie als functie van de tijd

### opgave 2.2: uniform heelal

Initieer een heelal met 100 deeltjes: uniform 10x10 op een grid, dus deeltje 1 bevindt zich op ($x\_(1)$,$y\_(1)$) = (0.05, 0.95) en $\Delta\_(x)$ en $\Delta\_(y)$ = 0.10. 

Kijk hoe de deeltjes gaan bewegen. Specifiek:
       a) plot de gemiddelde afstand tussen 2 deeltjes als functie van de tijd
       b) plot de totale kinetische energie als functie van de tijd

### opgave 2.3: de Big Bang

Initieer een heelal met 100 deeltjes die uit 1 punt komen.
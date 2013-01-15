# Foutenpropagatie (de theorie)

### a] Het probleem:
Bepaal de onzekerheid op z als $z=f(a,b)$, met onzekerheden $\Delta$ a en $\Delta$ b.

Tijdens het practicum is aandacht besteed aan het bepalen van de onzekerheid 
op een grootheid z die een functie is van twee variabelen a$pm \Delta$ a en b$pm \Delta$ b. 
De spreiding, voor (ongecorreleerde) variabelen, wordt gegeven door:

$(\Delta z)^2 = (\frac(\partial z)(\partial a))^2 (\Delta a)^2+(\frac(\partial z)(\partial b))^2 (\Delta b)^2$

Dit is natuurlijk uit te breiden naar meer (en gecorreleerde) variabelen. 

Het is niet altijd (makkelijk) om een analytische uitdrukking te krijgen voor $\Delta$z (gaan we 
in het prakticum op in). De manier om numeriek inzicht te krijgen in de verdeling en spreiding 
op z is het uitvoeren van ’test experimenten’ en zo de verdeling van uitkomsten voor z te bepalen.

### b] simuleer een groot aantal experimenten en bereken de spreiding:

Simuleer een groot aantal experimenten $i$ door een random waarde te ’trekken’ uit de verdeling voor a en 
b: $a_i$ en $b_i$ respectievelijk en daarvoor een waarde van $z_i$ te bepalen. Uit de verdeling van z 
kan je de spreiding schatten door de RMS of variantie te bepalen, de gemiddelde afwijking van het gemiddelde:

$RMS = langle z^2 \rangle  = \sqrt(\frac( \sum\_(i)(z\_i - \langle z \rangle )^2 )(N))$

computing hints: 

   * Een random gesimuleerde meting $x_i$ trekken uit gaussisch verdeelde x met gemiddelde mu 
     en breedte sigma gaat als volgt: 

       x_i = gauss(mu, sigma) i.p.v. het ’gewone’ random x_i = random()

.

.

.

# Foutenpropagatie (de opgaves)

### opgave 3.1
Stel dat je twee variabelen a en b hebt gemeten met hun respectievelijke meetfout $\Delta$ a and $\Delta$ b: 
a = 20 $\pm$ 2 en b = 10 $\pm$ 2. Bereken de spreiding (RMS of variantie) op een grootheid c die een combinatie 
is van deze variabelen. Gebruik ook de foutenpropagatie uit het practicumhandleiding om te berekenen wat je 
verwacht.

Maak een grafiek van c voor een groot aantal test-experimenten en bepaal zowel het gemiddelde 
$ \langle c \rangle$ als de spreiding (RMS of $\Delta$c) op $c$ als:

  a) c = a + b

  b) c als c = ab 

  c) c als c = a/b 

  d) c = atan(a/100)sin(b/10).





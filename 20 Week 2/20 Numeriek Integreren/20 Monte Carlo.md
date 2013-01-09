# Numeriek integreren - Monte Carlo (de opgaves)

Bereken, gebruikmakend van de Riemannsom en de Monte Carlo-techniek de volgende integralen. 
Maak ook een grafiek met behulp van Matplotlib.

### opgave 2.1 blabla
Hint: test door

### opgave 2.2 blabla
Hint: test door

### opgave 2.3 blabla
Hint: test door



# Numeriek integreren - Monte Carlo (de theorie)

Benader de integraal door gebruik te maken van random getallen. Gooi in een gebied rond de 
integratie regio random punten en kijk welke fractie binnen het integratiegebied valt.

### a] Het probleem
Gegeven f(x) op a $leq$ x $leq$ b: bereken $int_a^b f(x)dx$

### b] Definieer een ’box’ om de integraalregio heen:

Definieer een box om de integraalregio heen: definieer een xmin, xmax, ymin en ymax zodanig 
dat: xmin ≤ a en xmax ≥ b en dat ook geldt: voor a$leq$x$leq$b: ymin$leq$f(x)$leq$ymax. 
In de meeste toepassingen wordt gekozen voor xmin = a en xmax = b.

### c] Gooi random punten in de box:

Gooi een groot aantal random punten (xi,yi) in de box en bekijk voor elk punt of het binnen 
de functie ligt (’goed’) of erbuiten (’fout’):
  * xi :  random getal tussen xmin en xmax 
  * yi :	random getal tussen ymin en ymax

Is het punt ’goed’ (binnen de functie) of ’fout’ (buiten de functie) ? ’goed’: yi < f(xi) of ’fout’: yi > f(xi)
Let op: bij negatieve f(x) draait definitie om. Visualiseer altijd de functie.

### d] Bepaal de integraal:

De integraal is de fractie punten die binnen de grafiek vallen keer de oppervlakte van de totale box. In ons geval (rechthoek als box) geldt dan:

### Extra:
􏰄 b a
Ngoed f(x) dx =	(xmax − xmin)(ymax − ymin)Ngoed + Nfout
In ’echte’ toepassingen wordt uit het oogpunt van effici ̈entie de box vaak zo gekozen dat hij de
integraal zo nauw mogelijk omsluit. De fractie ’goede’ worpen is dan zo groot mogelijk.

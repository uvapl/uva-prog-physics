# Numeriek integreren - de Riemannsom  (de opgaves)

Bereken, gebruikmakend van de Riemannsom de volgende integralen. 
Maak ook een grafiek met behulp van Matplotlib.

### opgave 2.1 blabla
Hint: test door

### opgave 2.2 blabla
Hint: test door

### opgave 2.3 blabla
Hint: test door



# Numeriek integreren - de Riemannsom  (de theorie)

Evalueer een integraal door het te schrijven als som van kleine rechthoekjes: een zogenaamde Riemannsom.

### a] Het probleem
Gegeven f(x) op a $leq$ x $leq$ b: bereken $int_a^b f(x)dx$

### b] Schrijf de integraal als Riemannsom

Verdeel het interval (a, b) in N intervallen van gelijke lengte $\Delta x$ en 
representeer $f(x)$ door de waarde van de functie op discrete $x$-waarden $x_i$:

$f_i=f(x_i)$, waarbij $x_i = a + i \Delta x$, met  (i=0,1,2,...,N en $\Delta x$ =a−b) 

Schrijf de integraal dan als een Riemannsom:

$int\_a^b f(x) dx = sum\_(i=0)^(N-1) int\_(x\_i)^(x\_(i+1)) f(x) dx$

### c] Benader centrale waarde voor f(x) in elke bin en doe sommatie:

Met behulp van een lineaire benadering (de trapeziumregel) kunnen we de centrale waarde voor 
f(x) benaderen in elke bin door het gemiddelde van de waarden van f(x) op de linker en rechter 
rand van de bin. In deze lineaire benadering op het interval $(x_i,x_(i+1))$ is f(x) dan te schrijven als:

$f(x) = \frac(f\_(i+1)+f\_(i))(2)$

De sommatie voor de integraal uit vergelijking (1) is dan te schrijven als:

$\int_a^b f(x) dx = \frac(\Delta x)(2) (f\_0+)$ 


### Extra: hogere orde (meer precieze) benaderingen:

Het is mogelijk de evaluatie van de integraal te verbeteren door niet te uit te gaan van de 
(te simpele) lineaire benadering. De Simpsonregel bijvoorbeeld is een parabolische benadering 
(let op, N=even) waarbij f(x) op het interval (xi−1,xi+1) wordt benaderd door een parabool door 
de 3 punten (fi−1, fi, fi+1). Zoek op of werk zelf uit als je deze wilt gebruiken.



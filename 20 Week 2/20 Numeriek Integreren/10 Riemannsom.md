## Numeriek integreren - de Riemannsom

Evalueer een integraal door het te schrijven als som van kleine rechthoekjes: een zogenaamde Riemannsom.

### a] Het probleem
Gegeven f(x) op a $leq$ x $leq$ b: bereken $int_a^b f(x)dx$

### b] Schrijf de integraal als Riemannsom

Verdeel het interval (a, b) in N intervallen van gelijke lengte $\Delta x$ en 
representeer $f(x)$ door de waarde van de functie $f(x_i)$ op de $x$-waarden $x_i$:

$f_i=f(xi)$, waarbij $x_i=a+i \Delta x$ (i=0,1,2,...,Nen∆x=a−b) N

Schrijf de integraal dan als een Riemannsom:


$int_a^b f(x) dx =	\Sum_i=0^N f(x) dx	\int_(x_i)^(x_(i+1)) $


### c] Benader centrale waarde voor f(x) in elke bin en doe sommatie:

Met behulp van een lineaire benadering (de trapeziumregel) kunnen we de centrale waarde voor 
f(x) benaderen in elke bin door het gemiddelde van de waarden van f(x) op de linker en rechter 
rand van de bin. In deze lineaire benadering op het interval (xi,xi+1) is f(x) dan te schrijven als:

$\int$

De sommatie voor de integraal uit vergelijking (1) is dan te schrijven als:

$\int$


### Extra: hogere orde (meer precieze) benaderingen:

Het is mogelijk de evaluatie van de integraal te verbeteren door niet te uit te gaan van de 
(te simpele) lineaire benadering. De Simpsonregel bijvoorbeeld is een parabolische benadering 
(let op, N=even) waarbij f(x) op het interval (xi−1,xi+1) wordt benaderd door een parabool door 
de 3 punten (fi−1, fi, fi+1). Zoek op of werk zelf uit als je deze wilt gebruiken.

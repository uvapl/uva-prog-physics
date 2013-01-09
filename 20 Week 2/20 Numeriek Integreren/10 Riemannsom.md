## Numeriek integreren - de Riemannsom

Evalueer een integraal door het te schrijven als som van kleine rechthoekjes: een zogenaamde Riemannsom.

### a] Het probleem
Gegeven f(x) op a $leq$ x $leq$ b: bereken $int_a^b f(x)dx$

### b] Schrijf de integraal als Riemannsom

Verdeel het interval (a, b) in N intervallen van gelijke lengte $\Delta x$ en 
representeer $f(x)$ door de waarde van de functie op discrete $x$-waarden $x_i$:

$f_i=f(x_i)$, waarbij $x_i = a + i \Delta x$, met  (i=0,1,2,...,N en $\Delta x$ =a−b) 

Schrijf de integraal dan als een Riemannsom:

$\int_a^b f(x) dx = \sum_i^N f(x) dx \int_x^x) f(x) dx$


### c] Benader centrale waarde voor f(x) in elke bin en doe sommatie:

Met behulp van een lineaire benadering (de trapeziumregel) kunnen we de centrale waarde voor 
f(x) benaderen in elke bin door het gemiddelde van de waarden van f(x) op de linker en rechter 
rand van de bin. In deze lineaire benadering op het interval $(x_i,x_(i+1))$ is f(x) dan te schrijven als:

$f(x) = \frac( f_(i+1) + f_(i))(2) + Order(\Delta x)$

De sommatie voor de integraal uit vergelijking (1) is dan te schrijven als:

$\int_a^b f(x) dx \approx \frac(\Delta x)(2) (f_0 + 2f_1 + 2f_2 + ... + 2f_N + f_N) + Order((\Delta x)^2)$ 


### Extra: hogere orde (meer precieze) benaderingen:

Het is mogelijk de evaluatie van de integraal te verbeteren door niet te uit te gaan van de 
(te simpele) lineaire benadering. De Simpsonregel bijvoorbeeld is een parabolische benadering 
(let op, N=even) waarbij f(x) op het interval (xi−1,xi+1) wordt benaderd door een parabool door 
de 3 punten (fi−1, fi, fi+1). Zoek op of werk zelf uit als je deze wilt gebruiken.

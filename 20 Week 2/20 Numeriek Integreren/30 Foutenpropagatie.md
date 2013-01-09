## Fouten propagatie

### a] Het probleem:
Bepaal de onzekerheid op z als z = f (a, b), met onzekerheden ∆a en ∆b.

Tijdens het practicum is aandacht besteed aan het bepalen van de onzekerheid 
op een grootheid z die een functie is van twee variabelen x$pm \Delta$x en y$pm \Delta$y. De 
spreiding, voor (ongecorreleerde) variabelen, wordt gegeven door:
􏰀∂z􏰁2 􏰀∂z􏰁2 (∆z)2 =  ∂x	(∆x)2 +	∂y	(∆y)2

Dit is natuurlijk uit te breiden naar meer (en gecorreleerde) variabelen.
Het is niet altijd (makkelijk) om een analytische uitdrukking te krijgen voor ∆z (gaan we in het prakticum op in). De manier om numeriek inzicht te krijgen in de verdeling en spreiding op z is het uitvoeren van ’test experimenten’ en zo de verdeling van uitkomsten voor z te bepalen.

### b] simuleer een groot aantal experimenten en bereken de spreiding:

Simuleer een groot aantal experimenten i door een random waarde te ’trekken’ uit de verdeling voor a en b: ai en bi respectievelijk en daarvoor een waarde van zi te bepalen. Uit de verdeling van z kan je de spreiding schatten door de RMS of variantie te bepalen, de gemiddelde afwijking van het gemiddelde:
􏰅(zi −⟨z⟩)2 RMS = ⟨z2⟩ =	N

computing hints:
   * Een random gesimuleerde meting xi trekken uit gaussisch verdeelde x met gemiddelde mu 
     en breedte sigma gaat als volgt: xi = gauss(mu, sigma) i.p.v. ’gewone’ random xi = random()

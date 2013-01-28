# Data-analyse: temperatuur in Nederland

![TemperatureMapEurope](TemperatureMapEurope.jpg){:.inline}{:style="width:250px"}

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren 
die door de ECA (European Climate Assessment) beschikbaar wordt gemaakt in 
grote ASCII files. Data sets zijn hier beschikbaar: 
[ECA data-sets](http://eca.knmi.nl/dailydata/predefinedseries.php)
Voor elk weerstation, bijvoorbeeld station `XXX` zijn er 2 files: 
`TX_STAID000XXX` en `TN_STAID000XXX` met respectievelijk de maximum temperatuur 
voor elke dag.

We beginnen bescheiden: de temperatuur in De Bilt (station 162). Omdat de data sets groot 
zijn hebben we die van De Bilt hier beschikbaar gemaakt. Download deze files: 
[`TX_STAID000162.txt`](TX_STAID000162.txt) en [`TN_STAID000162.txt`](TN_STAID000162.txt), 
open ze en lees bovenin hoe de data gecodeerd is. We zien bijvoorbeeld dat de 
maximum(minimum) temperatuur op 1 januari 1901 -3.1(-6.8) graden C was. Schrijf een 
programma dat deze file doorloopt en beantwoord de volgende vragen.


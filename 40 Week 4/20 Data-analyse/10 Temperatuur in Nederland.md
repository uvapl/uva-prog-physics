# Data-analyse: temperatuur in Nederland

![TemperatureMapEurope](TemperatureMapEurope.jpg){:.inline}{:style="width:250px"}

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren 
die door de ECA (European Climate Assessment) beschikbaar wordt gemaakt in 
grote ASCII files. Data sets zijn hier beschikbaar: 
[ECA data-sets](http://eca.knmi.nl/dailydata/predefinedseries.php)

We beginnen bescheiden: de temperatuur in De Bilt (station 162). Omdat de data 
sets groot zijn hebben we die van De Bilt beschikbaar gemaakt op 
[http://www.nikhef.nl/ ̃ivov/Python/KlimaatData/](http://www.nikhef.nl/\ ̃ivov/Python/KlimaatData/).

Download de file `TX STAID000162.txt` (maximum temperatuur voor elke dag) en `TN STAID000162.txt` 
(minimum temperatuur voor elke dag), open ze en lees bovenin hoe de data gecodeerd is. We zien 
dat de maximum(minimum) temperatuur op 1 januari 1901 -3.1(-6.8) graden C was. Schrijf een 
programma dat de file doorloopt en beantwoord de volgende vragen.

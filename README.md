# Rail NL

Deze case gaat over het maken van een dienstvoering. Deze dienstvoering bestaat uit een aantral trajecten, waar treinen overheen rijden. Een traject is een route van stations in een bepaalde volgorde, met een bepaalde tijdsduur. Daarnaast kan men kiezen tussen het maken van een dienstvoering voor de provincies Noord en Zuid Holland of heel Nederland.
Een dienstvoering bestaat uit maximaal 7 (Noord en Zuid Holland) of maximaal 20 (heel Nederland) trajecten.
Een traject mag niet langer zijn dan het opgegeven tijdsframe. 


Gegeven zijn een aantal stations en verbindingen tussen deze stations. 

Voor Noord en Zuid Holland:
    22 stations, waarvan 7 kritiek en 28 verbindingen, waarvan 20 kritiek. 
    
Voor heel Nederland:
    60 stations, waarvan 23 kritiek en 89 connecties, waarvan 60 kritiek.

## Doel

Tijdens deze case is ons uiteindelijke doel het optimaliseren van de volgende functie:

K = p10000 - (T20 + Min/10)

Waarbij:

K = kwaliteit van de ontwikkelde dienstregeling
P = de fractie (percentage gedeeld door 100) van bezochte kritieke verbindingen
T = aantal trajecten
MIN = aantal minuten

## Beperkingen 

Voor Noord en Zuid Holland:

Maximale T : 7 

Maximaal aantal minuten per traject: 120
    
Voor heel Nederland:

Maximale T : 20

Maximaal aantal minuten per traject: 180

## Toestandsruimte

Voor het berekeken van de toestandsruimte hebben we gekeken naar twee verschillende aspecten van de opdracht:
- de K functie
- het aantal verschillende combinaties van trajecten

### Toestandruimte K-functie

Voor het minimaliseren van de K functie is het noodzakelijk om het eerste gedeelte van de functie: p10000, te minimaliseren. 
Dit wordt gerealiseerd door een p van 0, wat betekent dat er geen kritieke verbindingen worden aangedaan. 

Daarna is het zaak om het tweede gedeelte van de functie: - (T20 + Min/10), te maximaliseren voor een zo laag mogelijke K.
Door de gegeven beperking is T voor Noord en Zuid Holland maximaal 7 -> *T = 7*, en voor heel Nederland maximaal 20 -> *T = 20*.

Het tweede deel van de kostenfunctie bestaat uit het aantal minuten. Voor deze berekening gaan we ervan uit dat men 120 (voor Noord en Zuid Holland) of 180 (voor heel Nederland) heen en weer rijdt over een niet kritiek traject. Dit zou leiden tot de volgende waarde van MIN: 7 / 20 van deze trajecten, 120*7 = 840 -> *MIN = 840*, en voor heel Nederland 180*20 = 3600 -> *MIN = 3600*

*lowerbound K (Noord en Zuid Holland) = 0x10000 - ( 7x20 + 840/10 ) = - 224* 
*lowerbound K (Nederland) = 0x10000 - ( 20x20 + 3600/10 ) = - 760* 

Met 20 / 60 kritieke verbindingen zijn we tot de conclusie gekomen dat elke kritieke verbinding met betrekking tot de K functie een toegevoegde waarde heeft van 10000/20 = 500 of 10000/60 = 166.67. Dit betekent dat een kritieke verbinding maarliefst 500/(1/10) = 5000  of 166.67/(10) = 1667.7 minuten lang moet zijn voordat een kritieke verbinding geen waarde meer toevoegt. In deze casus is geen enkele kritieke verbinding zo lang.
Voor het maximaliseren van de K functie is het dus noodzakelijk om de maximale P te kiezen -> *P = 1*

Als we de lengte in minuten van alle kritieke verbindingen bij elkaar optellen komen op tot 275 minuten. Omdat een traject maximaal 120 minuten lang mag zijn komen betekent dit dat er in een ideale situaie minimaal 3 trajecten nodig zijn. oftwel:
-> *T = 3* 
-> *MIN = 275*

*Upperbound K = 1x10000 - ( 3x20 + 275/10 ) = 9912,5*

## Gebruik

#### Om het programma te gebruiken dienen eerst de requirements uit requirements.txt geinstalleerd te worden.
```
pip install -r requirements.txt 
```

#### Om het programma te starten voert men eerst de volgende command uit.
```
    python main.py
```

#### *Keuze 1: Kaart van heel Nederland of alleen Noord- en Zuid-Holland?*

| *Kaart*                	| *Command* 	|
|------------------------	|:---------:	|
| Nederland              	| ``` 1 ``` 	|
| Noord- en Zuid-Holland 	| ``` 2 ``` 	|

#### *Keuze 2: Uitvoer van een algorithme of visualisatie van resultaten?*

| *Keuze*       	|   *Command*   	|
|---------------	|:-------------:	|
| Algorithmes   	| ``` ENTER ``` 	|
| Visualisaties 	|   ``` v ```   	|

*NB: een visualisatie kan pas worden uitgevoerd nadat er resultaten zijn geproduceerd.*

#### *Keuze 3: Welk algorithme?*

| *Algorithm*         	| *Command*                                 	|
|---------------------	|:-------------------------------------------:	|
| Random              	|             ```     r ```            	|
| Greedy              	|               ``` g ```              	|
| Hillclimber         	|            ``` h ```            	|
| Simulated Annealing 	| ``` s  ``` |

*NB: een visualisatie met een kaart (MapHelper) kan alleen worden geproduceerd na het runnen van Hillclimber of Simulated Annealing.*

#### *Keuze 4: Hoeveel iteraties (n) ?*
```
n
```


## Requirements

- matplotlib 2.1.0
- os 16.1
- sys 29.1
- csv 14.1
- random 9.6
- re 6.2
- networkx 2.0



```
## Credits
By Darian El Sayed and Felix Mooij for de Universiteit van Amsterdam.

# Rail NL

Deze case gaat over het maken van de lijnvoering, wat zijn de trajecten waarover de treinen gedurende de dag heen en weer rijden? 
Meer specifiek: over de lijnvoering van intercitytreinen. Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet. 
Een traject is een route van sporen en stations waarover treinen heen en weer rijden. 
Een traject mag niet langer zijn dan het opgegeven tijdsframe. 

Gegeven zijn 22 stations, waarvan 7 kritiek en 28 verbindingen, waarvan 20 kritiek. 

## Doel

Tijdens deze case is ons uiteindelijke doel het optimaliseren van de volgende functie:

K = p*10000 - (T*20 + Min/10)

K = kwaliteit van de ontwikkelde dienstregeling
P = de fractie (percentage gedeeld door 100) van bezochte kritieke verbindingen
T = aantal trajecten
MIN = aantal minuten

## Beperkingen 

Maximale T : 7
Maximaal aantal minuten per traject: 120

## Toestandsruimte

Voor het berekeken van de toestandsruimte hebben we gekeken naar twee verschillende aspecten van de opdracht:
- de K functie
- het aantal verschillende combinaties van trajecten

### Toestandruimte K-functie

Voor het minimaliseren van de K functie is het noodzakelijk om het eerste gedeelte van de functie: p*10000, te minimaliseren. 
Dit wordt gerealiseerd door een p van 0, wat betekent dat er geen kritieke verbindingen worden aangedaan. 

Daarna is het zaak om het tweede gedeelte van de functie: - (T*20 + Min/10), te maximaliseren voor een zo laag mogelijke K.
Door de gegeven beperking is T maximaal 7 -> *T = 7*

We hebben daarna vastgesteld dat het langst mongelijke traject zonder een kritieke verbinding aan te doen de volgende is:
Amsterdam Sloterdijk-> Amsterdam Zuid-> Schiphol Airport-> Leiden Centraal-> Alphen a/d Rijn, tijdsduur: 51 min
We gaan er vanuit dat er een dienstregeling onstaat van 7 van deze trajecten, 51*7 = 357 -> *MIN = 357*

*lowerbound K = 0*10000 - ( 7*20 + 357/10 ) = - 175,7* 

Met 21 kritieke verbindingen zijn we tot de conclusie gekomen dat elke kritieke verbinding met betrekking tot de K functie een toegevoegde waarde heeft van 10000/20 = 500. Dit betekent dat een kritieke verbinding maarliefst 500/(1/10) = 5000 minuten lang moet zijn voordat een kritieke verbinding geen waarde meer toevoegt. In deze casus is geen enkele kritieke verbinding zo lang.
Voor het maximaliseren van de K functie is het dus noodzakelijk om de maximale P te kiezen -> *P = 1*

Als we de lengte in minuten van alle kritieke verbindingen bij elkaar optellen komen op tot 275 minuten. Omdat een traject maximaal 120 minuten lang mag zijn komen betekent dit dat er in een ideale situaie minimaal 3 trajecten nodig zijn. oftwel:
-> *T = 3* 
-> *MIN = 275*

*Upperbound K = 1*10000 - ( 3*20 + 275/10 ) = 9912,5*





```
## Credits
By Darian El Sayed, Felix Mooij and Bram Schmidt for de Universiteit van Amsterdam.

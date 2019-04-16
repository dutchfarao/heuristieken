# Rail NL

Deze case gaat over het maken van de lijnvoering, wat zijn de trajecten waarover de treinen gedurende de dag heen en weer rijden? 
Meer specifiek: over de lijnvoering van intercitytreinen. Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet. 
Een traject is een route van sporen en stations waarover treinen heen en weer rijden. 
Een traject mag niet langer zijn dan het opgegeven tijdsframe. 

Gegeven zijn 22 stations, waarvan 7 kritiek en 28 verbindingen, waarvan 21 kritiek. 

## Doel

Tijdens deze case is ons uiteindelijke doel het optimaliseren van de volgende functie:

K = p*10000 - (T*20 + Min/10)

K = kwaliteit van de ontwikkelde dienstregeling
P = de fractie (percentage gedeeld door 100) van bezochte kritieke verbindingen
T = aantal trajecten
MIN = aantal minuten

## Beperkingen 

Maximale T : 7
Maximaal aantal minuten per traject: 200

## Toestandsruimte

Voor het berekeken van de toestandsruimte hebben we gekeken naar twee verschillende aspecten van de opdracht:
- de K functie
- het aantal verschillende combinaties van trajecten

### Toestandruimte K-functie

Voor het minimaliseren van de K functie is het noodzakelijk om het eerste gedeelte van de functie: p*10000, te minimaliseren. 
Dit wordt gerealiseerd door een p van 0, wat betekent dat er geen kritieke verbindingen worden aangedaan. 

Daarna is het zaak om het tweede gedeelte van de functie: - (T*20 + Min/10), te maximaliseren voor een zo laag mogelijke K.
Door de gegeven beperking is T maximaal 7 -> T = 7

We hebben daarna vastgesteld dat het langst mongelijke traject zonder een kritieke verbinding aan te doen de volgende is:
Amsterdam Sloterdijk-> Amsterdam Zuid-> Schiphol Airport-> Leiden Centraal-> Alphen a/d Rijn, tijdsduur: 51 min
We gaan er vanuit dat er een dienstregeling onstaat van 7 van deze trajecten, 51*7 = 357 -> MIN = 357

*lowerbound K = 0 - ( 7*20 + 357/10 ) = - 175,7*



```
## Credits
By Darian El Sayed, Felix Mooij and Bram Schmidt for de Universiteit van Amsterdam.

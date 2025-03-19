import csv

from helper import bereken_totaal

from presentatie import toon_inkomsten

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

totaal_inkomsten = bereken_totaal(inkomsten)

toon_inkomsten = bereken_totaal(inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
 writer = csv.writer(csvfile, delimiter=';')

for item, bedrag in inkomsten.items():
 writer.writerow([item, bedrag])
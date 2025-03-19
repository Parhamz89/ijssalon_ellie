def toon_inkomsten(inkomsten_dict, totaal):
    for item, bedrag in inkomsten_dict.items():
        print(f"{item}: {bedrag} euro") # Print elk item met het bijbehorende bedrag

print("==========================")

print(f"Totaal: {totaal} euro") # Print het totaal bedrag
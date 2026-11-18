# consegne :
# Riscrivete il programma dell'inizio, da zero, senza guardarlo.\
# Questi sono i dati:
# Il programma deve stampare i mesi sopra il budget, il totale dell'anno\
# e la media mensile con due decimali.

mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
spese = [820, 760, 910, 700, 680, 1250, 890, 1420, 730, 770, 800, 1100]
budget = 900


# Stampa mesi sopra a budget

mesi_sopra = []

for i in range(len(spese)):
    if spese[i] >900:
        mesi_sopra.append(mesi[i])
        
print (f" I mesi che superano 900 sono: {mesi_sopra}")

# il totale dell'anno

totale_anno=sum(spese)
print(f" il totale delle spese anno è: {totale_anno}")


# Spesa media mesile 2 decimali

totale_speseAnno=sum(spese)
media_spese=totale_speseAnno / len (spese)
print (f"La media delle spese è : {media_spese:.2f}")
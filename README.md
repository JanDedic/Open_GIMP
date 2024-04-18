
Skript, který otevírá png snímky do GIMPU

Vytvořím si prázdný seznam, následně pomocí for cyklu iteruju přes adresářovou strukturu a příkazem os.walk ji procházím
a os.getcwd zapíše cestu k souboru. další for loop se už konkrétně kouká na snímky.
Pokud soubor končí .png, tak jej přidá do seznamu s kompletní cestou. Následně se spustí GIMP, který se načítá s cestami uloženými v seznamu.




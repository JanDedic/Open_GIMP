
Skript, který otevírá png snímky do GIMPU

Vytvořím si prázdný seznam, následně pomocí for cyklu iteruju přes adresářovou strukturu a příkazem os.walk ji procházím
a os.getcwd zapíše cestu k souboru. další for loop se už konkrétně kouká na snímky.
Pokud soubor končí .png, tak jej přidá do seznamu s kompletní cestou. Následně se spustí GIMP, který se načítá s cestami uloženými v seznamu.

To si můžete vyzkoušet na přiloženém obrázku panda.png

######################################################

1, jako první si zkontrolujte, zda cesta ke gimpu/inkscapu odpovídá vaší cestě v PC ke gimpu/inkscapu.

2, první si dám soubor do složky, kde mám snímky.

3, přes cmd se přepnu příkazem: cd "cesta k souboru".

4, skript sputím tím, že do příkazového řádku napíšu: python3 open.py

######################################################

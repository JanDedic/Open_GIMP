import os

files = []
for root,dirs,filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if (filename.endswith(".png")):
            path = (os.path.join(root, filename)) 
            files.append(path)
os.system("C:/GIMP/GIMP2/bin/gimp-2.10 " + " ".join(files))

"""
Skript, který otevírá snímky do GIMPU

"""





Iteruje přes adresářovou strukturu:
Používá funkci os.walk k iteraci přes všechny podadresáře a soubory v aktuálním pracovním adresáři (os.getcwd()).
Pro každý soubor ve struktuře adresářů zjišťuje, zda končí příponou .png.
Pokud soubor končí příponou .png, přidává jeho plnou cestu (os.path.join(root, filename)) do seznamu files.
Otevírá GIMP:
Poté, co je vytvořen seznam files obsahující cesty ke všem souborům s příponou .png ve struktuře adresářů, spouští systémový příkaz (os.system).
Příkaz používá cestu k spustitelnému souboru GIMP (C:/GIMP/GIMP2/bin/gimp-2.10) a předává jako argumenty všechny cesty k souborům .png z files.
Tímto způsobem je GIMP otevřen s uvedenými soubory, které budou načteny do programu.




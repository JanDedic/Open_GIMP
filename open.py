#import knihovny pro práci se soubory
import os
#definuju menu, kde si vybírám, jestli otevřu snímky v gimpu nebo inkscapu
def menu():
    print("Menu:")
    print("1. Otevře snímky v gimpu")
    print("2. Otevře snímky v inkscapu")
    choice = input("Vyberte možnost (1-2): ")
    if choice == "1":
        opengimp()
    if choice == "2":
        openink()
def opengimp():         
    #vytvoří seznam, do kterého se budou přidávat cesty k souborům
    files = []

    #for cyklus, který prochází vnořenou strukturu a os.getcvwd bere cestu
    for root,dirs,filenames in os.walk(os.getcwd()):
        #druhá smyčka prochází přímo snímky ve finální složce ze snímky, 
        #pokud jsou ve formátu png, tak přidá do proměné path cestu k souboru + název souboru.
        for filename in filenames:
            if (filename.endswith(".png")):
                path = (os.path.join(root, filename)) 
                #přidá do seznamu cestu k souboru
                files.append(path)
    #kvůli omezení CMD na +-8000 znaků se načítá text do souboru .bat
    input_file = "spustit_gimp.bat"
    #otevře soubor
    with open(input_file, "w") as file:
        #zapíše do souboru cestu k gimpu.exe a přidá k němu cestu ze seznamu, tudíž se gimp spustí s cestou ke snímku, který se má otevřít
        file.write(f"C:/GIMP/GIMP2/bin/gimp-2.10 {' '.join(files)}")
    #spustí soubor a začne otevírat snímky v gimpu
    os.system("spustit_gimp.bat")
def openink():
    files = []

    #for cyklus, který prochází vnořenou strukturu a os.getcvwd bere cestu
    for root,dirs,filenames in os.walk(os.getcwd()):
        #druhá smyčka prochází přímo snímky ve finální složce ze snímky, 
        #pokud jsou ve formátu png, tak přidá do proměné path cestu k souboru + název souboru.
        for filename in filenames:
            if (filename.endswith(".png")):
                path = (os.path.join(root, filename)) 
                #přidá do seznamu cestu k souboru
                files.append(path)
    #kvůli omezení CMD na +-8000 znaků se načítá text do souboru .bat
    input_file = "spustit_ink.bat"
    #otevře soubor
    with open(input_file, "w") as file:
        #zapíše do souboru cestu k gimpu.exe a přidá k němu cestu ze seznamu, tudíž se gimp spustí s cestou ke snímku, který se má otevřít
        file.write(f"C:/Inkscape/bin/inkscape --without-gui {' '.join(files)}")
    #spustí soubor a začne otevírat snímky v gimpu
    os.system("spustit_ink.bat")
menu()

######################################################
#jako první si zkontrolujte, zda cesta ke gimpu/inkscapu odpovídá vaší cestě v PC ke gimpu/inkscapu
#první si dám soubor do složky, kde mám snímky
#přes cmd se přepnu příkazem: cd "cesta k souboru"
#skript sputím tím, že do příkazového řádku napíšu: python3 open.py
######################################################
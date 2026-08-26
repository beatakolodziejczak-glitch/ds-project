sciezka = "data/processed/train_fold_03_normalized.csv"
czesci_sciezki = sciezka.split("/")
folder = czesci_sciezki[1]
pelna_nazwa_pliku = czesci_sciezki[2]
czesci_nazwy = pelna_nazwa_pliku.split(".")
nazwa_bez_rozszerzenia = czesci_nazwy[0]
format_pliku = czesci_nazwy[1]
elementy_nazwy = nazwa_bez_rozszerzenia.split("_")
typ_zbioru = elementy_nazwy[0]
numer_fold = elementy_nazwy[2]
print(f"Folder: {folder}")
print(f"Typ zbioru: {typ_zbioru}")
print(f"Numer fold: {numer_fold}")
print(f"Format pliku: {format_pliku}")

liczba_probek = 50000
batch_size = 128
liczba_epok = 50
czas_na_batch = 0.15

# Obliczamy liczbe batchy na epoke (dzielenie calkowite i modulo)
batchy_pelnych = liczba_probek // batch_size
reszta = liczba_probek % batch_size
batchy_na_epoke = batchy_pelnych + (1 if reszta > 0 else 0)

# Obliczamy calkowity czas w sekundach
czas_epoki_sek = batchy_na_epoke * czas_na_batch
calkowity_czas_sek = czas_epoki_sek * liczba_epok

# Konwersja na godziny, minuty i sekundy
godziny = int(calkowity_czas_sek // 3600)
reszta_sek = calkowity_czas_sek % 3600
minuty = int(reszta_sek // 60)
sekundy = int(reszta_sek % 60)

# Wyswietlenie wyniku
print(f"Szacowany czas: {godziny} h {minuty} min {sekundy} s")

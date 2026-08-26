wagi = [65.5, 78.2, 54.8, 92.1, 70.0]

# 1. Obliczamy srednia
srednia = sum(wagi) / len(wagi)

# 2. Obliczamy odchylenie standardowe (std)
wariancja = sum((x - srednia) ** 2 for x in wagi) / len(wagi)
std = wariancja ** 0.5

# 3. Obliczamy z-scores i wyswietlamy wyniki
print(f"{"Waga (kg)":<10} | {"Z-score":<10} | {"Interpretacja":<20}")
print("-" * 50)

for x in wagi:
    z = (x - srednia) / std
    
    # Interpretacja zgodnie z wymaganiami
    if z > 2:
        interpretacja = "wartość bardzo wysoka"
    elif z < -2:
        interpretacja = "bardzo niska"
    elif abs(z) < 1:
        interpretacja = "typowa"
    else:
        interpretacja = "poza typową (umiarkowana)"
        
    print(f"{x:<10} | {z:<10.2f} | {interpretacja:<20}")

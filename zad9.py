min_val = 50
max_val = 100
wartosci = [75, 50, 100, 62.5]

print(f"{"Wartość oryg.":<15} | {"Wartość znorm.":<15} | {"Czy w przedziale?":<15}")
print("-" * 55)

for value in wartosci:
    normalized = (value - min_val) / (max_val - min_val)
    status = "Tak" if 0 <= normalized <= 1 else "Nie"
    print(f"{value:<15} | {normalized:<15.2f} | {status:<15}")

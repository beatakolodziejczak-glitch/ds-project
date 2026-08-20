total_samples = 1000

train_size = total_samples * 70 // 100
val_size = total_samples * 15 // 100
test_size = total_samples * 15 // 100

current_sum = train_size + val_size + test_size
remainder = total_samples - current_sum
train_size += remainder

print(f"Zbiór treningowy: {train_size} próbek")
print(f"Zbiór walidacyjny: {val_size} próbek")
print(f"Zbiór testowy: {test_size} próbek")
print(f"Suma próbek: {train_size + val_size + test_size}")


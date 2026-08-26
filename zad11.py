learning_rate = 0.01
batch_size = 64
epochs = 100
dropout = 0.5

if 0 < learning_rate <= 1:
    print("learning_rate: OK")
else:
    print("learning_rate: BŁĄD!")

is_power_of_two = batch_size > 0 and (batch_size & (batch_size - 1)) == 0
if is_power_of_two:
    print("batch_size: OK")
else:
    print("batch_size: BŁĄD!")

if 0 < epochs < 1000:
    print("epochs: OK")
else:
    print("epochs: BŁĄD!")

if 0 <= dropout <= 1:
    print("dropout: OK")
else:
    print("dropout: BŁĄD!")

from cs50 import get_float

#Prompt user for float input
change = get_float("Change owed: ")
while change <= 0:
    input = int(get_float("Change owed: "))

coin_total = 0
remainder = change
change_available = [0.25, 0.10, 0.05, 0.01]

for x in change_available:
    coins_used = round(remainder // x, 2)
    remainder = round(remainder % x, 2)
    coin_total += coins_used

print(coin_total)
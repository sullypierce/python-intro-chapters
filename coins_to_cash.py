def calc_dollars():
    piggyBank = {
    "quarters": 99,
    "pennies" : 342,
    "nickels" : 9,
    "dimes" : 32
    }
    total = 0
    total += piggyBank["quarters"]*.25
    total += piggyBank["pennies"]*.01
    total += piggyBank["nickels"]*.05
    total += piggyBank["dimes"]*.1
    print(total)

calc_dollars()    

dollarAmount = 8.69

def coin_numbers(amount):
    piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
    }
    amount *= 100
    print(amount)
    piggyBank["quarters"] = int(amount/25)
    amount %=25
    piggyBank["dimes"] = int(amount/10)
    if amount/10 >= 1:
        amount %=10
    piggyBank["nickels"] = int(amount/5)
    if amount/5 >= 1:
        amount %=5
    piggyBank["pennies"] = int(amount/1)
    print(piggyBank)


coin_numbers(dollarAmount)

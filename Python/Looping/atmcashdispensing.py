amt = int(input("Enter the amount you want to withdraw: "))

twok = fiveh = twoh = h = 0

while amt > 0:
    if amt >= 2000:
        twok += 1
        amt -= 2000
    elif amt >= 500:
        fiveh += 1
        amt -= 500
    elif amt >= 200:
        twoh += 1
        amt -= 200
    elif amt >= 100:
        h += 1
        amt -= 100
    else:
        print("Amount cannot be withdrawn in available denominations.")
        break

print("2000 notes:", twok)
print("500 notes:", fiveh)
print("200 notes:", twoh)
print("100 notes:", h)

odds = [x for x in range(20) if x % 2]

print(odds)


newOdds = []
for x in range(20):
    if x % 2:
        newOdds.append(x)
print(newOdds)
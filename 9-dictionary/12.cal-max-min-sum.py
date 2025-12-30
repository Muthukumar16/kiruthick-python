# Calculate

dTuples = {(1,2): "One", (3,4): "Two"}
dStr = {'Green': 1, "Blue": 2, "Red": 3}
dDigits = {41: 'N', 12: 'S', 32: 'A', 24: "C"}
dFloat = {4.1: 'N', 1.2: 'S', 3.2: 'A', 2.4: "C"}

print(min(dTuples), min(dStr), min(dDigits), min(dFloat))
# O/P: (1, 2) Blue 12 1.2

print(max(dTuples), max(dStr), max(dDigits), max(dFloat))
# O/P: (3, 4) Red 41 4.1

print(sum(dDigits), sum(dFloat))
# O/P: 109 10.9

#print(sum(dTuples), sum(dStr))
# O/P: TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
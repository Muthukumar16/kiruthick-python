# `+` Concat Operator
tpl1 = (1,2,3)
tpl2 = (6,7,8)
tpl3 = tpl1 + tpl2
print(tpl3) # O/P: (1, 2, 3, 6, 7, 8)
tpl4 = tpl3 + (30, 32, 34)
print(tpl4) # O/P: (1, 2, 3, 6, 7, 8, 30, 32, 34)

# Exceptional Flow
# tpl1 + 2
# tbl1 + (3)
# TypeError: can only concatenate tuple (not "int") to tuple

# Replicate
print(tpl1 * 3) # O/P: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Slicing
tpl = (10,12,14,20,22,24,30,32,34)
seq = tpl[:3]
print(seq)          # O/P: (10, 12, 14)
print(tpl[3:-3])    # O/P: (20, 22, 24)
# Giving Upper limit beyond the size of the tuple, it is automatically falling in range
print(tpl[3:30])    # O/P: (20, 22, 24, 30, 32, 34)
# Giving Lower limit beyond much lower, it is automatically falling in range
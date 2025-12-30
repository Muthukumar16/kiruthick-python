st = "@My name is nitin and my digital is nin @72"
str1 = st.split()
lstr1 = len(str1)
str2 = st.replace(" ", "")
lstr2 = len(str2)
freq = {}
for i in range(0, lstr1):
    if str1[i] == str1[i][::-1]:
        print(str1[i])
for c in str2:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

max_char = max(freq)
print(max_char)



# Counting freq. of items.
txt = "This is simple string"
words = txt.split()
print(words)
# O/P: ['This', 'is', 'simple', 'string'] - split by spaces (default delimiter)

txtCSV = "One,Two,Three,Four,Five,Six"
wordsCSV = txtCSV.split(",")
print(wordsCSV)
# O/P: ['One', 'Two', 'Three', 'Four', 'Five', 'Six'] - Split by comma separator delimiter

test = txtCSV.split("T")
print(test)
# O/P: ['One,', 'wo,', 'hree,Four,Five,Six'] - Split by delimiter "T"

# Count frequency of a list of elements using a dictionary

import json
sentence = "This is a super idea This idea will change the idea of learning"
words = sentence.split() #
print(words)
# O/P: ['This', 'is', 'a', 'super', 'idea', 'This', 'idea', 'will', 'change', 'the', 'idea', 'of', 'learning']
dictCountWords = {} # Create dictionary to keep Word <key> : Value <counts>
for word in words:
    key = word
    if key not in dictCountWords:
        counts = words.count(word)
        dictCountWords[key] = counts

print(json.dumps(dictCountWords, indent=3))
# O/P:
# {
#    "This": 2,
#    "is": 1,
#    "a": 1,
#    "super": 1,
#    "idea": 3,
#    "will": 1,
#    "change": 1,
#    "the": 1,
#    "of": 1,
#    "learning": 1
# }
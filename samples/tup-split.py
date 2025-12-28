# Write a menu driven program in Python to count number of words, characters, vowels, digits and alphabets in a given string.
x = input("Enter a string: ")
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "U")
count = 0
count_of_digit = 0
alphabet = 0
for i in x:
  if i.isdigit():
    count_of_digit += 1
  elif i.isalpha():
    alphabet += 1
  if i in vowels:
    count += 1

y = x.split()
print("number of words are:", len(y))
print("number of digit is: ", count_of_digit)
print("number of alphabet is: ", alphabet)
print("number of charectar is: ", len(x))
print("Number of vowel is:", count)

# setdefault() Method

#Given key is NOT ALREADY PRESENT in the dictionary
Marks = {1: 150, 2: 250, 3: 300}
print(Marks)
# O/P: {1: 150, 2: 250, 3: 300}
Marks.setdefault(5, 500)
print(Marks)
# O/P: {1: 150, 2: 250, 3: 300, 5: 500}

#Given key is ALREADY PRESENT in the dictionary
Marks.setdefault(5, 555)
print(Marks)
# O/P: {1: 150, 2: 250, 3: 300, 5: 500} - Not make any changes in the Marks dict

#New Key without value
Marks.setdefault(6)
print(Marks)
# O/P: {1: 150, 2: 250, 3: 300, 5: 500, 6: None} - default value is None

# Example
digits = {}
d1 = digits.setdefault(1, 'M')
d2 = digits.setdefault(2, "K")
d3 = digits.setdefault(3)
print(d1, d2, d3)
# O/P: M K None

# Set values during runtime using loop
new_dic = {}
for i in range(5):
    new_dic.setdefault(i)
print(new_dic)
# O/P: {0: None, 1: None, 2: None, 3: None, 4: None}

# update() Method - merge elements

emp1 = {'name': 'Kiryu', 'age': 17}
emp2 = {'name': 'Muthukumar', 'age': 50, 'city': 'Bangalore'}
emp2.update(emp1)
print(emp2)
# O/P: {'name': 'Kiryu', 'age': 17, 'city': 'Bangalore'}
print(emp1)
# O/P: {'name': 'Kiryu', 'age': 17}

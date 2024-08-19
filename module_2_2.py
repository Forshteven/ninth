grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_students = sorted(students)
print(list_of_students)
middle = [sum(i)/len(i) for i in grades]
print(middle)
k = dict(zip(list_of_students, middle))
print(k)
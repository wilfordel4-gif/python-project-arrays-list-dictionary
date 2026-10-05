students =["brian","Mary","Ann","John","Jane"]
print(students)
students.append("John")
print(students)
students.remove("Mary")
print(students)
age = [20, 21, 22]
future_age = [age + 2 for age in age]
print(future_age)
age.append(23)
age.append(24)
print(age)
del age[0]
print(age)
age[1] = 25
print(age)

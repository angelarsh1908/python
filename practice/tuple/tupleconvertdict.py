# create a list
# l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# d = {}
# for a, b in l:
#     d.setdefault(a, []).append(b)
# print(d)

# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])    

# sort the table by age
import operator
a.sort(key=operator.itemgetter(1))    

# print the table
print(a)


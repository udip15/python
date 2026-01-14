# import requests

# names = ["hello","hi"]

# for name in names:
#     print(name)
#  names.append("HI")
# print(names)

students = []
st1= {
  "name" : "Ram",
  "age" : 20
}
students.append(st1)
st2 = {

    "name" : "hari",
    "age" : 22
}

students.append(st2)


for student in students:
    print(student["name"])
    print(student)

    
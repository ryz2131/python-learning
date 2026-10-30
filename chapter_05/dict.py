# marks = {
#     "riyaz": 90,
#     "sajid": 80,
#     "haroon": 70,
#     "rashid": 60
# }
# # print(marks.items())
# # print(marks.keys())
# # print(marks.values())
# # print(marks.get("riyaz"))
# print(marks.get("ali", 50)
  # This will raise an AttributeError since dictionaries do not have an append method

students = {
    "Ali": 85,
    "Rahul": 70,
    "Amit": 95,
    "Sara": 80
}

# sorted_students = sorted(
#     students.items(),
#     key=lambda x: x[1],
#     reverse=false)
sorted_students = sorted(students.items())
print(sorted_students)





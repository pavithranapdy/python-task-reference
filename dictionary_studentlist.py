students=[
    {
    "name":"aaa",
    "RollNo":"ST345",
    "marks" : [80,75,95,45,100]
    },
    {
    "name":"bbb",
    "RollNo":"ST452",
    "marks" : [100,100,85,65,98]
    },
    {
    "name":"ccc",
    "RollNo":"ST305",
    "marks" : [88,77,99,98,97]
    }]

# include the total/key and sum of marks 
for i in students:
  i["total"]= sum(i["marks"])             # sum the marks in each iteration

# sort the latest list after total mark
for i in range(len(students)):          # swap value x, y = y, x
    for j in range(len(students) - 1):
        if students[j]["total"] < students[j + 1]["total"]:             # compare the mark
            students[j], students[j + 1] = students[j + 1], students[j] # swap the mark value
for i in range(len(students)):
    students[i]["rank"] = i + 1                           # and rank key in the students list
    if students[i]["total"] <= 400 and students[i]["total"] >= 300:
        students[i]["category"]= "Good"                # and category key in the students list
    elif students[i]["total"] <= 450 and students[i]["total"] >= 400:
        students[i]["category"]= "Very Good"
    elif students[i]["total"] <= 500 and students[i]["total"] >= 450:
        students[i]["category"]= "excellent"
    elif students[i]["total"] <= 300 and students[i]["total"] >= 260:
        students[i]["category"]= "average"
    else:
        students[i]["category"]= "below average"

# Print result
for item in students:
    print(item)





# sorted_students = sorted(students, key=lambda s: sum(s["marks"]), reverse=True)

# # Add rank and total
# ranked_students = []
# for i, s in enumerate(sorted_students, start=1):
#     student_info = {
#         "rank": i,
#         "name": s["name"],
#         "RollNo": s["RollNo"],
#         "total": sum(s["marks"])
#     }
#     ranked_students.append(student_info)

# # Print results
# for s in ranked_students:
#     print(s)



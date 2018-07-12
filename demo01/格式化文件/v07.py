import json

Student = {
    "name" : "wangdamei",
    "age" : 22,
    "gender" : "female",
    "mobile" : "1381213123"
}

print(type(Student))

stu_json = json.dumps(Student)
print(type(stu_json))
print(stu_json)

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)

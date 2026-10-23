print("Hello World!!")
name  = "Saket"
Years = 22
Height = 5.11
hobbies = ["Reading", "Coding", "Travelling"]
Education = {
    "School": "Deepanshu Public sr. sec. School",
    "10TH MARKS": "75.8 %",
    "12TH MARKS": "70.5 %",
}
Graduation ={
    "College": "SGT University",
    "CGPA": 8.07,
    "SGPA": [7.04,7.80,8.08,8.24,8.58,8.65]
}
Holidays = ("Saturday", "Sunday","Government Holidays")
Semesters = {1,2,3,4,5,6,7,8}
Years_Acc_Sem = {1,1,2,2,3,3,4,4}
print("Name:", name)
print("Years:", Years)
print("Height:", Height)
print("Hobbies:", hobbies)
print("Education:", Education)
print("Graduation:", "College Name:-", Graduation["College"])
print(Holidays)
print(Holidays[2])
print(Semesters)
print(Years_Acc_Sem)
print(type(name), type(Years), type(Height), type(hobbies), type(Education),type(Graduation), type(Holidays),type(Semesters))
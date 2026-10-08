INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
with open("C:/Users/polin/OneDrive/Desktop/CS201/students_analysis/students.csv", "r", encoding='utf-8') as f:
    next(f)
    lines = f.readlines()
ls = []
ls_math = []
ls_python = []
ls_english = []

for line in lines:
    info = line.strip().split(",")
    name, grade_1, grade_2, grade_3 = info[0], int(info[1]), int(info[2]), int(info[3])
    average_grade = (grade_1 + grade_2 + grade_3) // 3
    ls.append([name, grade_1, grade_2, grade_3, average_grade])
    ls_math.append(grade_1)
    ls_python.append(grade_2)
    ls_english.append(grade_3)
total_students = len(ls)
total_math = sum(ls_math)
total_python = sum(ls_python)
total_english = sum(ls_english)
average_math = round(total_math / total_students, 1)
average_python = round(total_python / total_students, 1)
average_english = round(total_english / total_students, 1)
with open("C:/Users/polin/OneDrive/Desktop/CS201/students_analysis/result.txt", "w", encoding='utf-8') as f:
    f.write(f"Середній бал по курсу:\n")
    f.write(f"math: {average_math}\n")
    f.write(f"python: {average_python}\n")
    f.write(f"english: {average_english}\n")
print(f"Середній бал по класу:")
print(f"math: {average_math}")
print(f"python: {average_python}")
print(f"english: {average_english}")
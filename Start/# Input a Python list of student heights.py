# بنأخد الأطوال كـ input ونقسمها لقائمة
student_heights = input().split()

# بنحول كل عنصر من نص لرقم
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# متغيرين: واحد للمجموع وواحد لعدد الطلاب
total_height = 0
number_of_students = 0

# بنمشي على كل طول ونضيفه للمجموع ونزوّد العداد
for height in student_heights:
    total_height += height
    number_of_students += 1 # دا ملوش علافة ب total_height، هو بس بيعدّ عدد الطلاب   

# بنحسب المتوسط ونطبع النتائج
average_height = round(total_height / number_of_students)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")
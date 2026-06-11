# Input a list of student scores
student_scores = input().split()

# بنحول كل عنصر في القائمة من نص (string) لرقم (integer)
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# متغير جديد بيبدأ من 0 عشان نحفظ فيه أكبر قيمة
highest = 0

# بنمشي على كل درجة في القائمة واحدة واحدة
for student_scoresX in student_scores:
  
  # بنقارن الدرجة الحالية بأكبر قيمة شفناها لحد دلوقتي
  if student_scoresX > highest:
    
    # لو الدرجة الحالية أكبر، بنحدّث highest بقيمتها
    highest = student_scoresX

# بنطبع أكبر درجة اتحفظت في highest
print(f"The highest score in the class is: {highest}")
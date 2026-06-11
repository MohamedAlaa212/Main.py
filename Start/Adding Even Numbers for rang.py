target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
final = 0
for X in range(2, target + 1, 2): # متنساش + 1 عشان الرينج بتشيل واحد من القيمة نهاية المجموعه يعني ال100 بتبقي 99
    final += X
print(final)
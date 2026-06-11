line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]

map = [line1, line2, line3]

position = input("Hiding your treasure! X marks the spot.\n") # المدخل مثلا b3

letter = position[0].lower() # فبتاخد الحرف الاول من المدخل  دا معني [0] 

abc = ["a", "b", "c"]

letter_index = abc.index(letter) # الكود داوالي قبلة بيحولو الحرف الي في المدخل لرقم يتخزن في المتغير

number_index = int(position[1]) - 1 # بياخد الحرف التاني من المدخل ويحولة ل "انت" بدل "استرنج" ويطرح واحد عشان الليست بتعد من صفر
    
map[letter_index][number_index] = "X" #map[1] place [0] = ["X","⬜️","⬜️"]   ← line2

print(f"{line1}\n{line2}\n{line3}")# طباعه ماب هيخلي اللاينز تبقي جمب بعض انما بالطريقة دي هتطلع تحت بعض وتعمل 

##map[0] = ["⬜️","⬜️","⬜️"]   ← line1
##map[1] = ["⬜️","⬜️","⬜️"]   ← line2
##map[2] = ["⬜️","⬜️","⬜️"]   ← line3
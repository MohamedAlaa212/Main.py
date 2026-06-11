import random

# القوائم الأساسية للحروف والأرقام والرموز
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# بنسأل المستخدم كام حرف وكام رمز وكام رقم يريد في الباسورد
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# بنختار عشوائياً العدد المطلوب من كل قائمة ونجمعهم في قائمة واحدة
password = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers)

# بنخلط القائمة عشوائياً عشان الباسورد ميكونش متوقع الترتيب
random.shuffle(password)

# بنحول القائمة لنص واحد ونطبعه
print("".join(password))


# ======== glossary ========

# random.choices(list, k=n)
# بتختار n عنصر عشوائي من القائمة مع إمكانية التكرار
# مثال: random.choices(['a','b','c'], k=2) → ['a', 'a'] or ['b', 'c']

# k=
# argument بيحدد عدد العناصر اللي عايز تاخدها
# مثال: k=4 يعني اختار 4 عناصر

# random.shuffle(list)
# بتخلط عناصر القائمة عشوائياً في مكانها مباشرة
# مثال: ['a', '1', '#', 'B'] → ['#', 'a', 'B', '1']

# "".join(list)
# بتحول قائمة من حروف لنص واحد متصل
# اللي بين الأقواس ده الفاصل بين العناصر
# مثال: "".join(['a','b','c']) → "abc"
# مثال: "-".join(['a','b','c']) → "a-b-c"

# random.choice(list)
# بتختار عنصر واحد بس عشوائي من القائمة
# الفرق عن choices: مفيش k لأنها دايماً واحد بس
# مثال: random.choice(['a','b','c']) → 'b'